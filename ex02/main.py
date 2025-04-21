from vector.vector import Vector
from matrix.matrix import Matrix

# ──────────────────────────────────────────────────────────────────────────────

def lerp(u, v, t):
    """
    Generic linear interpolation function.

    For numbers:
        returns u + (v - u) * t
    For Vector and Matrix types:
        calls the corresponding static lerp method.
    
    Args:
        u: A number, Vector, or Matrix.
        v: A number, Vector, or Matrix.
        t (float): Interpolation factor (0 ≤ t ≤ 1).

    Returns:
        The interpolated result of the same type as u and v.

    Raises:
        TypeError: If u and v are of incompatible types.
    """
    if isinstance(u, (int, float)) and isinstance(v, (int, float)):
        return u + (v - u) * t
    elif isinstance(u, Vector) and isinstance(v, Vector):
        return Vector.lerp(u, v, t)
    elif isinstance(u, Matrix) and isinstance(v, Matrix):
        return Matrix.lerp(u, v, t)
    else:
        raise TypeError("Unsupported types for lerp")

# ──────────────────────────────────────────────────────────────────────────────

def main():

    print("Generic lerp function examples:\n")
    
    # Numbers
    print("lerp(0., 1., 0.) =", lerp(0., 1., 0.))     # Expected: 0.0
    print("lerp(0., 1., 1.) =", lerp(0., 1., 1.))     # Expected: 1.0
    print("lerp(0., 1., 0.5) =", lerp(0., 1., 0.5))    # Expected: 0.5
    print("lerp(21., 42., 0.3) =", lerp(21., 42., 0.3))# Expected: 27.3
    print()
    
    # Vectors
    v1 = Vector.from_list([2., 1.])
    v2 = Vector.from_list([4., 2.])
    result_vector = lerp(v1, v2, 0.3)
    print("lerp(Vector.from_list([2., 1.]), Vector.from_list([4., 2.]), 0.3) returns:")
    print(result_vector)  # Expected: [2.6, 1.3]
    print()
    
    # Matrices
    m1 = Matrix.from_list([[2., 1.], [3., 4.]])
    m2 = Matrix.from_list([[20., 10.], [30., 40.]])
    result_matrix = lerp(m1, m2, 0.5)
    print("lerp(Matrix.from_list([[2., 1.], [3., 4.]]), Matrix.from_list([[20., 10.], [30., 40.]]), 0.5) returns:")
    print(result_matrix)  # Expected: [[11.0, 5.5], [16.5, 22.0]]

if __name__ == '__main__':
    main()
