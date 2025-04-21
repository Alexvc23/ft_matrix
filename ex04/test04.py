import pytest

from vector.vector import Vector

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

def test_norm_zero():
    print_test_header(
        "test_norm_zero",
        "Check 1-norm, 2-norm, and infinity norm for a zero vector."
    )
    v = Vector.from_list([0.0, 0.0, 0.0])

    # 1-norm should be 0.0
    assert v.norm_1() == pytest.approx(0.0)
    # 2-norm should be 0.0
    assert v.norm() == pytest.approx(0.0)
    # infinity norm should be 0.0
    assert v.norm_inf() == pytest.approx(0.0)

def test_norm_positive():
    print_test_header(
        "test_norm_positive",
        "Check 1-norm, 2-norm, and infinity norm for [1.0, 2.0, 3.0]."
    )
    v = Vector.from_list([1.0, 2.0, 3.0])

    # 1-norm = 1 + 2 + 3 = 6.0
    assert v.norm_1() == pytest.approx(6.0)
    # 2-norm = sqrt(1+4+9) ≈ 3.74165738
    assert v.norm() == pytest.approx(3.74165738)
    # Infinity norm = max(|1|,|2|,|3|) = 3.0
    assert v.norm_inf() == pytest.approx(3.0)

def test_norm_negative():
    print_test_header(
        "test_norm_negative",
        "Check 1-norm, 2-norm, and infinity norm for [-1.0, -2.0]."
    )
    v = Vector.from_list([-1.0, -2.0])

    # 1-norm = |−1| + |−2| = 3.0
    assert v.norm_1() == pytest.approx(3.0)
    # 2-norm = sqrt(1 + 4) = sqrt(5) ≈ 2.236067977
    assert v.norm() == pytest.approx(2.236067977)
    # Infinity norm = max(|−1|,|−2|) = 2.0
    assert v.norm_inf() == pytest.approx(2.0)
