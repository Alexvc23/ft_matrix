#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from matrix.matrix import Matrix


def main():
    print("=== Exercise 11: Determinant Examples ===\n")

    examples = [
        (
            [[1.0, -1.0], [-1.0, 1.0]],
            "2×2 zero-determinant"
        ),
        (
            [[2.0,0.0,0.0],[0.0,2.0,0.0],[0.0,0.0,2.0]],
            "3×3 scalar 2·I"
        ),
        (
            [[8.0,5.0,-2.0],[4.0,7.0,20.0],[7.0,6.0,1.0]],
            "3×3 general"
        ),
        (
            [
                [ 8.0,  5.0, -2.0,  4.0],
                [ 4.0,  2.5, 20.0,  4.0],
                [ 8.0,  5.0,  1.0,  4.0],
                [28.0, -4.0, 17.0,  1.0]
            ],
            "4×4 general"
        )
    ]

    for data, desc in examples:
        mat = Matrix.from_list(data)
        print(f"{desc}:")
        print(mat)
        print("det =", mat.determinant(), "\n")

if __name__ == "__main__":
    main()
