import pytest
from .vector import Vector
from .matrix import Matrix

def test_vector_lerp():
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])
    result = Vector.lerp(v1, v2, 0.3)
    expected = [2.6, 1.3]
    assert result.data == expected

def test_vector_lerp_invalid_t():
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])
    with pytest.raises(ValueError):
        Vector.lerp(v1, v2, -0.1)
    with pytest.raises(ValueError):
        Vector.lerp(v1, v2, 1.1)

def test_vector_lerp_mismatched_size():
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0])
    with pytest.raises(ValueError):
        Vector.lerp(v1, v2, 0.5)

def test_matrix_lerp():
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    result = Matrix.lerp(m1, m2, 0.5)
    expected = [[11.0, 5.5], [16.5, 22.0]]
    assert result.data == expected

def test_matrix_lerp_invalid_t():
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    with pytest.raises(ValueError):
        Matrix.lerp(m1, m2, -0.2)
    with pytest.raises(ValueError):
        Matrix.lerp(m1, m2, 1.2)

def test_matrix_lerp_mismatched_size():
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0, 5.0], [30.0, 40.0, 15.0]])
    with pytest.raises(ValueError):
        Matrix.lerp(m1, m2, 0.5)

