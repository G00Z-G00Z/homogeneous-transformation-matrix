import numpy as np
from calculations import get_homogenous_matrix_from_coordinates


# Test for making a homogenous matrix


def test_homogenous_matrix():
    # Test that the homogenous matrix is correct
    assert np.allclose(
        get_homogenous_matrix_from_coordinates(0, 1),
        np.array([[1, 0, 1], [0, 1, 0], [0, 0, 1]]),
    )
