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
    # staticmethod decorator is used to define a method that does not operate on an instance of the class.
    # e.g Vector.lerp(u, v, t) where u and v are not instances of the Vector class.
    @staticmethod
    def lerp(u, v, t: float):
        """
        Linearly interpolates between two vectors u and v with factor t.

        Formula: result = u + (v - u) * t

        Args:
            u (Vector): Starting vector.
            v (Vector): Ending vector.
            t (float): Interpolation factor (0 ≤ t ≤ 1).

        Returns:
            Vector: A new vector with interpolated coordinates.

        Raises:
            ValueError: If t is not in [0,1] or if the vectors are of mismatched size.

        Examples:
            >>> v1 = Vector.from_list([2., 1.])
            >>> v2 = Vector.from_list([4., 2.])
            >>> print(Vector.lerp(v1, v2, 0.3))
            [2.6, 1.3]
        """
        if not (0.0 <= t <= 1.0):
            raise ValueError("Interpolation factor t must be between 0 and 1")
        u._validate_same_size(v)
        new_data = [a + (b - a) * t for a, b in zip(u.data, v.data)]
        return Vector(new_data)

    # ──────────────────────────────────────────────────────────────────────
    @classmethod
    def from_list(cls, data):
        """
        Creates a Vector from a list of numbers.

        Args:
            data (list of float): The list of coordinates.

        Returns:
            Vector: A new Vector instance.
        """
        return cls(data)