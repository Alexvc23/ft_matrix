class Matrix:
    """
    A class used to represent a 2D matrix of numbers.
    Attributes:
        data (list[list[numeric]]): A 2-dimensional list representing the matrix.
    Methods:
        __init__(data):
            Initializes the matrix with the given 2D list of numbers.
        add(other):
            Adds the corresponding elements of another matrix to this matrix 
            (in-place), assuming both have the same dimensions.
        sub(other):
            Subtracts the corresponding elements of another matrix from this matrix 
            (in-place), assuming both have the same dimensions.
    """
    def __init__(self, data):
        # Initialize the matrix with the given list of lists of numbers
        self.data = data

        def add(self, other):
            # Ensure both matrices have the same size
            assert len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]), "Matrices must have the same number of rows"
            # Add the corresponding elements of the two matrices
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    self.data[i][j] += other.data[i][j]
    
        def sub(self, other):
            # Ensure both matrices have the same size
            assert len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]), "Matrices must have the same number of rows"
            # Subtract corresponding elements of the two matrices
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    self.data[i][j] -= other.data[i][j]



