class Matrix:
    """ 
        A class representing a matrix with basic operations.
        The Matrix class provides operations for handling matrices represented as lists of lists,
        including addition, subtraction, and scalar multiplication. All operations modify the matrix
        in-place.
        Attributes:
            data (list of lists): A two-dimensional array representing the matrix elements.
                Each inner list represents a row in the matrix.
    """

    # ──────────────────────────────────────────────────────────────────────
    
    #  Constructor
    def __init__(self, data):
        # Initialize the matrix with the given list of lists of numbers
        self.data = data


    # ──────────────────────────────────────────────────────────────────────
    def _validate_same_size(self, other):
        """
        Validate that two matrices have the same dimensions.

        This method checks if the current matrix and another matrix have the same
        dimensions and are both non-empty.

        Parameters:
        ----------
        other : Matrix
            Another matrix object to compare dimensions with.

        Raises:
        ------
        ValueError
            If either matrix is empty or if the matrices have different dimensions.

        Returns:
        -------
        None
        """
        # Ensure both matrices have the same dimensions and are not empty
        if not self.data or not other.data or not self.data[0] or not other.data[0]:
            raise ValueError("Matrices cannot be empty")
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions")

    # ──────────────────────────────────────────────────────────────────────
    def add(self, other):
        """
        Adds another matrix to this matrix in-place.
        
        Performs element-wise addition of the elements of 'other' to the
        corresponding elements of this matrix, modifying this matrix.
        
        Parameters:
            other: A matrix object with the same dimensions as this matrix.
        
        Raises:
            ValueError: If the dimensions of the matrices don't match.
            
        Returns:
            None: This operation modifies the matrix in-place.
        """
        self._validate_same_size(other)
        # Add the corresponding elements of the two matrices
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] += other.data[i][j]
    
    # ──────────────────────────────────────────────────────────────────────
    def sub(self, other):
        """
        Subtract another matrix from this matrix in-place.

        This method performs element-wise subtraction of matrices,
        modifying the current matrix instance.

        Parameters
        ----------
        other : Matrix
            The matrix to subtract from this matrix.

        Returns
        -------
        None
            The operation is performed in-place.

        Raises
        ------
        ValueError
            If the matrices do not have the same dimensions.

        Examples
        --------
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[0, 1], [2, 1]])
        >>> m1.sub(m2)
        >>> m1.data
        [[1, 1], [1, 3]]
        """
        self._validate_same_size(other)
        # Subtract corresponding elements of the two matrices
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] -= other.data[i][j]

    # ──────────────────────────────────────────────────────────────────────
    def scl(self, scalar):
        """
        Multiply each element of the matrix by a scalar value.

        This method performs scalar multiplication on the matrix by multiplying
        each element with the provided scalar value. The operation modifies the
        matrix in-place.

        Args:
            scalar: A number (int or float) to multiply with each element of the matrix.

        Returns:
            None: The matrix is modified in-place.

        Raises:
            ValueError: If the matrix is not properly formatted (checked by _validate_same_size).
        """
        # Multiply each element of the matrix by the scalar
        self._validate_same_size(self)
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.data[i][j] *= scalar
