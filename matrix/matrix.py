from copy import deepcopy
from vector.vector import Vector

class Matrix:
    """
    A class representing a matrix, supporting basic interpolation.
    """

    # ──────────────────────────────────────────────────────────────────────
    # Constructor
    def __init__(self, data):
        """
        Initialize the matrix with a two-dimensional list.

        Args:
            data (list of list of float): The rows of the matrix.
        """
        if not data or any(not row for row in data):
            raise ValueError("Matrix cannot be empty or contain empty rows")
        # ensure all rows have the same length
        row_len = len(data[0])
        for row in data:
            if len(row) != row_len:
                raise ValueError("All rows must have the same length")
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

    # ──────────────────────────────────────────────────────────────────────
    # Matrix Multiplication ex07
    def mul_vec(self, vec): # Assuming Vector behaves like a list or has __len__ and __getitem__
        """
        Multiplies the matrix by a vector.

        Args:
            vec: A Vector object (or list/tuple) whose length matches the number of columns in the matrix.

        Returns:
            # Vector: A new Vector object representing the result. 
            # Returning list as Vector class is not defined/imported.
            list: A new list representing the result vector components.

        Raises:
            ValueError: If the matrix is empty, vector is empty, or dimensions mismatch.
            TypeError: If vector does not support len() or indexing.
        """
        if not self.data or not self.data[0]:
                raise ValueError("Matrix cannot be empty for multiplication.")
        
        # Calculate dimensions on the fly
        rows = len(self.data)
        cols = len(self.data[0]) 
        
        try:
            vec_len = len(vec) 
        except TypeError:
                raise TypeError("Vector must support len()")

        if cols != vec_len:
            raise ValueError(f"Matrix columns ({cols}) must match vector size ({vec_len})")
        
        result_data = []
        for i in range(rows):
            acc = 0.0
            for j in range(cols):
                try:
                    # Assuming vec[j] works
                    acc += self.data[i][j] * vec[j] 
                except IndexError:
                        raise IndexError(f"Vector index {j} out of range for length {vec_len}")
                except TypeError:
                        raise TypeError("Vector elements must support multiplication with matrix elements.")
            result_data.append(acc)
        
        return Vector(result_data) 

    # ──────────────────────────────────────────────────────────────────────────────

    def mul_mat(self, other: "Matrix") -> "Matrix":
        """
        Multiplies this matrix by another matrix.

        Args:
            other: A Matrix object where the number of rows matches the number of columns in this matrix.

        Returns:
            Matrix: A new Matrix object representing the result of the multiplication.

        Raises:
            ValueError: If matrices are empty or dimensions mismatch for multiplication.
            TypeError: If 'other' is not a Matrix instance or data is invalid.
        """
        if not isinstance(other, Matrix):
                raise TypeError("Can only multiply by another Matrix instance.")
        if not self.data or not self.data[0] or not other.data or not other.data[0]:
                raise ValueError("Matrices cannot be empty for multiplication.")
                
        # Calculate dimensions on the fly
        self_rows = len(self.data)
        self_cols = len(self.data[0])
        other_rows = len(other.data)
        other_cols = len(other.data[0])

        # Validate dimensions of 'other' matrix as well
        for row in other.data:
            if len(row) != other_cols:
                    raise ValueError("Other matrix has inconsistent row lengths.")

        if self_cols != other_rows:
            raise ValueError(f"Matrix A's columns ({self_cols}) must match Matrix B's rows ({other_rows})")
        
        # Initialize result matrix with zeros
        result_data = [[0.0 for _ in range(other_cols)] for _ in range(self_rows)]
        
        for i in range(self_rows):
            for j in range(other_cols):
                acc = 0.0
                # Dot product of row i from self and column j from other
                for k in range(self_cols): # self_cols is same as other_rows
                    try:
                        acc += self.data[i][k] * other.data[k][j]
                    except TypeError:
                            raise TypeError("Matrix elements must support multiplication.")
                result_data[i][j] = acc
                
        return Matrix(result_data)

    # ──────────────────────────────────────────────────────────────────────────────
    def trace(self) -> float:
        """
        Compute and return the trace of the matrix, i.e. the sum of its diagonal elements.

        Returns:
            float: The sum of A[i][i] for i = 0..n-1.

        Raises:
            ValueError: If the matrix is empty or not square.
        """
        if not self.data or not self.data[0]:
            raise ValueError("Matrix cannot be empty")
        n = len(self.data)
        # validate square
        for row in self.data:
            if len(row) != n:
                raise ValueError("Trace undefined for non-square matrix")
        return sum(self.data[i][i] for i in range(n))

    # ──────────────────────────────────────────────────────────────────────────────
    def transpose(self):
        """
        Compute and return the transpose of the matrix.

        Returns:
            Matrix: A new Matrix instance containing the transpose.

        Time complexity: O(nm)
        Space complexity: O(nm)
        """
        # zip(*…) transposes, but we need to convert tuples back to lists
        # e.g zip([1, 2], [3, 4]) gives (1, 3), (2, 4)
        # and we need to convert them to lists
        # e.g [[1, 3], [2, 4]]
        transposed_data = [list(col) for col in zip(*self.data)]
        return Matrix(transposed_data)

    # ──────────────────────────────────────────────────────────────────────

    def row_echelon(self):
        """
        Compute and return the **reduced** row‐echelon form (RREF) of the matrix
        using Gauss‐Jordan elimination.

        Returns:
            Matrix: A new Matrix instance in reduced row‐echelon form.
        """
        A = deepcopy(self.data)
        m = len(A)
        n = len(A[0])
        pivot_row = 0

        for col in range(n):
            if pivot_row >= m:
                break
            # Find pivot in or below pivot_row
            pivot = None
            for r in range(pivot_row, m):
                if abs(A[r][col]) > 1e-12: # 1e-12 is equivalent to 10**-12
                    pivot = r
                    break
            if pivot is None:
                continue
            # Swap into position
            A[pivot_row], A[pivot] = A[pivot], A[pivot_row]
            # Normalize pivot row
            pv = A[pivot_row][col]
            A[pivot_row] = [x / pv for x in A[pivot_row]]
            # Eliminate all other rows
            for r in range(m):
                if r != pivot_row and abs(A[r][col]) > 1e-12:
                    factor = A[r][col]
                    A[r] = [a_r - factor * a_p for a_r, a_p in zip(A[r], A[pivot_row])]
            pivot_row += 1

        return Matrix(A)
