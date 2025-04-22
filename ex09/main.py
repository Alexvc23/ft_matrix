#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ex08/main.py
from matrix.matrix import *

def main():
    print("=== Exercise 09: Matrix Transpose ===\n")

    # 2×2 square
    A = Matrix.from_list([[1.0, 2.0], [3.0, 4.0]])
    print("Original (2×2):")
    print(A)
    print("Transposed:")
    print(A.transpose(), "\n")  # Expected [[1,3],[2,4]]

    # 2×3 (wider)
    B = Matrix.from_list([[1.0, 2.0, 3.0],
                          [4.0, 5.0, 6.0]])
    print("Original (2×3):")
    print(B)
    print("Transposed (3×2):")
    print(B.transpose(), "\n")  # Expected [[1,4],[2,5],[3,6]]

    # 3×2 (taller)
    C = Matrix.from_list([[7.0, 8.0],
                          [9.0, 10.0],
                          [11.0, 12.0]])
    print("Original (3×2):")
    print(C)
    print("Transposed (2×3):")
    print(C.transpose())

if __name__ == "__main__":
    main()
