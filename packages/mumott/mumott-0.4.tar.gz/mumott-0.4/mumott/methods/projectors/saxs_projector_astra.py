try:
    import astra
except ImportError:
    raise ImportError('ASTRA is not installed. SAXSProjectorAstra is not available.')

import logging
import numpy as np
from numpy.typing import NDArray
from ... import Geometry
from ...core.hashing import list_to_hash
from .base_projector import Projector


logger = logging.getLogger(__name__)


class SAXSProjectorAstra(Projector):
    """
    Projector for transforms of tensor fields from three-dimensional space
    to projection space.

    This version utilizes the high-performance toolbox ASTRA (https://www.astra-toolbox.com/)
    It provides a minimal wrapper on top of the existing python-bindings to conform with
    the way mumott parametrizes the geometry.

    Parameters
    ----------
    geometry : Geometry
        An instance of :class:`Geometry <mumott.Geometry>` containing the
        necessary vectors to compute forwared and adjoint projections.
    """

    def __init__(self,
                 geometry: Geometry):
        super().__init__(geometry)
        self._has_astra_objects = False
        self._update(force_update=True)

    def _geometry_to_astra_vec(self):
        """
        Transform geometric information as represented in mumott to the way
        it is represented in ASTRA.
        """
        # rename things
        geom = self._geometry
        number_of_projections = len(geom.rotations)
        p_0 = geom.p_direction_0
        j_0 = geom.j_direction_0
        k_0 = geom.k_direction_0

        # initialize vec_array
        self._astra_vec = np.zeros((number_of_projections, 12))

        # loop over all projections. (Could be sped up by vectorization.)
        for i in range(number_of_projections):
            R = geom._rotations[i].T
            p = R @ p_0
            j = R @ j_0
            k = R @ k_0
            shift_in_xyz = j * geom.j_offsets[i] + k * geom.k_offsets[i]

            # make ASTRA-style output
            self._astra_vec[i, :] = (*p, *shift_in_xyz, *j, *k)

    def _set_up_astra_objects(self):
        """
        Initialize ASTRA object (allocate arrays on the graphics card)
        """
        # (in astra x means index number 2!)
        self.proj_geom = astra.create_proj_geom('parallel3d_vec',
                                                self._geometry.projection_shape[1],
                                                self._geometry.projection_shape[0],
                                                self._astra_vec)

        # Astra syntax is (y, x, z)
        # See https://www.astra-toolbox.com/docs/geom3d.html
        self.vol_geom = astra.create_vol_geom(self._geometry.volume_shape[1],
                                              self._geometry.volume_shape[0],
                                              self._geometry.volume_shape[2])

        # Allocate arrays on the GPU with zeros
        self.astra_volume_id = astra.data3d.create('-vol', self.vol_geom)
        self.astra_sino_id = astra.data3d.create('-sino', self.proj_geom)

        # Set up the projection and back-projection algorithms
        config = dict(type='FP3D_CUDA',
                      ProjectionDataId=self.astra_sino_id,
                      VolumeDataId=self.astra_volume_id)
        self.proj_algorithm_id = astra.algorithm.create(config)

        config = dict(type='BP3D_CUDA',
                      ProjectionDataId=self.astra_sino_id,
                      ReconstructionDataId=self.astra_volume_id)
        self.bp_algorithm_id = astra.algorithm.create(config)

    def forward(self,
                field: NDArray,
                indices: NDArray[int] = None) -> NDArray:
        """Compute the forward projection of a tensor field.

        Parameters
        ----------
        field
            An array containing coefficients in its fourth dimension,
            which are to be projected into two dimensions. The first three
            dimensions should match the :attr:`volume_shape` of the sample.
        indices
            Must be ``None`` since the computation of individual projections
            is not supported for this projector.

        Returns
        -------
            An array with four dimensions ``(I, J, K, L)``, where
            the first dimension corresponds to projection index.
            The second and third dimension contain the pixels in the
            ``J`` and ``K`` dimension respectively, whereas
            the last dimension is the coefficient dimension, matching
            ``field[-1]``.
        """
        if not np.allclose(field.shape[:-1], self._geometry.volume_shape):
            raise ValueError(f'The shape of the input field ({field.shape}) does not match the'
                             f' volume shape expected by the projector ({self._geometry.volume_shape})')
        self._update()
        if indices is None:
            return self._forward_stack(field)
        else:
            raise NotImplementedError('The SAXSProjectorAstra object does not support the'
                                      ' computation of individual projections.')

    def _forward_stack(self,
                       volume: NDArray) -> NDArray:
        """Internal method for forward projecting an entire stack.

        Parameters
        ----------
        field
            The field to be projected.

        Returns
        -------
            The resulting projections.
        """
        if len(volume.shape) == 3:
            # Scalar projection of a 3D volume

            # move data to GPU
            astra.data3d.store(self.astra_volume_id, volume.transpose((2, 1, 0)))
            astra.data3d.store(self.astra_sino_id, 0)

            # carry out projection
            astra.algorithm.run(self.proj_algorithm_id)

            # move data back to system RAM and return
            return astra.data3d.get(self.astra_sino_id).transpose((1, 2, 0))

        elif len(volume.shape) == 4:
            # initialize output array
            number_of_channels = volume.shape[3]
            output_array = np.zeros((len(self._geometry.rotations),
                                     *self._geometry.projection_shape,
                                     number_of_channels))

            # loop over channels and carry out a scalar projection
            for channel_number in range(volume.shape[3]):
                output_array[..., channel_number] = self._forward_stack(volume[..., channel_number])

            return output_array

    def adjoint(self,
                projections: NDArray,
                indices: NDArray[int] = None) -> NDArray:
        """Compute the adjoint of a set of projections according to the system geometry.

        Parameters
        ----------
        projections
            An array containing coefficients in its last dimension,
            from e.g. the residual of measured data and forward projections.
            The first dimension should match :attr:`indices` in size, and the
            second and third dimensions should match the system projection geometry.
        indices
            A one-dimensional array containing one or more indices
            indicating from which projections the adjoint is to be computed.

        Returns
        -------
            The adjoint of the provided projections.
            An array with four dimensions ``(X, Y, Z, P)``, where the first
            three dimensions are spatial and the last dimension runs over
            coefficients.
        """
        if not np.allclose(projections.shape[-3:-1], self._geometry.projection_shape):
            raise ValueError(f'The shape of the projections ({projections.shap}) does not match the'
                             f' volume shape expected by the projector ({self._geometry.projection_shape})')
        self._update()

        if indices is None or indices.size == len(self._geometry):
            return self._adjoint_stack(projections)
        else:
            raise NotImplementedError('The SAXSProjectorAstra object does not support the'
                                      ' computation of individual projections.')

        return self._adjoint_subset(projections, indices)

    def _adjoint_stack(self,
                       sinograms: NDArray) -> NDArray:
        """Internal method for computing the adjoint of a whole stack of projections.

        Parameters
        ----------
        projections
            An array containing coefficients in its last dimension,
            from e.g. the residual of measured data and forward projections.
            The first dimension should run over all the projection directions
            in the system geometry.

        Returns
        -------
            The adjoint of the provided projections.
            An array with four dimensions ``(X, Y, Z, P)``, where the first
            three dimensions are spatial, and the last dimension runs over
            coefficients.
        """

        if len(sinograms.shape) == 3:
            # Scalar back-projection

            # copy data to GPU RAM
            astra.data3d.store(self.astra_volume_id, 0)
            astra.data3d.store(self.astra_sino_id, sinograms.transpose((2, 0, 1)))

            # carry out back-projection
            astra.algorithm.run(self.bp_algorithm_id)

            # move data back to system RAM and return
            return astra.data3d.get(self.astra_volume_id).transpose((2, 1, 0))

        elif len(sinograms.shape) == 4:
            # initialize output array
            number_of_channels = sinograms.shape[3]
            output_array = np.zeros((*self._geometry.volume_shape, number_of_channels))

            # loop over channels and carry out scalar projection
            for channel_number in range(sinograms.shape[3]):
                output_array[..., channel_number] = self._adjoint_stack(
                    sinograms[..., channel_number])

            return output_array

    def _update(self,
                force_update: bool = False) -> None:
        super()._update(force_update)  # This quits the function if not dirty (hidden in .super)

        self._geometry_to_astra_vec()
        if self._has_astra_objects:
            astra.astra.delete([self.astra_volume_id,
                                self.astra_sino_id,
                                self.proj_algorithm_id,
                                self.bp_algorithm_id])

        self._set_up_astra_objects()
        self._has_astra_objects = True
        self._geometry_hash = hash(self._geometry)

    def __hash__(self) -> int:
        to_hash = [self._geometry_hash, hash(self._geometry)]
        return int(list_to_hash(to_hash), 16)

    def __str__(self) -> str:
        wdt = 74
        s = []
        s += ['-' * wdt]
        s += [self.__class__.__name__.center(wdt)]
        s += ['-' * wdt]
        with np.printoptions(threshold=4, edgeitems=2, precision=5, linewidth=60):
            s += ['{:18} : {}'.format('is_dirty', self.is_dirty)]
            s += ['{:18} : {}'.format('hash', hex(hash(self))[2:8])]
        s += ['-' * wdt]
        return '\n'.join(s)

    def _repr_html_(self) -> str:
        s = []
        s += [f'<h3>{self.__class__.__name__}</h3>']
        s += ['<table border="1" class="dataframe">']
        s += [
            '<thead><tr><th style="text-align: left;">Field</th><th>Size</th><th>Data</th></tr></thead>'
        ]
        s += ['<tbody>']
        with np.printoptions(threshold=4, edgeitems=2, precision=2, linewidth=40):
            s += ['<tr><td style="text-align: left;">is_dirty</td>']
            s += [f'<td>1</td><td>{self.is_dirty}</td></tr>']
            s += ['<tr><td style="text-align: left;">hash</td>']
            s += [
                f'<td>{len(hex(hash(self)))}</td><td>{hex(hash(self))[2:8]}</td></tr>'
            ]
        s += ['</tbody>']
        s += ['</table>']
        return '\n'.join(s)
