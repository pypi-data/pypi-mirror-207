import pytest
import numpy as np

from mumott.methods.projectors.saxs_projector_numba import SAXSProjectorNumba
from mumott.data_handling import DataContainer
from mumott.data_handling.geometry import GeometryTuple

dc = DataContainer('tests/test_half_circle.h5')
gm = dc.geometry
default_step_size = 1.0

gm_tuples = [GeometryTuple(rotation=np.eye(3), j_offset=0.2, k_offset=0.5),
             GeometryTuple(rotation=np.eye(3)[[2, 0, 1]], j_offset=0.2453, k_offset=0.5222),
             GeometryTuple(rotation=np.eye(3)[[1, 0, 2]], j_offset=-0.2453, k_offset=0.2)]

gm_hash_table = ['277106', '902494', '161751']

kernel_params = [dict(kernel_dimensions=(2, 2), kernel_width=(0.4, 1.2), kernel_type='bessel'),
                 dict(kernel_dimensions=(4, 7), kernel_width=(0.6, 0.2), kernel_type='gaussian'),
                 dict(kernel_dimensions=(3, 1), kernel_width=(0.1, 1.3), kernel_type='rectangular')]

kernel_density = [np.array(((0.25, 0.25), (0.25, 0.25))),
                  np.array([[0.00420072, 0.01253808, 0.02415652, 0.03005694,
                             0.02415652, 0.01253808, 0.00420072],
                           [0.01457805, 0.04351176, 0.08383206, 0.10430868,
                            0.08383206, 0.04351176, 0.01457805],
                           [0.01457805, 0.04351176, 0.08383206, 0.10430868,
                            0.08383206, 0.04351176, 0.01457805],
                           [0.00420072, 0.01253808, 0.02415652, 0.03005694,
                            0.02415652, 0.01253808, 0.00420072]]),
                  np.array([[1 / 3, 1 / 3, 1 / 3]])]
kernel_offsets = [np.array([-0.20100503, -0.20100503, 0.20100503, 0.20100503, -0.60301508,
                            0.60301508, -0.60301508, 0.60301508]),
                  np.array([-4.51127820e-01, -4.51127820e-01, -4.51127820e-01, -4.51127820e-01,
                            -4.51127820e-01, -4.51127820e-01, -4.51127820e-01, -1.50375940e-01,
                            -1.50375940e-01, -1.50375940e-01, -1.50375940e-01, -1.50375940e-01,
                            -1.50375940e-01, -1.50375940e-01,  1.50375940e-01,  1.50375940e-01,
                            1.50375940e-01,  1.50375940e-01,  1.50375940e-01,  1.50375940e-01,
                            1.50375940e-01,  4.51127820e-01,  4.51127820e-01,  4.51127820e-01,
                            4.51127820e-01,  4.51127820e-01,  4.51127820e-01,  4.51127820e-01,
                            -1.71673820e-01, -1.14449213e-01, -5.72246066e-02,  3.05311332e-18,
                            5.72246066e-02,  1.14449213e-01,  1.71673820e-01, -1.71673820e-01,
                            -1.14449213e-01, -5.72246066e-02,  3.05311332e-18,  5.72246066e-02,
                            1.14449213e-01,  1.71673820e-01, -1.71673820e-01, -1.14449213e-01,
                            -5.72246066e-02,  3.05311332e-18,  5.72246066e-02,  1.14449213e-01,
                            1.71673820e-01, -1.71673820e-01, -1.14449213e-01, -5.72246066e-02,
                            3.05311332e-18,  5.72246066e-02,  1.14449213e-01,  1.71673820e-01]),
                  np.array([-3.34448161e-02, 2.48689958e-18, 3.34448161e-02, 4.15667500e-17,
                            4.15667500e-17, 4.15667500e-17])]
kernel_hash = ['202170', '164889', '135780']

fields = [np.array(((0.2, 0.1)*64)).reshape(4, 4, 4, 2)]

projs = [np.array(
             [[[[0.8, 0.4],
              [0.8, 0.4],
              [0.8, 0.4],
              [0.8, 0.4]],
              [[0.6, 0.3],
               [0.6, 0.3],
               [0.6, 0.3],
               [0.6, 0.3]],
              [[0.6, 0.3],
               [0.6, 0.3],
               [0.6, 0.3],
               [0.6, 0.3]],
              [[0.6, 0.3],
               [0.6, 0.3],
               [0.6, 0.3],
               [0.6, 0.3]]]])]

