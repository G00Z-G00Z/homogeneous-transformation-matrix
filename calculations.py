import numpy as np
from numpy import ndarray


def rot2d(theta: int) -> ndarray:
    theta = np.deg2rad(theta)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def get_initial_arm_coordinates(angle: int, length: float) -> ndarray:
    """Gets the initial arm coordinates with angle and length"""
    # Get the rotation matrix
    rot = rot2d(angle)

    # Get the coordinates of the end of the arm
    end = np.array([[length], [0]])

    return rot @ end


def get_homogenous_matrix_from_coordinates(angle: int, length: float) -> ndarray:
    """
    Gets the homogenous matrix from angle and length
    """
    # Get the rotation matrix
    rot = rot2d(angle)

    # Get the coordinates of the end of the arm
    arm_length = np.array([length, 0]).T
    arm_length = np.reshape(arm_length, (2, 1))
    end = rot @ arm_length
    return np.block([[rot, end], [np.zeros((1, 2)), 1]])


def calculate_global_position_homogenous(
    a1: float, a2: float, theta1: int, theta2: int
):
    """
    Calculates the final position given the arm lengths and the angles
    """
    T1G = get_homogenous_matrix_from_coordinates(theta1, a1)
    T2G = get_homogenous_matrix_from_coordinates(theta2, a2)

    # Find the global position of the end effector
    global_point = T1G @ T2G

    return global_point[0:2, 2], T1G, T2G


def calculate_global_position_not_homogenous(
    a1: float, a2: float, theta1: int, theta2: int
):
    # Find T1G which is the homogeneous transformation matrix from frame 1 to frame G
    rotation1 = rot2d(theta1)
    translation1 = get_initial_arm_coordinates(theta1, a1)

    # Find T2G which is the homogeneous transformation matrix from frame 2 to frame G
    translation2 = get_initial_arm_coordinates(theta2, a2)

    # Find the global position of the end effector
    global_point = rotation1 @ translation2 + translation1

    return global_point


# %%

a1 = 0.04  # cm
a2 = a1  # cm
theta1 = 30  # degrees
theta2 = 45  # degrees

global_point, T1G, T2G = calculate_global_position_homogenous(a1, a2, theta1, theta2)

print(f"T1G: {T1G}")
print(f"T2G: {T2G}")
print(f"Global point: {global_point}")
