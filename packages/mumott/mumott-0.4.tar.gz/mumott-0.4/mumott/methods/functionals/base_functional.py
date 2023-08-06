from abc import ABC, abstractmethod
from typing import Dict

from ... import DataContainer
from ..basis_sets.base_basis_set import BasisSet
from ..projectors.base_projector import Projector


class Functional(ABC):

    """This is the base class from which specific functionals are being derived.
    """

    def __init__(self,
                 data_container: DataContainer,
                 basis_set: BasisSet,
                 projector: Projector):
        pass

    @abstractmethod
    def get_residuals(self) -> Dict:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def _repr_html_(self) -> str:
        pass