adjs = [np.array([[[[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0., 0.], [0., 0.], [0., 0.], [0., 0.]]],
                  [[[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0., 0.], [0., 0.], [0., 0.], [0., 0.]]],
                  [[[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0., 0.], [0., 0.], [0., 0.], [0., 0.]]],
                  [[[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0.6, 0.3], [0.6, 0.3], [0.6, 0.3], [0.6, 0.3]],
                   [[0., 0.], [0., 0.], [0., 0.], [0., 0.]]]])]

kernels = ['bessel', 'rectangular', 'gaussian', 'asdf']
valid = [True, True, True, False]


@pytest.mark.parametrize('step_size, expected_value', [(0.5, 0.5),
                                                       (0.1, 0.1),
                                                       (1.5, None),
                                                       (-0.5, None)])
def test_step_size(step_size, expected_value):
    if expected_value is None:
        with pytest.raises(ValueError, match=r".* step size .*"):
            pr = SAXSProjectorNumba(gm, step_size)
        with pytest.raises(ValueError, match=r".* step size .*"):
            pr = SAXSProjectorNumba(gm)
            pr.step_size = step_size
    else:
        pr = SAXSProjectorNumba(gm, step_size)
        assert np.isclose(pr.step_size, expected_value)
        pr = SAXSProjectorNumba(gm, default_step_size)
        pr.step_size = step_size
        assert np.isclose(pr.step_size, expected_value)


@pytest.mark.parametrize('gm_tuple, expected_value', [(g, h) for g, h in zip(gm_tuples, gm_hash_table)])
def test_gm_hash(gm_tuple, expected_value):
    dc = DataContainer('tests/test_half_circle.h5')
    geom = dc.geometry
    pr = SAXSProjectorNumba(geom, default_step_size)
    geom[0] = gm_tuple
    assert pr.is_dirty
    pr._update()
    assert expected_value == str(pr._geometry_hash)[:6]


@pytest.mark.parametrize('step_size, expected_value', [(1.0, '388672'),
                                                       (0.5, '685053')])
def test_hash(step_size, expected_value):
    pr = SAXSProjectorNumba(gm, step_size)
    assert expected_value == str(hash(pr))[:6]


@pytest.mark.parametrize('kernel_pars, kernel_dens, kernel_offs, kernel_h',
                         [t for t in
                          zip(kernel_params, kernel_density, kernel_offsets, kernel_hash)])
def test_sampling_kernel(kernel_pars, kernel_dens, kernel_offs, kernel_h):
    pr = SAXSProjectorNumba(gm, default_step_size)
    pr.create_sampling_kernel(**kernel_pars)
    assert np.allclose(kernel_dens, pr.sampling_kernel)
    assert np.allclose(kernel_offs, pr.kernel_offsets)
    assert kernel_h == str(hash(pr))[:6]


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, projs)])
def test_forward(field, proj):
    pr = SAXSProjectorNumba(gm, default_step_size)
    assert np.allclose(proj, pr.forward(field))


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, projs)])
def test_forward_subset(field, proj):
    dc = DataContainer('tests/test_half_circle.h5')
    geo = dc.geometry
    geo.append(geo[0])
    pr = SAXSProjectorNumba(geo, default_step_size)
    p = pr.forward(field, indices=0)
    assert np.allclose(proj, p)
    with pytest.raises(TypeError, match='integer kind'):
        pr.forward(field, indices=np.array('abc'))


@pytest.mark.parametrize('proj, adj', [f for f in zip(projs, adjs)])
def test_adj(proj, adj):
    pr = SAXSProjectorNumba(gm, default_step_size)
    assert np.allclose(adj, pr.adjoint(proj))


@pytest.mark.parametrize('kernel, validity', [t for t in zip(kernels, valid)])
def test_kernel_type(kernel, validity):
    pr = SAXSProjectorNumba(gm, default_step_size)
    if validity is True:
        pr.create_sampling_kernel(kernel_type=kernel)
    else:
        with pytest.raises(ValueError, match='.* kernel .*'):
            pr.create_sampling_kernel(kernel_type=kernel)


def test_str():
    dc = DataContainer('tests/test_half_circle.h5')
    pr = SAXSProjectorNumba(dc.geometry)
    string = str(pr)
    assert '981cce' in string


def test_html():
    dc = DataContainer('tests/test_half_circle.h5')
    pr = SAXSProjectorNumba(dc.geometry)
    html = pr._repr_html_()
    assert '981cce' in html
