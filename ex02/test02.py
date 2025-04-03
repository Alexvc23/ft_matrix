import pytest
from vector import Vector
from matrix import Matrix
from main import lerp

def test_lerp_numbers():
    assert lerp(0., 1., 0.) == 0.0
    assert lerp(0., 1., 1.) == 1.0
    assert lerp(0., 1., 0.5) == 0.5
    assert lerp(21., 42., 0.3) == pytest.approx(27.3)

def test_lerp_vectors():
    v1 = Vector.from_list([2., 1.])
    v2 = Vector.from_list([4., 2.])
    result = lerp(v1, v2, 0.3)
    expected = Vector.from_list([2.6, 1.3])
    # Compare element-wise using pytest.approx for floats
    assert result.data == pytest.approx(expected.data)

def test_lerp_matrices():
    m1 = Matrix.from_list([[2., 1.], [3., 4.]])
    m2 = Matrix.from_list([[20., 10.], [30., 40.]])
    result = lerp(m1, m2, 0.5)
    expected = Matrix.from_list([[11., 5.5], [16.5, 22.]])
    for row_res, row_exp in zip(result.data, expected.data):
        assert row_res == pytest.approx(row_exp)

def test_lerp_invalid_t():
    v1 = Vector.from_list([2., 1.])
    v2 = Vector.from_list([4., 2.])
    with pytest.raises(ValueError):
        lerp(v1, v2, -0.1)
    with pytest.raises(ValueError):
        lerp(v1, v2, 1.1)

def test_lerp_type_mismatch():
    with pytest.raises(TypeError):
        lerp(0., Vector.from_list([1., 2.]), 0.5)
