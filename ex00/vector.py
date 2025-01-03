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

            from typing import List

