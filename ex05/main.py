from vector.vector import Vector

def main():
    print("=== Exercise 05: Cosine of the Angle Between Vectors ===\n")
    
    # Example 1
    u = Vector.from_list([1.0, 0.0])
    v = Vector.from_list([1.0, 0.0])
    print("angle_cos(Vector.from_list([1., 0.]), Vector.from_list([1., 0.])) =", Vector.angle_cos(u, v))
    # Expected output: 1.0
    
    # Example 2
    u = Vector.from_list([1.0, 0.0])
    v = Vector.from_list([0.0, 1.0])
    print("angle_cos(Vector.from_list([1., 0.]), Vector.from_list([0., 1.])) =", Vector.angle_cos(u, v))
    # Expected output: 0.0
    
    # Example 3
    u = Vector.from_list([-1.0, 1.0])
    v = Vector.from_list([1.0, -1.0])
    print("angle_cos(Vector.from_list([-1., 1.]), Vector.from_list([1., -1.])) =", Vector.angle_cos(u, v))
    # Expected output: -1.0
    
    # Example 4
    u = Vector.from_list([2.0, 1.0])
    v = Vector.from_list([4.0, 2.0])
    print("angle_cos(Vector.from_list([2., 1.]), Vector.from_list([4., 2.])) =", Vector.angle_cos(u, v))
    # Expected output: 1.0
    
    # Example 5
    u = Vector.from_list([1.0, 2.0, 3.0])
    v = Vector.from_list([4.0, 5.0, 6.0])
    print("angle_cos(Vector.from_list([1., 2., 3.]), Vector.from_list([4., 5., 6.])) =", Vector.angle_cos(u, v))
    # Expected output: approximately 0.974631846

if __name__ == '__main__':
    main()
