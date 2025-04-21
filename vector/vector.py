# Imports 
from typing import List
import math # import math module for mathematical operations

class Vector:
    """
    A class representing a mathematical vector with support for linear interpolation.
    """

    # ──────────────────────────────────────────────────────────────────────
    # Constructor
    def __init__(self, data: List[float]):
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
    # Dunder methods for basic operations and representation

    def __len__(self):
        """
        Return the number of elements in the vector.
        """
        return len(self.data)

    def __getitem__(self, idx):
        """
        Get the element at the specified index.
        """
        return self.data[idx]

    def __repr__(self):
        """
        Return the string representation of the vector.
        e.g print(Vector([1, 2, 3])) will print: Vector([1, 2, 3])
        """
        return f"Vector({self.data})"

    # ──────────────────────────────────────────────────────────────────────
    # class method are used to create instances of the class in different ways.
    # for example, from a list of numbers.
    # this is useful for creating vectors from different data sources.
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
            Vector([2.6, 1.3])
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
    # ──────────────────────────────────────────────────────────────────────
    def add(self, other):
        """
        Add another vector to this vector in-place.

        This method performs element-wise addition with another vector and modifies the current vector.

        Args:
            other (Vector): The vector to add to this vector. Must have the same dimensions.

        Raises:
            ValueError: If the vectors have different dimensions.

        Example:
            >>> v1 = Vector([1, 2, 3])
            >>> v2 = Vector([4, 5, 6])
            >>> v1.add(v2)
            >>> v1.data
            [5, 7, 9]
        """
        # Validate sizes before addition
        self._validate_same_size(other)
        # Add the corresponding elements of the two vectors
        for i in range(len(self.data)):
            self.data[i] += other.data[i]

    # ──────────────────────────────────────────────────────────────────────
    def sub(self, other):
        """
        Subtracts another vector from the current vector in-place.

        This method performs element-wise subtraction of the elements of 'other'
        from the corresponding elements of this vector, modifying the current vector.

        Parameters:
        ----------
        other : Vector
            The vector to subtract from this vector. Must have the same dimensions.

        Returns:
        -------
        None
            The method modifies the current vector in-place.

        Raises:
        ------
        ValueError
            If the vectors have different dimensions.
        """
        # Validate sizes before subtraction
        self._validate_same_size(other)
        # Subtract the corresponding elements of the two vectors
        for i in range(len(self.data)):
            self.data[i] -= other.data[i]

    # ──────────────────────────────────────────────────────────────────────
    def scl(self, scalar):
        """
        Multiply each element of the vector by a scalar.

        Args:
            scalar (int or float): The value by which to multiply each element of the vector.

        Returns:
            None: The vector is modified in-place.

        Example:
            >>> v = Vector([1, 2, 3])
            >>> v.scl(2)
            >>> v.data
            [2, 4, 6]
        """
        # Multiply each element of the vector by the scalar
        for i in range(len(self.data)):
            self.data[i] *= scalar

    # ──────────────────────────────────────────────────────────────────────
    @staticmethod
    def linear_combination(vectors: List['Vector'], scalars: List[float]) -> 'Vector':
        """
        Computes the linear combination of vectors with their corresponding scalars.
        Linear combination is the sum of each vector multiplied by its scalar:
        result = a₁v₁ + a₂v₂ + ... + aₙvₙ
        where aᵢ are scalars and vᵢ are vectors.
        Args:
            vectors (List[Vector]): A list of Vector objects.
            scalars (List[float]): A list of scalars to multiply with each vector.
        Returns:
            Vector: The resulting vector from the linear combination.
        Raises:
            ValueError: If the number of vectors doesn't match the number of scalars,
                       if vectors have different lengths, or if lists are empty.
        """

        if not vectors or not scalars:
            raise ValueError("Vectors and scalars lists cannot be empty")

        if len(vectors) != len(scalars):
            raise ValueError("The number of vectors must match the number of scalars.")

        # Check that all vectors have the same length
        expected_length = len(vectors[0])
        for i, vector in enumerate(vectors):
            if len(vector) != expected_length:
                raise ValueError(f"Vector at index {i} has different length ({len(vector)}) than expected ({expected_length})")

        # Initialize the result vector with zeros, same size as the first vector
        result_data = [0.0] * expected_length

        # Iterate through each vector and its corresponding scalar
        for vector, scalar in zip(vectors, scalars, strict=True):
            for i in range(len(vector)):
                result_data[i] += scalar * vector[i]
    
        return Vector(result_data)

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
    # ──────────────────────────────────────────────────────────────────────

    def cross(self, other: "Vector") -> "Vector":
        """
        Return the cross product of this vector with another 3D vector.
        """
        if len(self.data) != 3 or len(other.data) != 3:
            raise ValueError("Cross product requires 3-dimensional vectors")

        a1, a2, a3 = self.data
        b1, b2, b3 = other.data

        return Vector([
            a2 * b3 - a3 * b2,
            a3 * b1 - a1 * b3,
            a1 * b2 - a2 * b1,
        ])

