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

def test_dot_zero():
    print_test_header(
        "test_dot_zero",
        "Dot product with a zero vector should return 0.0.\n"
        "u = [0.0, 0.0], v = [1.0, 1.0], expecting 0.0"
    )
    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])
    assert u.dot(v) == 0.0

def test_dot_identity():
    print_test_header(
        "test_dot_identity",
        "Dot product of two vectors [1.0, 1.0] should be 2.0.\n"
        "u = [1.0, 1.0], v = [1.0, 1.0], expecting 2.0"
    )
    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    assert u.dot(v) == 2.0

def test_dot_negative():
    print_test_header(
        "test_dot_negative",
        "Dot product of [-1.0, 6.0] and [3.0, 2.0] should be (-1*3) + (6*2) = 9.0."
    )
    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    assert u.dot(v) == 9.0

def test_dot_mismatched_sizes():
    print_test_header(
        "test_dot_mismatched_sizes",
        "Attempting to compute the dot product of vectors with different sizes\n"
        "should raise a ValueError.\n"
        "u = [1.0, 2.0], v = [1.0, 2.0, 3.0]"
    )
    u = Vector([1.0, 2.0])
    v = Vector([1.0, 2.0, 3.0])
    with pytest.raises(ValueError):
        u.dot(v)
