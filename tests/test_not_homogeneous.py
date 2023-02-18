from .fixtures import cases
import numpy as np
from calculations import calculate_global_position_not_homogenous


def test_not_homogeneous_cases(cases):
    for case in cases:
        global_point = calculate_global_position_not_homogenous(
            case.a1, case.a2, case.theta1, case.theta2
        )
        global_point = np.reshape(global_point, (1, 2))
        case.expected = np.reshape(case.expected, (1, 2))
        assert np.allclose(global_point, case.expected), "Coordinates did not match"
