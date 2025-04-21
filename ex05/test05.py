import pytest

from vector.vector import Vector

def test_angle_cos_parallel():
    # Two identical vectors: cosine should be 1.0.
    u = Vector.from_list([1.0, 0.0])
    v = Vector.from_list([1.0, 0.0])
    assert Vector.angle_cos(u, v) == pytest.approx(1.0)

def test_angle_cos_orthogonal():
    # Two perpendicular vectors: cosine should be 0.0.
    u = Vector.from_list([1.0, 0.0])
    v = Vector.from_list([0.0, 1.0])
    assert Vector.angle_cos(u, v) == pytest.approx(0.0)

def test_angle_cos_opposite():
    # Vectors pointing in opposite directions: cosine should be -1.0.
    u = Vector.from_list([-1.0, 1.0])
    v = Vector.from_list([1.0, -1.0])
    # Dot = (-1)*1 + (1)*(-1) = -2; Norms: sqrt(2)*sqrt(2)=2; -2/2 = -1.
    assert Vector.angle_cos(u, v) == pytest.approx(-1.0)

def test_angle_cos_collinear():
    # Collinear vectors: cosine should be 1.0.
    u = Vector.from_list([2.0, 1.0])
    v = Vector.from_list([4.0, 2.0])
    assert Vector.angle_cos(u, v) == pytest.approx(1.0)

def test_angle_cos_general():
    # General 3-dimensional example.
    u = Vector.from_list([1.0, 2.0, 3.0])
    v = Vector.from_list([4.0, 5.0, 6.0])
    # Expected cosine is approximately 0.974631846.
    assert Vector.angle_cos(u, v) == pytest.approx(0.974631846)

def test_angle_cos_mismatched_size():
    u = Vector.from_list([1.0, 2.0])
    v = Vector.from_list([1.0, 2.0, 3.0])
    with pytest.raises(ValueError):
        Vector.angle_cos(u, v)

def test_angle_cos_zero_vector():
    u = Vector.from_list([0.0, 0.0])
    v = Vector.from_list([1.0, 2.0])
    with pytest.raises(ValueError):
        Vector.angle_cos(u, v)
