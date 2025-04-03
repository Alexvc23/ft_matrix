import pytest
from .vector import Vector

def test_dot_zero():
    # Dot product with a zero vector should return 0.0.
    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])
    assert u.dot(v) == 0.0

def test_dot_identity():
    # Dot product of two vectors [1.0, 1.0] should be 2.0.
    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    assert u.dot(v) == 2.0

def test_dot_negative():
    # Dot product of [-1.0, 6.0] and [3.0, 2.0] should be (-1*3) + (6*2) = -3 + 12 = 9.0.
    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    assert u.dot(v) == 9.0

def test_dot_mismatched_sizes():
    # Attempting to dot vectors of different sizes should raise a ValueError.
    u = Vector([1.0, 2.0])
    v = Vector([1.0, 2.0, 3.0])
    with pytest.raises(ValueError):
        u.dot(v)
