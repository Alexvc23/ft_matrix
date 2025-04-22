import pytest

from vector.vector import Vector
from matrix.matrix import Matrix

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

# Vector tests
def test_vector_addition():
    print_test_header(
        "test_vector_addition",
        "Checking addition of two 2D vectors:" +
        "\nVector u = [2.0, 3.0]" +
        "\nVector v = [5.0, 7.0]" +
        "\nExpecting result = [7.0, 10.0]"
    )
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.add(v)
    assert u.data == [7.0, 10.0]


def test_vector_addition_mismatched_dimensions():
    print_test_header(
        "test_vector_addition_mismatched_dimensions",
        "Checking addition with mismatched dimensions:" +
        "\nVector u = [2.0, 3.0]" +
        "\nVector v = [5.0, 7.0, 1.0]" +
        "\nExpecting ValueError"
    )
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0, 1.0])
    with pytest.raises(ValueError):
        u.add(v)


def test_vector_subtraction():
    print_test_header(
        "test_vector_subtraction",
        "Checking subtraction of two 2D vectors:" +
        "\nVector u = [2.0, 3.0]" +
        "\nVector v = [5.0, 7.0]" +
        "\nExpecting result = [-3.0, -4.0]"
    )
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.sub(v)
    assert u.data == [-3.0, -4.0]


def test_vector_subtraction_mismatched_dimensions():
    print_test_header(
        "test_vector_subtraction_mismatched_dimensions",
        "Checking subtraction with mismatched dimensions:" +
        "\nVector u = [2.0, 3.0]" +
        "\nVector v = [5.0, 7.0, 1.0]" +
        "\nExpecting ValueError"
    )
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0, 1.0])
    with pytest.raises(ValueError):
        u.sub(v)


def test_vector_scaling():
    print_test_header(
        "test_vector_scaling",
        "Checking scalar multiplication of a 2D vector by 2:" +
        "\nVector u = [2.0, 3.0]" +
        "\nMultiplying by 2" +
        "\nExpecting result = [4.0, 6.0]"
    )
    u = Vector([2.0, 3.0])
    u.scl(2)
    assert u.data == [4.0, 6.0]


def test_vector_empty():
    print_test_header(
        "test_vector_empty",
        "Checking operations on empty vectors:" +
        "\nVector u = []" +
        "\nVector v = []" +
        "\nExpecting ValueError"
    )
    u = Vector([])
    v = Vector([])
    with pytest.raises(ValueError):
        u.sub(v)

# Matrix tests
def test_matrix_addition():
    print_test_header(
        "test_matrix_addition",
        "Checking addition of 2x2 matrices:" +
        "\nMatrix A = [[1.0, 2.0],[3.0, 4.0]]" +
        "\nMatrix B = [[5.0, 6.0],[7.0, 8.0]]" +
        "\nExpecting result = [[6.0, 8.0],[10.0, 12.0]]"
    )
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    A.add(B)
    assert A.data == [[6.0, 8.0], [10.0, 12.0]]


def test_matrix_addition_mismatched_dimensions():
    print_test_header(
        "test_matrix_addition_mismatched_dimensions",
        "Checking addition with mismatched dimensions:" +
        "\nMatrix A = [[1.0, 2.0],[3.0, 4.0]]" +
        "\nMatrix B = [[5.0, 6.0, 1.0],[7.0, 8.0, 1.0]]" +
        "\nExpecting ValueError"
    )
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0, 1.0], [7.0, 8.0, 1.0]])
    with pytest.raises(ValueError):
        A.add(B)


def test_matrix_subtraction():
    print_test_header(
        "test_matrix_subtraction",
        "Checking subtraction of 2x2 matrices:" +
        "\nMatrix A = [[1.0, 2.0],[3.0, 4.0]]" +
        "\nMatrix B = [[5.0, 6.0],[7.0, 8.0]]" +
        "\nExpecting result = [[-4.0, -4.0], [-4.0, -4.0]]"
    )
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0], [7.0, 8.0]])
    A.sub(B)
    assert A.data == [[-4.0, -4.0], [-4.0, -4.0]]


def test_matrix_subtraction_mismatched_dimensions():
    print_test_header(
        "test_matrix_subtraction_mismatched_dimensions",
        "Checking subtraction with mismatched dimensions:" +
        "\nMatrix A = [[1.0, 2.0],[3.0, 4.0]]" +
        "\nMatrix B = [[5.0, 6.0, 1.0],[7.0, 8.0, 1.0]]" +
        "\nExpecting ValueError"
    )
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    B = Matrix([[5.0, 6.0, 1.0], [7.0, 8.0, 1.0]])
    with pytest.raises(ValueError):
        A.sub(B)


def test_matrix_scaling():
    print_test_header(
        "test_matrix_scaling",
        "Checking scalar multiplication of a 2x2 matrix by 2:" +
        "\nMatrix A = [[1.0, 2.0],[3.0, 4.0]]" +
        "\nMultiplying by 2" +
        "\nExpecting result = [[2.0, 4.0], [6.0, 8.0]]"
    )
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    A.scl(2)
    assert A.data == [[2.0, 4.0], [6.0, 8.0]]


def test_matrix_empty():
    print_test_header(
        "test_matrix_empty",
        "Checking operations on empty matrices:" +
        "\nMatrix A = []" +
        "\nMatrix B = []" +
        "\nExpecting ValueError"
    )
    with pytest.raises(ValueError, match="Matrix cannot be empty or contain empty rows"):
        A = Matrix([])
    # If the Matrix class allowed empty matrices, the following would test addition:
    # A = Matrix([])  # Assuming this was allowed
    # B = Matrix([])  # Assuming this was allowed
    # with pytest.raises(ValueError):
    #     A.add(B)
