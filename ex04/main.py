from vector import Vector

def main():
    print("=== Exercise 04: Norm Examples ===\n")

    # Example 1: Zero vector
    v1 = Vector.from_list([0.0, 0.0, 0.0])
    print("For Vector:", v1)
    print("1-norm =", v1.norm_1())      # Expected output: 0.0
    print("2-norm =", v1.norm())        # Expected output: 0.0
    print("Infinity norm =", v1.norm_inf())  # Expected output: 0.0
    print()

    # Example 2: Positive vector
    v2 = Vector.from_list([1.0, 2.0, 3.0])
    print("For Vector:", v2)
    print("1-norm =", v2.norm_1())      # Expected output: 6.0
    print("2-norm =", v2.norm())        # Expected output: ~3.74165738
    print("Infinity norm =", v2.norm_inf())  # Expected output: 3.0
    print()

    # Example 3: Negative vector
    v3 = Vector.from_list([-1.0, -2.0])
    print("For Vector:", v3)
    print("1-norm =", v3.norm_1())      # Expected output: 3.0
    print("2-norm =", v3.norm())        # Expected output: ~2.236067977
    print("Infinity norm =", v3.norm_inf())  # Expected output: 2.0

if __name__ == '__main__':
    main()
