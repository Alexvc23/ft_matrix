from .vector import Vector

def test_linear_combination_basic():
    vectors = [[1, 2, 3], [4, 5, 6]]
    scalars = [2, 1]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [6.0, 9.0, 12.0]

def test_linear_combination_zero_scalars():
    vectors = [[1, 2, 3], [4, 5, 6]]
    scalars = [0, 0]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [0.0, 0.0, 0.0]

def test_linear_combination_single_vector():
    vectors = [[1, 2, 3]]
    scalars = [2]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [2.0, 4.0, 6.0]

def test_linear_combination_negative_scalars():
    vectors = [[1, 2, 3], [4, 5, 6]]
    scalars = [-1, -2]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [-9.0, -12.0, -15.0]

def test_linear_combination_different_lengths():
    """
    Test linear combination with vectors and scalars of different lengths.

    This test checks if the linear_combination method correctly raises a ValueError
    when the number of vectors does not match the number of scalars.

    Test expects:
        - vectors: List with a single vector [1, 2, 3]
        - scalars: List with two scalars [2, 3]
        - Expected outcome: ValueError should be raised
    """
    vectors = [[1, 2, 3]]
    scalars = [2, 3]
    try:
        Vector.linear_combination(vectors, scalars)
        assert False  # Should not reach this
    except ValueError:
        assert True

def test_linear_combination_different_vector_lengths():
    vectors = [[1, 2], [1, 2, 3]]
    scalars = [1, 1]
    try:
        Vector.linear_combination(vectors, scalars)
        assert False  # Should not reach this
    except ValueError:
        assert True
