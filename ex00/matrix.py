class Matrix:
    """
    A class used to represent a 2D matrix of numbers.
    Attributes:
        data (list[list[numeric]]): A 2-dimensional list representing the matrix.
    """
    def __init__(self, data):
        # Initialize the matrix with the given list of lists of numbers
        self.data = data

    def _validate_same_size(self, other):
        # Ensure both matrices have the same dimensions
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions")

    def add(self, other):
        self._validate_same_size(other)
        # Add the corresponding elements of the two matrices
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] += other.data[i][j]
    
    def sub(self, other):
        self._validate_same_size(other)
        # Subtract corresponding elements of the two matrices
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] -= other.data[i][j]

    def scl(self, scalar):
        # Multiply each element of the matrix by the scalar
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] *= scalar
