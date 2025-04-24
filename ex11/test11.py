import pytest

from matrix.matrix import Matrix

def test_det_2x2_zero():
    u = Matrix.from_list([[1.0, -1.0], [-1.0, 1.0]])
    assert u.determinant() == pytest.approx(0.0)

def test_det_3x3_scalar():
    u = Matrix.from_list([[2.0,0.0,0.0],[0.0,2.0,0.0],[0.0,0.0,2.0]])
    # det = 2^3 = 8
    assert u.determinant() == pytest.approx(8.0)

def test_det_3x3_general():
    u = Matrix.from_list([[8.0,5.0,-2.0],[4.0,7.0,20.0],[7.0,6.0,1.0]])
    assert u.determinant() == pytest.approx(-174.0)

def test_det_4x4_general():
    u = Matrix.from_list([
        [ 8.0,  5.0, -2.0,  4.0],
        [ 4.0,  2.5, 20.0,  4.0],
        [ 8.0,  5.0,  1.0,  4.0],
        [28.0, -4.0, 17.0,  1.0]
    ])
    assert u.determinant() == pytest.approx(1032.0)

def test_det_non_square_raises():
    with pytest.raises(ValueError):
        Matrix.from_list([[1.0,2.0,3.0],[4.0,5.0,6.0]]).determinant()

def test_det_empty_raises():
    with pytest.raises(ValueError):
        Matrix.from_list([]).determinant()
