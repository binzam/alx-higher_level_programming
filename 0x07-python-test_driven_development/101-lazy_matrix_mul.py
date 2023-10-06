#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    """

    return (numpy.matmul(m_a, m_b))
