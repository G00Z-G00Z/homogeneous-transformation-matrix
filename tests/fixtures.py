from dataclasses import dataclass
from numpy import ndarray
import pytest
import numpy as np


@dataclass
class Case:
    a1: int
    a2: int
    theta1: int
    theta2: int
    expected: ndarray


@pytest.fixture
def cases():
    return [
        Case(0.04, 0.04, 30, 30, np.array([0.05464102, 0.05464102])),
        Case(0.04, 0.04, 30, 45, np.array([0.04499378, 0.05863703])),
    ]
