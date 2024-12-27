from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    # Example usage of Vector class
    print("\033[94mStarting Vector operations demonstration...\033[0m")  # Blue

    # Initialize two Objects Vector
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    print(f"\033[92mInitialized vectors:\nu = {u.data}\nv = {v.data}\033[0m")  # Green

    # Add two vectors
    print("\n\033[93mAdding vectors u + v:\033[0m")  # Yellow
    u.add(v)
    print(f"\033[96mResult: {u.data}\033[0m")  # Cyan

    # Reset vector u and subtract vectors
    print("\n\033[93mSubtracting vectors u - v:\033[0m")  # Yellow
    u = Vector([2.0, 3.0])
    print(f"\033[95mReset u to: {u.data}\033[0m")  # Magenta
    u.sub(v)
    print(f"\033[96mResult: {u.data}\033[0m")  # Cyan

    # Scale Vector u by 2
    print("\n\033[93mScaling vector u by 2:\033[0m")  # Yellow
    u = Vector([2.0, 3.0])
    print(f"\033[95mReset u to: {u.data}\033[0m")  # Magenta
    u.scl(2)
    print(f"\033[96mResult: {u.data}\033[0m")  # Cyan

if __name__ == "__main__":
    main()
