#!/usr/bin/env python3
from vector.vector import Vector

def main():
    print("Exercise 03 – Dot Product Examples\n")

    # Example 1: Dot product with a zero vector
    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])
    print("Example 1:")
    print("u =", u)
    print("v =", v)
    print("u · v =", u.dot(v))  # Expected output: 0.0
    print()

    # Example 2: Dot product of two identical vectors
    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    print("Example 2:")
    print("u =", u)
    print("v =", v)
    print("u · v =", u.dot(v))  # Expected output: 2.0
    print()

    # Example 3: Dot product with negative values
    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    print("Example 3:")
    print("u =", u)
    print("v =", v)
    print("u · v =", u.dot(v))  # Expected output: 9.0

if __name__ == '__main__':
    main()
