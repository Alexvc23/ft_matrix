import pytest

from matrix.matrix import Matrix

def approx_matrix(mat1, mat2, tol=1e-6):
    assert len(mat1) == len(mat2)
    for row1, row2 in zip(mat1, mat2):
        assert len(row1) == len(row2)
        for a, b in zip(row1, row2):
            assert pytest.approx(b, abs=tol) == a

def test_identity_3x3():
    u = Matrix.from_list([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])
    r = u.row_echelon()
    approx_matrix(r.data, u.data)

def test_simple_2x2():
    u = Matrix.from_list([[1.0, 2.0], [3.0, 4.0]])
    r = u.row_echelon()
    approx_matrix(r.data, [[1.0, 0.0], [0.0, 1.0]])

def test_degenerate_2x2():
    u = Matrix.from_list([[1.0, 2.0], [2.0, 4.0]])
    r = u.row_echelon()
    approx_matrix(r.data, [[1.0, 2.0], [0.0, 0.0]])

def test_full_example_3x5():
    u = Matrix.from_list([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0, 1.0, 4.0, 17.0]
    ])
    r = u.row_echelon()
    expected = [
        [1.0,         0.625,      0.0, 0.0,      -12.1666667],
        [0.0,         0.0,        1.0, 0.0,       -3.6666667],
        [0.0,         0.0,        0.0, 1.0,        29.5      ]
    ]
    approx_matrix(r.data, expected)
