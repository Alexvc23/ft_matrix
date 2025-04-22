import pytest

from matrix.matrix import Matrix


def test_transpose_square():
    m = Matrix.from_list([[1.0, 2.0], [3.0, 4.0]])
    t = m.transpose()
    assert t.data == [[1.0, 3.0], [2.0, 4.0]]

def test_transpose_rectangular_wider():
    m = Matrix.from_list([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    t = m.transpose()
    assert t.data == [
        [1.0, 4.0],
        [2.0, 5.0],
        [3.0, 6.0]
    ]

def test_transpose_rectangular_taller():
    m = Matrix.from_list([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    t = m.transpose()
    assert t.data == [
        [1.0, 3.0, 5.0],
        [2.0, 4.0, 6.0]
    ]

def test_transpose_single_row():
    m = Matrix.from_list([[7.0, 8.0, 9.0]])
    t = m.transpose()
    assert t.data == [[7.0], [8.0], [9.0]]

def test_transpose_single_column():
    m = Matrix.from_list([[7.0], [8.0], [9.0]])
    t = m.transpose()
    assert t.data == [[7.0, 8.0, 9.0]]

def test_invalid_empty_matrix():
    with pytest.raises(ValueError):
        Matrix.from_list([])

def test_invalid_jagged_matrix():
    with pytest.raises(ValueError):
        Matrix.from_list([[1.0, 2.0], [3.0]])
