import pytest
from .vector import Vector
from .matrix import Matrix

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

def test_vector_lerp():
    print_test_header(
        "test_vector_lerp",
        "Test linear interpolation for two 2D vectors.\n"
        "Expects a result that is blended between v1 and v2 by t=0.3."
    )
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])
    result = Vector.lerp(v1, v2, 0.3)
    expected = [2.6, 1.3]
    assert result.data == expected

def test_vector_lerp_invalid_t():
    print_test_header(
        "test_vector_lerp_invalid_t",
        "Test linear interpolation for invalid t < 0 or t > 1.\n"
        "Expects ValueError to be raised."
    )
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])
    with pytest.raises(ValueError):
        Vector.lerp(v1, v2, -0.1)
    with pytest.raises(ValueError):
        Vector.lerp(v1, v2, 1.1)

def test_vector_lerp_mismatched_size():
    print_test_header(
        "test_vector_lerp_mismatched_size",
        "Test linear interpolation for vectors of different sizes.\n"
        "Expects ValueError to be raised."
    )
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0])
    with pytest.raises(ValueError):
        Vector.lerp(v1, v2, 0.5)

def test_matrix_lerp():
    print_test_header(
        "test_matrix_lerp",
        "Test linear interpolation for two 2x2 matrices.\n"
        "Checks element-wise blending between m1 and m2 with t=0.5."
    )
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    result = Matrix.lerp(m1, m2, 0.5)
    expected = [[11.0, 5.5], [16.5, 22.0]]
    assert result.data == expected

def test_matrix_lerp_invalid_t():
    print_test_header(
        "test_matrix_lerp_invalid_t",
        "Test linear interpolation for a matrix with invalid t < 0 or t > 1.\n"
        "Expects ValueError to be raised."
    )
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0], [30.0, 40.0]])
    with pytest.raises(ValueError):
        Matrix.lerp(m1, m2, -0.2)
    with pytest.raises(ValueError):
        Matrix.lerp(m1, m2, 1.2)

def test_matrix_lerp_mismatched_size():
    print_test_header(
        "test_matrix_lerp_mismatched_size",
        "Test linear interpolation for matrices of different dimensions.\n"
        "Expects ValueError to be raised."
    )
    m1 = Matrix([[2.0, 1.0], [3.0, 4.0]])
    m2 = Matrix([[20.0, 10.0, 5.0], [30.0, 40.0, 15.0]])
    with pytest.raises(ValueError):
        Matrix.lerp(m1, m2, 0.5)
