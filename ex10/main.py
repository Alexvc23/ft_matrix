#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from matrix.matrix import Matrix

def main():
    print("=== Exercise 10: Row‐Echelon Form ===\n")

    examples = [
        (
            [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]],
            "3×3 identity"
        ),
        (
            [[1.0,2.0],[3.0,4.0]],
            "2×2 simple"
        ),
        (
            [[1.0,2.0],[2.0,4.0]],
            "2×2 degenerate"
        ),
        (
            [
                [8.0, 5.0, -2.0, 4.0, 28.0],
                [4.0, 2.5, 20.0, 4.0, -4.0],
                [8.0, 5.0,  1.0, 4.0, 17.0]
            ],
            "3×5 full example"
        )
    ]

    for data, name in examples:
        print(f"Example: {name}")
        m = Matrix.from_list(data)
        print("Original:")
        print(m)
        print("Row‐echelon form:")
        print(m.row_echelon())
        print()

if __name__ == "__main__":
    main()
