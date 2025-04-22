#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ex08/main.py
from matrix.matrix import *


def main():
    print("=== Exercise 08: Trace Examples ===\n")

    # Example 1: 2x2 identity
    u = Matrix.from_list([
        [1.0, 0.0],
        [0.0, 1.0]
    ])
    print("Trace of\n", u, "\nis", u.trace(), "\n")  # Expected 2.0

    # Example 2: 3x3 with positive trace
    u = Matrix.from_list([
        [2.0, -5.0,  0.0],
        [4.0,  3.0,  7.0],
        [-2.0, 3.0,  4.0]
    ])
    print("Trace of\n", u, "\nis", u.trace(), "\n")  # Expected 9.0

    # Example 3: 3x3 with negative trace
    u = Matrix.from_list([
        [-2.0, -8.0, 4.0],
        [ 1.0,-23.0, 4.0],
        [ 0.0,  6.0, 4.0]
    ])
    print("Trace of\n", u, "\nis", u.trace())       # Expected -21.0

if __name__ == "__main__":
    main()
