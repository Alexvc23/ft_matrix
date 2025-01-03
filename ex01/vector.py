from typing import List

class Vector:
    """
    A class to represent a mathematical vector and perform basic vector operations.

    Attributes:
        data (list): A list of numbers representing the vector.

    Methods:
        __init__(data):
            Initializes the vector with the given list of numbers.
        _validate_same_size(other):
            Ensures both vectors have the same size.
        add(other):
            Adds the corresponding elements of the two vectors.
        sub(other):
            Subtracts the corresponding elements of the two vectors.
        scl(scalar):
            Multiplies each element of the vector by the scalar.
    """
    def __init__(self, data):
        # Initialize the vector with the given list of numbers
        self.data = data

    def _validate_same_size(self, other):
        # Ensure both vectors have the same size
        if not self.data or not other.data or not self.data[0] or not other.data[0]:
            raise ValueError("Matrices cannot be empty")
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same size")

    def add(self, other):
        # Validate sizes before addition
        self._validate_same_size(other)
        # Add the corresponding elements of the two vectors
        for i in range(len(self.data)):
            self.data[i] += other.data[i]

    def sub(self, other):
        # Validate sizes before subtraction
        self._validate_same_size(other)
        # Subtract the corresponding elements of the two vectors
        for i in range(len(self.data)):
            self.data[i] -= other.data[i]

    def scl(self, scalar):
        # Multiply each element of the vector by the scalar
        for i in range(len(self.data)):
            self.data[i] *= scalar

    # --------------------------------------------------------- exo01 ---------------------------------------------------------

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