import pytest

from vector.vector import Vector

# ANSI color codes for readability (borrowed from ex00)
class ANSI:
    RESET = "\033[0m"
    BOLD  = "\033[1m"
    YELLOW= "\033[93m"
    CYAN  = "\033[96m"

def print_test_header(test_name, description):
    print(f"\n{ANSI.BOLD}{ANSI.YELLOW}=== {test_name} ==={ANSI.RESET}")
    print(f"{ANSI.CYAN}{description}{ANSI.RESET}")
    print(f"{'-' * 40}")

def test_cross_product_basis():
    print_test_header(
        "test_cross_product_basis",
        "e_x × e_y = e_z"
    )
    u = Vector([1.0, 0.0, 0.0])
    v = Vector([0.0, 1.0, 0.0])
    w = u.cross(v)
    assert w.data == [0.0, 0.0, 1.0]

def test_cross_product_example():
    print_test_header(
        "test_cross_product_example",
        "u=[1,2,3], v=[4,5,6] => u×v = [−3,6,−3]"
    )
    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    w = u.cross(v)
    assert w.data == [-3.0, 6.0, -3.0]

def test_cross_product_another():
    print_test_header(
        "test_cross_product_another",
        "u=[4,2,−3], v=[−2,−5,16] => u×v = [17,−58,−16]"
    )
    u = Vector([4.0, 2.0, -3.0])
    v = Vector([-2.0, -5.0, 16.0])
    w = u.cross(v)
    assert w.data == [17.0, -58.0, -16.0]

def test_invalid_dimension():
    print_test_header(
        "test_invalid_dimension",
        "vectors of length ≠3 should error"
    )
    with pytest.raises(ValueError):
        Vector([1.0, 2.0]).cross(Vector([1.0, 2.0, 3.0]))
