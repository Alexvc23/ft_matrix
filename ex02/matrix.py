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
    # staticmethod decorator is used to define a method that does not operate on an instance of the class.
    # e.g Matrix.lerp(u, v, t) where u and v are not instances of the Matrix class.
    @staticmethod
    def lerp(u, v, t: float):
        """ 
        Performs linear interpolation between matrices u and v with factor t.
        
        Linear interpolation calculates a matrix that is a weighted average between
        two matrices, where the weight is determined by the factor t.
        
        Parameters:
        -----------
        u : Matrix
            The first matrix (starting point of interpolation).
        v : Matrix
            The second matrix (ending point of interpolation).
        t : float
            The interpolation factor in the range [0.0, 1.0].
            When t=0, the result equals u.
            When t=1, the result equals v.
        
        Returns:
        --------
        Matrix
            A new matrix with values interpolated between u and v.
        
        Raises:
        -------
        ValueError
            If the interpolation factor t is not between 0 and 1.
            If the matrices u and v are not the same size.
        
        Examples:
        ---------
        >>> m1 = Matrix([[0, 0], [0, 0]])
        >>> m2 = Matrix([[1, 1], [1, 1]])
        >>> lerp(m1, m2, 0.5)
        Matrix([[0.5, 0.5], [0.5, 0.5]])
        """
        if not (0.0 <= t <= 1.0):
            raise ValueError("Interpolation factor t must be between 0 and 1")

        u._validate_same_size(v)

        result = []
        for i in range(len(u.data)):
            row = []
            for j in range(len(u.data[0])):
                a = u.data[i][j]
                b = v.data[i][j]
                interpolated = a + (b - a) * t
                row.append(interpolated)
            result.append(row)

        return Matrix(result)
