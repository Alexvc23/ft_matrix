#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ex07/main.py
from vector.vector import Vector
from matrix.matrix import Matrix

def main():

    print("\n--- Example 1: Matrix-Vector Multiplication ---")
    A = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v1 = Vector([1.0, 1.0])
    print(f"A = {A}")
    print(f"v1 = {v1}")
    print("A * v1 =", A.mul_vec(v1))

    print("\n--- Example 2: Matrix-Matrix Multiplication ---")
    B = Matrix([[2.0, 0.0], [0.0, 2.0]])
    print(f"B = {B}")
    print("A * B =", A.mul_mat(B))

    print("\n--- Example 3: Matrix-Vector Multiplication (different values) ---")
    C = Matrix([[1., 0.], [0., 1.]])
    v2 = Vector([4., 2.])
    print(f"C = {C}")
    print(f"v2 = {v2}")
    print("C * v2 =", C.mul_vec(v2)) # Should be [4., 2.]

    print("\n--- Example 4: Matrix-Matrix Multiplication (different values) ---")
    D = Matrix([[1., 2.], [3., 4.]]) # Same as A
    E = Matrix([[5., 6.], [7., 8.]])
    print(f"D = {D}")
    print(f"E = {E}")
    print("D * E =", D.mul_mat(E)) # Expected: [[19, 22], [43, 50]]

    print("\n--- Example 5: Matrix-Vector Multiplication (3x2 * 2x1) ---")
    F = Matrix([[1., 2.], [3., 4.], [5., 6.]])
    v3 = Vector([1., 2.])
    print(f"F = {F}")
    print(f"v3 = {v3}")
    print("F * v3 =", F.mul_vec(v3)) # Expected: [5., 11., 17.]

    print("\n--- Example 6: Matrix-Matrix Multiplication (3x2 * 2x2) ---")
    # F is 3x2, E is 2x2
    print(f"F = {F}")
    print(f"E = {E}")
    print("F * E =", F.mul_mat(E)) # Expected: [[19, 22], [43, 50], [67, 78]]

    print("\n----------------------------------------\n")


if __name__ == "__main__":
    main()