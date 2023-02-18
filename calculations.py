# %%
import numpy as np

# Function that returns a 2x2 rotation matrix given an angle in degrees


# %%
def rot2d(theta):
    theta = np.deg2rad(theta)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


# %%
# Functions that returns a 2x1 vector with the coordinates of a point, when giving an angle and a lenght
def get_initial_arm_coordinates(angle, length):
    # Get the rotation matrix
    rot = rot2d(angle)

    # Get the coordinates of the end of the arm
    end = np.array([[length], [0]])

    return rot @ end


# %%

a1 = 0.04  # cm
a2 = a1  # cm
theta1 = 30  # degrees
theta2 = 45  # degrees

# Find T1G which is the homogeneous transformation matrix from frame 1 to frame G

rotation1 = rot2d(theta1)
translation1 = get_initial_arm_coordinates(theta1, a1)

# Find T2G which is the homogeneous transformation matrix from frame 2 to frame G

rotation2 = rot2d(theta2)
translation2 = get_initial_arm_coordinates(theta2, a2)

global_point = rotation1 @ translation2 + translation1

print(global_point)

# %%
