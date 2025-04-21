#!/usr/bin/env python3
from vector.vector import Vector

def cross_product(u: Vector, v: Vector) -> Vector:
    return u.cross(v)

def main():
    examples = [
        ([0.0, 0.0, 1.0], [1.0, 0.0, 0.0]),
        ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]),
        ([4.0, 2.0, -3.0], [-2.0, -5.0, 16.0]),
    ]

    for a, b in examples:
        u = Vector(a)
        v = Vector(b)
        w = cross_product(u, v)
        print(f"{u} × {v} = {w}")

if __name__ == "__main__":
    main()
