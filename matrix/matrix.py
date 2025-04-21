class Matrix:
    """
    A class representing a matrix, supporting basic interpolation.
    """

    # ──────────────────────────────────────────────────────────────────────
    # Constructor
    def __init__(self, data):
        """
        Initialize the matrix with a 2D list of floats.
        """
        self.data = data

    # ──────────────────────────────────────────────────────────────────────
    def _validate_same_size(self, other):
        """         
        This helper method checks if two matrices have the same number of rows
        and the same number of columns in each corresponding row.

        Args:
            other: Another matrix to compare dimensions with.
            
        Raises:
            ValueError: If matrices have different number of rows or if any 
                        corresponding rows have different number of columns.
        """
        if not self.data or not other.data or len(self.data) != len(other.data):
            raise ValueError("Matrices must have the same number of rows")
        for row_self, row_other in zip(self.data, other.data):
            if len(row_self) != len(row_other):
                raise ValueError("Matrices must have the same number of columns per row")

    # ──────────────────────────────────────────────────────────────────────
    # The __repr__ method is used to define the string representation of the object.
    # e.g print(Matrix([[1, 2], [3, 4]])) will print the matrix as:
    # 1 2
    # 3 4
    def __repr__(self):
        return '\n'.join(str(row) for row in self.data)
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
    # staticmethod decorator is used to define a method that does not operate on an instance of the class.
    # e.g Matrix.lerp(u, v, t) where u and v are not instances of the Matrix class.
    # ──────────────────────────────────────────────────────────────────────
    @staticmethod
    def lerp(u, v, t: float):
        """
        Linearly interpolates between two matrices u and v with factor t.

        Formula: result = u + (v - u) * t, applied element-wise.

        Args:
            u (Matrix): Starting matrix.
            v (Matrix): Ending matrix.
            t (float): Interpolation factor (0 ≤ t ≤ 1).

        Returns:
            Matrix: A new matrix with interpolated elements.

        Raises:
            ValueError: If t is not in [0,1] or if the matrices have mismatched dimensions.

        Examples:
            >>> m1 = Matrix.from_list([[2., 1.], [3., 4.]])
            >>> m2 = Matrix.from_list([[20., 10.], [30., 40.]])
            >>> print(Matrix.lerp(m1, m2, 0.5))
            [11.0, 5.5]
            [16.5, 22.0]
        """
        if not (0.0 <= t <= 1.0):
            raise ValueError("Interpolation factor t must be between 0 and 1")
        u._validate_same_size(v)
        new_data = []
        for row_u, row_v in zip(u.data, v.data):
            new_row = [a + (b - a) * t for a, b in zip(row_u, row_v)]
            new_data.append(new_row)
        return Matrix(new_data)

    # ──────────────────────────────────────────────────────────────────────
    @classmethod
    def from_list(cls, data):
        """
        Creates a Matrix from a two-dimensional list.

        Args:
            data (list of list of float): The matrix rows.

        Returns:
            Matrix: A new Matrix instance.
        """
        return cls(data)