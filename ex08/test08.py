import pytest

from matrix.matrix import Matrix


def test_trace_2x2_identity():
    u = Matrix.from_list([[1.0, 0.0],
                          [0.0, 1.0]])
    assert u.trace() == pytest.approx(2.0)

def test_trace_3x3_positive():
    u = Matrix.from_list([[2.0, -5.0, 0.0],
                          [4.0, 3.0,  7.0],
                          [-2.0,3.0,  4.0]])
    assert u.trace() == pytest.approx(9.0)

def test_trace_3x3_negative():
    u = Matrix.from_list([[-2.0, -8.0, 4.0],
                          [ 1.0,-23.0, 4.0],
                          [ 0.0,  6.0, 4.0]])
    assert u.trace() == pytest.approx(-21.0)

def test_trace_non_square_raises():
    u = Matrix.from_list([[1.0, 2.0, 3.0],
                          [4.0, 5.0, 6.0]])
    with pytest.raises(ValueError):
        u.trace()

def test_trace_empty_raises():
    with pytest.raises(ValueError, match="Matrix cannot be empty or contain empty rows"):
        u = Matrix.from_list([])
