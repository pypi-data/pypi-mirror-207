import logging

from typing import Dict, Any

from scipy.optimize import minimize

from ...core.hashing import list_to_hash
from .base_optimizer import Optimizer
from ..loss_functions.base_loss_function import LossFunction


logger = logging.getLogger(__name__)


class LBFGS(Optimizer):
    """This ``Optimizer`` makes the ``L-BFGS-B`` algorithm from `scipy.optimize
    <https://docs.scipy.org/doc/scipy/reference/optimize.html>`_
    available for usage with an ``LossFunction``.

    Parameters
    ----------
    loss_function : LossFunction
        The objective function to be optimized for using this algorithm.
    kwargs : Dict[str, Any]
        Miscellaneous options. See notes for valid entries.

    Notes
    -----
    Valid entries in :attr:`kwargs` are
        x0
            Initial guess for solution vector. Must be the same size as
            :attr:`functional.coefficients`. Defaults to :attr:`loss_function.initial_values`.
        bounds
            Used to set the ``bounds`` of the optimization method, see `scipy.optimize.minimize
            <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`_
            documentation for details. Defaults to ``None``.
        maxiter
            Maximum number of iterations. Defaults to ``10``.
        disp
            Whether to display output from the optimizer. Defaults to ``True``
        maxcor
            Maximum number of Hessian corrections to the Jacobian. Defaults to ``10``.
        iprint
            If ``disp`` is true, controls output with no output if ``iprint < 0``,
            convergence output only if ``iprint == 0``, iteration-wise output if
            ``0 < iprint <= 99``, and sub-iteration output if ``iprint > 99``.
        maxfun
            Maximum number of function evaluations, including line search evaluations.
            Defaults to ``20``.
        ftol
            Relative change tolerance for objective function. Changes to absolute change tolerance
            if objective function is ``< 1``, see `scipy.optimize.minimize
            <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`_
            documentation, which may lead to excessively fast convergence.
            Defaults to ``1e-3``.
        gtol
            Convergence tolerance for gradient. Defaults to ``1e-5``.
    """

    def __init__(self,
                 loss_function: LossFunction,
                 **kwargs: Dict[str, Any]):
        super().__init__(loss_function, **kwargs)
        # This will later be used to reshape the flattened output.
        self._output_shape = None

    def optimize(self) -> Dict:
        """ Executes the optimization using the options stored in this class
        instance. The optimization will continue to run until convergence,
        or until the maximum number of iterations (``'maxiter'``) is exceeded.

        Returns
        -------
            A ``dict`` of optimization results. See `scipy.optimize.OptimizeResult
            <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html>`_
            for details. The entry ``'x'``, which contains the result, will be reshaped using
            the shape of the gradient from :attr:`loss_function`.
        """
        lbfgs_kwargs = dict(x0=self._loss_function.initial_values,
                            bounds=None)
        misc_options = dict(maxiter=10,
                            disp=True,
                            maxcor=10,
                            iprint=1,
                            maxfun=20,
                            ftol=1e-3,
                            gtol=1e-5)

        for k in lbfgs_kwargs:
            if k in dict(self):
                lbfgs_kwargs[k] = self[k]

        for k in misc_options:
            if k in dict(self):
                misc_options[k] = self[k]

        for k in dict(self):
            if k not in lbfgs_kwargs and k not in misc_options:
                logger.warning(f'Unknown option {k}, with value {self[k]}, has been ignored.')
        lbfgs_kwargs['x0'] = lbfgs_kwargs['x0'].ravel()

        def loss_function_wrapper(coefficients):
            d = self._loss_function.get_loss(coefficients, get_gradient=True)
            # Store gradient shape to reshape flattened output.
            if self._output_shape is None:
                self._output_shape = d['gradient'].shape
            return d['loss'], d['gradient'].ravel()

        result = minimize(fun=loss_function_wrapper, **lbfgs_kwargs,
                          jac=True, method='L-BFGS-B', options=misc_options)
        result = dict(result)
        result['x'] = result['x'].reshape(self._output_shape)
        return dict(result)

    def __hash__(self) -> int:
        to_hash = [self._options, hash(self._loss_function)]
        return int(list_to_hash(to_hash), 16)
