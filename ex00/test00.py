import pytest
from ex00.vector import Vector
from ex00.matrix import Matrix

# Vector tests
def test_vector_addition():
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.add(v)
    assert u.data == [7.0, 10.0]

def test_vector_addition_mismatched_dimensions():
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0, 1.0])
    with pytest.raises(ValueError):
        u.add(v)

def test_vector_subtraction():
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.sub(v)
    assert u.data == [-3.0, -4.0]

def test_vector_subtraction_mismatched_dimensions():
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0, 1.0])
    with pytest.raises(ValueError):
        u.sub(v)

def test_vector_scaling():
    u = Vector([2.0, 3.0])
    u.scl(2)
    assert u.data == [4.0, 6.0]

def test_vector_empty():
    u = Vector([])
    v = Vector([])
    with pytest.raises(ValueError):
        u.sub(v)

# Matrix tests
def test_matrix_addition():
    A = Matrix([[1.0,2.0],[3.0,4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    A.add(B)
    assert A.data == [[6.0, 8.0], [10.0, 12.0]]

def test_matrix_addition_mismatched_dimensions():
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0, 1.0], [7.0, 8.0, 1.0]])
    with pytest.raises(ValueError):
         A.add(B)

def test_matrix_subtraction():
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    A.sub(B)
    assert A.data == [[-4.0, -4.0], [-4.0, -4.0]]

def test_matrix_subtraction_mismatched_dimensions():
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0, 1.0], [7.0, 8.0, 1.0]])
    with pytest.raises(ValueError):
         A.sub(B)

def test_matrix_scaling():
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    A.scl(2)
    assert A.data == [[2.0, 4.0], [6.0, 8.0]]

def test_matrix_empty():
	A = Matrix([])
	B = Matrix([])
	with pytest.raises(ValueError):
		A.add(B)