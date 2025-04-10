class Vector:
    """
    A class representing a mathematical vector with support for linear interpolation.
    """

    # ──────────────────────────────────────────────────────────────────────
    # Constructor
    def __init__(self, data):
        """
        Initialize the vector with a list of numbers.
        
        Args:
            data (list of float): The list representing the vector coordinates.
        """
        self.data = data

    # ──────────────────────────────────────────────────────────────────────`
    def _validate_same_size(self, other):
        """
        Validates that this vector and another vector have the same non-empty size.
        
        Args:
            other (Vector): The other vector to compare against.
        
        Raises:
            ValueError: If either vector is empty or if their sizes differ.
        """
        if not self.data or not other.data:
            raise ValueError("Vectors cannot be empty")
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same size")

    # ──────────────────────────────────────────────────────────────────────

    # this is used to define the string representation of the object.
    # e.g print(Vector([1, 2, 3])) will print the vector as: [1, 2, 3]
    # this is important for debugging and logging purposes.
    def __repr__(self):
        """
        Returns a string representation of the vector.
        """
        return "[" + ", ".join(str(x) for x in self.data) + "]"

    # ──────────────────────────────────────────────────────────────────────
    @classmethod
    def from_list(cls, data):
        """
        Create a Vector instance from a list of numbers.
        """
        return cls(data) 
    # ──────────────────────────────────────────────────────────────────────────────
    def dot(self, other):
        """
        Computes the dot product of this vector with another vector.

        The dot product is computed as:
            result = sum(self[i] * other[i] for i in range(n))
        
        Args:
            other (Vector): The vector with which to compute the dot product.

        Returns:
            float: The dot product of the two vectors.

        Raises:
            ValueError: If the two vectors have different sizes.

        Examples:
            >>> u = Vector([1.0, 1.0])
            >>> v = Vector([1.0, 1.0])
            >>> print(u.dot(v))
            2.0
        """
        self._validate_same_size(other)
        result = 0.0
        # zip pairs the elements of self.data and other.data together
        # e.g if self.data = [1, 2] and other.data = [3, 4], 
        # then zip(self.data, other.data) = [(1, 3), (2, 4)]
        for a, b in zip(self.data, other.data):
            result += a * b  # Here, one could use a fused multiply-add if available.
        return result