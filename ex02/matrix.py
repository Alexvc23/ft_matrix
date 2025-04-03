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