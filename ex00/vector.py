class Vector:
    def __init__(self, data):
        # Initialize the vector with the given list of numbers
        self.data = data

    def _validate_same_size(self, other):
        # Ensure both vectors have the same size
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
