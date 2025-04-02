from typing import List

class Vector:
    """
    A class to represent a mathematical vector and perform basic vector operations.

    Attributes:
        data (list): A list of numbers representing the vector.

    """
    # Constructor
    def __init__(self, data):
        # Initialize the vector with the given list of numbers
        self.data = data
    # ──────────────────────────────────────────────────────────────────────
    def _validate_same_size(self, other):
        """
        Validates that two vectors have the same non-zero size.

        This method checks that neither vector is empty and both have the same dimensions.
        It's typically used before performing operations that require vectors of matching sizes.

        Args:
            other: Another vector object to compare with the current instance.
            
        Raises:
            ValueError: If either vector is empty or if the vectors have different sizes.
        """
        # Ensure both vectors have the same size
        if not self.data or not other.data or not self.data[0] or not other.data[0]:
            raise ValueError("Matrices cannot be empty")
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same size")

    # ──────────────────────────────────────────────────────────────────────
    def add(self, other):
        """
        Add another vector to this vector in-place.

        This method performs element-wise addition with another vector and modifies the current vector.

        Args:
            other (Vector): The vector to add to this vector. Must have the same dimensions.

        Raises:
            ValueError: If the vectors have different dimensions.

        Example:
            >>> v1 = Vector([1, 2, 3])
            >>> v2 = Vector([4, 5, 6])
            >>> v1.add(v2)
            >>> v1.data
            [5, 7, 9]
        """
        # Validate sizes before addition
        self._validate_same_size(other)
        # Add the corresponding elements of the two vectors
        for i in range(len(self.data)):
            self.data[i] += other.data[i]

    # ──────────────────────────────────────────────────────────────────────
    def sub(self, other):
        """
        Subtracts another vector from the current vector in-place.

        This method performs element-wise subtraction of the elements of 'other'
        from the corresponding elements of this vector, modifying the current vector.

        Parameters:
        ----------
        other : Vector
            The vector to subtract from this vector. Must have the same dimensions.

        Returns:
        -------
        None
            The method modifies the current vector in-place.

        Raises:
        ------
        ValueError
            If the vectors have different dimensions.
        """
        # Validate sizes before subtraction
        self._validate_same_size(other)
        # Subtract the corresponding elements of the two vectors
        for i in range(len(self.data)):
            self.data[i] -= other.data[i]

    # ──────────────────────────────────────────────────────────────────────
    def scl(self, scalar):
        """
        Multiply each element of the vector by a scalar.

        Args:
            scalar (int or float): The value by which to multiply each element of the vector.

        Returns:
            None: The vector is modified in-place.

        Example:
            >>> v = Vector([1, 2, 3])
            >>> v.scl(2)
            >>> v.data
            [2, 4, 6]
        """
        # Multiply each element of the vector by the scalar
        for i in range(len(self.data)):
            self.data[i] *= scalar

    # ──────────────────────────────────────────────────────────────────────
    def linear_combination(vectors: List[List[float]], scalars: List[float]) -> List[float]:
        """
        Computes the linear combination of vectors with their corresponding scalars.
        Linear combination is the sum of each vector multiplied by its scalar:
        result = a₁v₁ + a₂v₂ + ... + aₙvₙ
        where aᵢ are scalars and vᵢ are vectors.
        Args:
            vectors (List[List[float]]): A list of vectors where each vector is a list of floats
            scalars (List[float]): A list of scalars to multiply with each vector
        Returns:
            List[float]: The resulting vector from the linear combination
        Raises:
            ValueError: If the number of vectors doesn't match the number of scalars
                       or if vectors have different lengths
        """
        print(f"Input vectors: {vectors}")
        print(f"Input scalars: {scalars}")

        if not vectors or not scalars:
            raise ValueError("Vectors and scalars lists cannot be empty")

        if len(vectors) != len(scalars):
            print(f"Error: Vector count ({len(vectors)}) != Scalar count ({len(scalars)})")
            raise ValueError("The number of vectors must match the number of scalars.")

        # Check that all vectors have the same length
        expected_length = len(vectors[0])
        for i, vector in enumerate(vectors):
            if len(vector) != expected_length:
                raise ValueError(f"Vector at index {i} has different length ({len(vector)}) than expected ({expected_length})")

        # Initialize the result vector with zeros, same size as the first vector
        result = [0.0] * expected_length
        print(f"Initialized result vector: {result}")

        # Iterate through each vector and its corresponding scalar
        for vector, scalar in zip(vectors, scalars, strict=True):
            print(f"\nProcessing vector {vector} with scalar {scalar}")
            for i in range(len(vector)):
                old_value = result[i]
                result[i] += scalar * vector[i]
                print(f"Position {i}: {old_value} + ({scalar} * {vector[i]}) = {result[i]}")
    
        print(f"Final result: {result}")
        return result

    # ──────────────────────────────────────────────────────────────────────────────

    def lerp(u, v, t):
        """
        Linearly interpolates between values or sequences.
        Performs linear interpolation between two values or sequences based on the formula:
        result = u + (v - u) * t
        Parameters:
            u: Starting value (int, float) or sequence (list, tuple)
            v: Ending value (int, float) or sequence (list, tuple)
            t: Interpolation factor, typically between 0 and 1
               t=0 gives u, t=1 gives v, and intermediate values blend linearly
        Returns:
            The interpolated value or sequence (same type as input)
        Raises:
            ValueError: If u and v are sequences with different lengths
            TypeError: If u and v are unsupported types
        Examples:
            >>> lerp(0, 10, 0.5)
            5.0
            >>> lerp([0, 0], [10, 20], 0.5)
            [5.0, 10.0]
        """

        # If u and v are numbers (float/int), return the usual formula
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            return u + (v - u) * t
        
        # If u and v are lists/tuples, perform element-wise interpolation
        elif isinstance(u, (list, tuple)) and isinstance(v, (list, tuple)):
            # Ensure they have the same length
            if len(u) != len(v):
                raise ValueError("Cannot interpolate between sequences of different lengths.")
            
            # Recursively interpolate each element
            return type(u)(lerp(ui, vi, t) for ui, vi in zip(u, v))
        
        else:
            # Unsupported type
            raise TypeError(f"Unsupported type for lerp: {type(u)} and {type(v)}")