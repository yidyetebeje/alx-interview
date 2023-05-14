#!/usr/bin/python3
"""
rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in place without using additional space.

    Args:
      matrix: A n x n 2D matrix.

    Returns:
      None.
    """

    n = len(matrix)
    for i in range(n // 2):
        for j in range(n - i - 1):
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                matrix[n - j - 1][i], matrix[n - i - 1][n -
                                                        j - 1], matrix[j][n - i - 1], matrix[i][j]
