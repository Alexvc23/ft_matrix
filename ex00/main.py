from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    # Example usage of Vector class
    print("Starting Vector operations demonstration...")

    # Initialize two Objects Vector
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    print(f"Initialized vectors:\nu = {u.data}\nv = {v.data}")

    # Add two vectors
    print("\nAdding vectors u + v:")
    u.add(v)
    print(f"Result: {u.data}") # [7.0, 10.0]

    # Reset vector u and subtract vectors
    print("\nSubtracting vectors u - v:")
    u = Vector([2.0, 3.0])
    print(f"Reset u to: {u.data}")
    u.sub(v)
    print(f"Result: {u.data}") # [-3.0, -4.0]

    # Scale Vector u by 2
    print("\nScaling vector u by 2:")
    u = Vector([2.0, 3.0])
    print(f"Reset u to: {u.data}")
    u.scl(2)
    print(f"Result: {u.data}") # [4.0, 6.0]

if __name__ == "__main__":
    main()
