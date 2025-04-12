# Imports 
import math # import math module for mathematical operations

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
    # class method are used to create instances of the class in different ways.
    # for example, from a list of numbers.
    # this is useful for creating vectors from different data sources.
    @classmethod
    def from_list(cls, data):
        """
        Create a Vector instance from a list of numbers.
        """
        return cls(data)
    # ──────────────────────────────────────────────────────────────────────
    def dot(self, other):
            """
            Compute the dot product of this vector with another vector.
            
            Args:
                other (Vector): The other vector.
            
            Returns:
                float: The dot product.
            """
            self._validate_same_size(other)
            result = 0.0
            for a, b in zip(self.data, other.data):
                result += a * b  # Here one could use a fused multiply–add if available.
            return result
    # ─────────────────────────────────────────────────────────────────────
    def norm_1(self) -> float:
        """
        Compute the 1-norm (Manhattan norm) of the vector.
        
        Returns:
            float: Sum of the absolute values of the coordinates.
            
        Example:
            For [1., 2., 3.], 1-norm = 6.0.
        """
        return sum(abs(x) for x in self.data)
    # ──────────────────────────────────────────────────────────────────────
    def norm(self) -> float:
            """
            Compute the 2-norm (Euclidean norm) of the vector.
            
            Returns:
                float: The square root of the sum of the squares of the coordinates.
                
            Example:
                For [1., 2., 3.], 2-norm ≈ 3.74165738.
            """
            return math.sqrt(sum(x * x for x in self.data))

    # ──────────────────────────────────────────────────────────────────────
    def norm_inf(self) -> float:
        """
        Compute the infinity norm (maximum norm) of the vector.
        
        Returns:
            float: The maximum absolute value among the coordinates.
            
        Example:
            For [1., 2., 3.], infinity norm = 3.0.
        """
        return max(abs(x) for x in self.data)
    # ─────────────────────────────────────────────────────────────────────
    # static methods are used when we want to define a method that does not depend on the instance of the class.
    @staticmethod
    def angle_cos(u, v):
        """
        Compute the cosine of the angle between two vectors u and v.
        
        The formula is:
        
            cos(θ) = (u · v) / (‖u‖ * ‖v‖)
        
        Behavior is undefined if one (or both) vectors is the zero vector.
        
        Args:
            u (Vector): The first vector.
            v (Vector): The second vector.
        
        Returns:
            float: The cosine of the angle between u and v.
        
        Raises:
            ValueError: If the vectors are of different sizes or if either has zero norm.
        
        Examples:
            >>> u = Vector.from_list([1., 0.])
            >>> v = Vector.from_list([1., 0.])
            >>> print(Vector.angle_cos(u, v))
            1.0
        """
        u._validate_same_size(v)
        norm_u = u.norm()
        norm_v = v.norm()
        if norm_u == 0 or norm_v == 0:
            raise ValueError("Cannot compute angle with zero vector")
        return u.dot(v) / (norm_u * norm_v)