import pytest

from vector.vector import Vector
from matrix.matrix import Matrix


def test_mul_vec_identity():
    A = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Vector([5.0, -3.0])
    w = A.mul_vec(v)
    assert w.data == [5.0, -3.0]

def test_mul_vec():
    A = Matrix([[2.0, 0.0], [0.0, 3.0]])
    v = Vector([4.0, 5.0])
    w = A.mul_vec(v)
    assert w.data == [8.0, 15.0]

def test_mul_mat_identity():
    A = Matrix([[1.0, 0.0], [0.0, 1.0]])
    B = Matrix([[7.0, 8.0], [9.0, 10.0]])
    C = A.mul_mat(B)
    assert C.data == [[7.0, 8.0], [9.0, 10.0]]

def test_mul_mat():
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[2.0, 0.0], [1.0, 2.0]])
    C = A.mul_mat(B)
    assert C.data == [[4.0, 4.0], [10.0, 8.0]]

def test_mul_mat_mismatch():
    A = Matrix([[1.0, 2.0, 3.0]])
    B = Matrix([[1.0, 2.0], [3.0, 4.0]])
    with pytest.raises(ValueError):
        A.mul_mat(B)

def test_examples():
    print("\n--- Example 1: Matrix-Vector Multiplication ---")
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v1 = Vector([1.0, 1.0])
    print(f"A = {A}")
    print(f"v1 = {v1}")
    result1 = A.mul_vec(v1)
    print("A * v1 =", result1)
    assert result1.data == [3.0, 7.0] # Added assertion

def test_mul_mat_scaling():
    B = Matrix([[2.0, 0.0], [0.0, 2.0]])
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    result = A.mul_mat(B)
    assert result.data == [[2.0, 4.0], [6.0, 8.0]]

def test_identity_matrix_vector():
    C = Matrix([[1., 0.], [0., 1.]])
    v2 = Vector([4., 2.])
    result = C.mul_vec(v2)
    assert result.data == [4.0, 2.0]

def test_mul_mat_general():
    D = Matrix([[1., 2.], [3., 4.]])
    E = Matrix([[5., 6.], [7., 8.]])
    result = D.mul_mat(E)
    assert result.data == [[19.0, 22.0], [43.0, 50.0]]

def test_mul_vec_rectangular():
    F = Matrix([[1., 2.], [3., 4.], [5., 6.]])
    v3 = Vector([1., 2.])
    result = F.mul_vec(v3)
    assert result.data == [5.0, 11.0, 17.0]

def test_mul_mat_rectangular():
    F = Matrix([[1., 2.], [3., 4.], [5., 6.]])
    E = Matrix([[5., 6.], [7., 8.]])
    result = F.mul_mat(E)
    assert result.data == [[19.0, 22.0], [43.0, 50.0], [67.0, 78.0]]