import pytest
from .vector import Vector

# ANSI color codes for convenience
class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

def print_test_header(test_name, description):
    """
    Prints a colored, formatted header before each test for readability.
    """
    print(f"\n{ANSI.BOLD}{ANSI.YELLOW}=== {test_name} ==={ANSI.RESET}")
    print(f"{ANSI.CYAN}{description}{ANSI.RESET}")
    print(f"{ANSI.BLUE}{'-' * 40}{ANSI.RESET}")


def test_linear_combination_basic():
    print_test_header(
        "test_linear_combination_basic",
        "Checking linear combination with basic inputs:" +
        "\nVectors = [[1, 2, 3], [4, 5, 6]]" +
        "\nScalars = [2, 1]" +
        "\nExpecting result = [6.0, 9.0, 12.0]"
    )
    vectors = [[1, 2, 3], [4, 5, 6]]
    scalars = [2, 1]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [6.0, 9.0, 12.0]


def test_linear_combination_zero_scalars():
    print_test_header(
        "test_linear_combination_zero_scalars",
        "Checking linear combination with zero scalars:" +
        "\nVectors = [[1, 2, 3], [4, 5, 6]]" +
        "\nScalars = [0, 0]" +
        "\nExpecting result = [0.0, 0.0, 0.0]"
    )
    vectors = [[1, 2, 3], [4, 5, 6]]
    scalars = [0, 0]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [0.0, 0.0, 0.0]


def test_linear_combination_single_vector():
    print_test_header(
        "test_linear_combination_single_vector",
        "Checking linear combination with a single vector:" +
        "\nVector = [[1, 2, 3]]" +
        "\nScalar = [2]" +
        "\nExpecting result = [2.0, 4.0, 6.0]"
    )
    vectors = [[1, 2, 3]]
    scalars = [2]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [2.0, 4.0, 6.0]


def test_linear_combination_negative_scalars():
    print_test_header(
        "test_linear_combination_negative_scalars",
        "Checking linear combination with negative scalars:" +
        "\nVectors = [[1, 2, 3], [4, 5, 6]]" +
        "\nScalars = [-1, -2]" +
        "\nExpecting result = [-9.0, -12.0, -15.0]"
    )
    vectors = [[1, 2, 3], [4, 5, 6]]
    scalars = [-1, -2]
    result = Vector.linear_combination(vectors, scalars)
    assert result == [-9.0, -12.0, -15.0]


def test_linear_combination_different_lengths():
    print_test_header(
        "test_linear_combination_different_lengths",
        "Test linear combination with vectors and scalars of different lengths:" +
        "\nVectors = [[1, 2, 3]]" +
        "\nScalars = [2, 3]" +
        "\nExpecting: ValueError"
    )
    vectors = [[1, 2, 3]]
    scalars = [2, 3]
    try:
        Vector.linear_combination(vectors, scalars)
        assert False  # Should not reach this
    except ValueError:
        assert True


def test_linear_combination_different_vector_lengths():
    print_test_header(
        "test_linear_combination_different_vector_lengths",
        "Checking linear combination with vectors of mismatched dimensions:" +
        "\nVectors = [[1, 2], [1, 2, 3]]" +
        "\nScalars = [1, 1]" +
        "\nExpecting: ValueError"
    )
    vectors = [[1, 2], [1, 2, 3]]
    scalars = [1, 1]
    try:
        Vector.linear_combination(vectors, scalars)
        assert False  # Should not reach this
    except ValueError:
        assert True
