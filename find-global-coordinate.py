"""
Author: Eduardo Gomez
"""
import argparse

import numpy as np
from numpy import ndarray

# Parsing args

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=float, help="lengs of arms", nargs=2)
parser.add_argument("--theta", type=float, help="length of the second arm", nargs=2)
args = parser.parse_args()
a, theta = args.a, args.theta
a1, a2 = a
theta1, theta2 = theta


def rot2d(theta: int) -> ndarray:
    """Rotation matrix in 2 dimensions"""
    theta = np.deg2rad(theta)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def get_homogenous_matrix_from_coordinates(angle: int, length: float) -> ndarray:
    """
    Gets the homogenous matrix from angle and length
    """
    # Get the rotation matrix
    rot = rot2d(angle)

    # Get the coordinates of the end of the arm
    arm_length = np.array([length, 0])
    arm_length = np.reshape(arm_length, (2, 1))
    initial_position = rot @ arm_length

    # Block puts the vectors or matrixes together as long as dimension match
    return np.block([[rot, initial_position], [np.zeros((1, 2)), 1]])


def calculate_global_position_homogenous(
    a1: float, a2: float, theta1: int, theta2: int
):
    """
    Calculates the final position given the arm lengths and the angles
    """
    T1G = get_homogenous_matrix_from_coordinates(theta1, a1)
    T2G = get_homogenous_matrix_from_coordinates(theta2, a2)

    # Find the global position of the end effector
    # this is equivalent as T1G x [a2cos(theta2), a2sin(theta2), 0], but
    # it leaves the result in the [0:2, 2] coords
    global_matrix = T1G @ T2G
    global_point = global_matrix[0:2, 2]

    # The coordinate is on this part of the global point
    return global_point, T1G, T2G


global_point, T1G, T2G = calculate_global_position_homogenous(a1, a2, theta1, theta2)


# print(f"T1G: \n{T1G}")
# print(f"T2G:\n{T2G}")
# print(f"Global point: {global_point}")
print("P(x_G, y_G) = ", global_point)
