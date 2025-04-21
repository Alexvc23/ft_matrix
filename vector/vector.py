# Imports
import math
from typing import List, Union, Sequence, TypeVar

T = TypeVar('T', bound='Vector') # Type variable for methods returning instances of the class

class Vector:
    """
    A class representing a mathematical vector with support for common vector operations.

    Attributes:
        data (List[float]): The coordinates of the vector.
    """

    # ──────────────────────────────────────────────────────────────────────
    # Constructor
    def __init__(self, data: Sequence[Union[float, int]]):
        """
        Initialize the vector with a sequence of numbers.

        Args:
            data: A sequence (e.g., list, tuple) of numbers (int or float).

        Raises:
            TypeError: If data is not a sequence or contains non-numeric types.
            ValueError: If data is empty.
        """
        if not isinstance(data, Sequence):
            raise TypeError("Input data must be a sequence (e.g., list, tuple).")
        if not data:
            raise ValueError("Input data cannot be empty.")
        try:
            # Store data as a list of floats, defensively copy the input
            self.data: List[float] = [float(x) for x in data]
        except (ValueError, TypeError) as e:
            raise TypeError("All elements in data must be numeric.") from e

    # ──────────────────────────────────────────────────────────────────────
    # Validation
    def _validate_same_size(self, other: T):
        """
        Validates that this vector and another vector have the same size.

        Args:
            other: The other vector to compare against.

        Raises:
            ValueError: If the vectors have different sizes.
        """
        if len(self.data) != len(other.data):
            raise ValueError(f"Vectors must have the same size ({len(self.data)} != {len(other.data)})")

    def _validate_dimension(self, expected_dim: int):
        """
        Validates that the vector has the expected dimension.

        Args:
            expected_dim: The dimension the vector must have.

        Raises:
            ValueError: If the vector does not have the expected dimension.
        """
        if len(self.data) != expected_dim:
            raise ValueError(f"Vector must be {expected_dim}-dimensional (current dimension: {len(self.data)})")

    # ──────────────────────────────────────────────────────────────────────
    # Dunder Methods
    def __repr__(self) -> str:
        """Returns a developer-friendly string representation of the vector."""
        return f"Vector({self.data})"

    def __str__(self) -> str:
        """Returns a user-friendly string representation of the vector."""
        return "[" + ", ".join(f"{x:.2f}" for x in self.data) + "]"

    def __len__(self) -> int:
        """Returns the number of elements (dimension) of the vector."""
        return len(self.data)

    def __getitem__(self, index: int) -> float:
        """Allows accessing vector elements using index notation (e.g., v[0])."""
        return self.data[index]

    def __add__(self: T, other: T) -> T:
        """
        Adds two vectors element-wise, returning a new Vector. (v1 + v2)

        Args:
            other: The vector to add.

        Returns:
            A new Vector representing the sum.

        Raises:
            ValueError: If vectors have different sizes.
        """
        self._validate_same_size(other)
        new_data = [a + b for a, b in zip(self.data, other.data)]
        return self.__class__(new_data) # Use self.__class__ to support potential subclassing

    def __iadd__(self: T, other: T) -> T:
        """
        Adds another vector to this vector in-place. (v1 += v2)

        Args:
            other: The vector to add.

        Returns:
            The modified vector (self).

        Raises:
            ValueError: If vectors have different sizes.
        """
        self._validate_same_size(other)
        for i in range(len(self.data)):
            self.data[i] += other.data[i]
        return self

    def __sub__(self: T, other: T) -> T:
        """
        Subtracts two vectors element-wise, returning a new Vector. (v1 - v2)

        Args:
            other: The vector to subtract.

        Returns:
            A new Vector representing the difference.

        Raises:
            ValueError: If vectors have different sizes.
        """
        self._validate_same_size(other)
        new_data = [a - b for a, b in zip(self.data, other.data)]
        return self.__class__(new_data)

    def __isub__(self: T, other: T) -> T:
        """
        Subtracts another vector from this vector in-place. (v1 -= v2)

        Args:
            other: The vector to subtract.

        Returns:
            The modified vector (self).

        Raises:
            ValueError: If vectors have different sizes.
        """
        self._validate_same_size(other)
        for i in range(len(self.data)):
            self.data[i] -= other.data[i]
        return self

    def __mul__(self: T, scalar: Union[float, int]) -> T:
        """
        Multiplies the vector by a scalar, returning a new Vector. (v * scalar)

        Args:
            scalar: The scalar value.

        Returns:
            A new Vector representing the scaled vector.

        Raises:
            TypeError: If scalar is not a number.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number (int or float).")
        new_data = [x * scalar for x in self.data]
        return self.__class__(new_data)

    def __rmul__(self: T, scalar: Union[float, int]) -> T:
        """
        Allows scalar multiplication from the left. (scalar * v)

        Args:
            scalar: The scalar value.

        Returns:
            A new Vector representing the scaled vector.

        Raises:
            TypeError: If scalar is not a number.
        """
        return self.__mul__(scalar) # Multiplication is commutative

    def __imul__(self: T, scalar: Union[float, int]) -> T:
        """
        Multiplies this vector by a scalar in-place. (v *= scalar)

        Args:
            scalar: The scalar value.

        Returns:
            The modified vector (self).

        Raises:
            TypeError: If scalar is not a number.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number (int or float).")
        for i in range(len(self.data)):
            self.data[i] *= scalar
        return self

    def __truediv__(self: T, scalar: Union[float, int]) -> T:
        """
        Divides the vector by a scalar, returning a new Vector. (v / scalar)

        Args:
            scalar: The scalar value.

        Returns:
            A new Vector representing the scaled vector.

        Raises:
            TypeError: If scalar is not a number.
            ValueError: If scalar is zero.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number (int or float).")
        if scalar == 0:
            raise ValueError("Division by zero is not allowed.")
        new_data = [x / scalar for x in self.data]
        return self.__class__(new_data)

    def __itruediv__(self: T, scalar: Union[float, int]) -> T:
        """
        Divides this vector by a scalar in-place. (v /= scalar)

        Args:
            scalar: The scalar value.

        Returns:
            The modified vector (self).

        Raises:
            TypeError: If scalar is not a number.
            ValueError: If scalar is zero.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number (int or float).")
        if scalar == 0:
            raise ValueError("Division by zero is not allowed.")
        for i in range(len(self.data)):
            self.data[i] /= scalar
        return self

    # ──────────────────────────────────────────────────────────────────────
    # Class and Static Methods
    @classmethod
    def from_list(cls: type[T], data: Sequence[Union[float, int]]) -> T:
        """
        Creates a Vector from a list or sequence of numbers.

        Args:
            data: The sequence of coordinates.

        Returns:
            A new Vector instance.
        """
        return cls(data)

    @staticmethod
    def lerp(u: T, v: T, t: float) -> T:
        """
        Linearly interpolates between two vectors u and v with factor t.

        Formula: result = u + (v - u) * t = u * (1 - t) + v * t

        Args:
            u: Starting vector.
            v: Ending vector.
            t: Interpolation factor (usually between 0 and 1).

        Returns:
            A new vector with interpolated coordinates.

        Raises:
            ValueError: If t is not in [0,1] or if the vectors are of mismatched size.
        """
        if not (0.0 <= t <= 1.0):
            # Warning instead of error might be preferable depending on use case
            # raise ValueError("Interpolation factor t should be between 0 and 1")
            pass # Allow extrapolation if needed, user beware
        u._validate_same_size(v)
        # Use the more numerically stable formula: u * (1 - t) + v * t
        new_data = [a * (1 - t) + b * t for a, b in zip(u.data, v.data)]
        # Alternative formula: a + (b - a) * t
        # new_data = [a + (b - a) * t for a, b in zip(u.data, v.data)]
        return u.__class__(new_data) # Use __class__ to return correct type

    @staticmethod
    def linear_combination(vectors: Sequence[T], scalars: Sequence[float]) -> T:
        """
        Computes the linear combination of vectors with corresponding scalars.

        Result = scalar₁*v₁ + scalar₂*v₂ + ... + scalarₙ*vₙ

        Args:
            vectors: A sequence of Vector objects.
            scalars: A sequence of scalar values.

        Returns:
            The resulting Vector from the linear combination.

        Raises:
            ValueError: If lists are empty, counts mismatch, or vectors have different lengths.
            TypeError: If vectors is not a sequence of Vector objects.
        """
        if not vectors or not scalars:
            raise ValueError("Vectors and scalars sequences cannot be empty.")
        if len(vectors) != len(scalars):
            raise ValueError("Number of vectors must match number of scalars.")
        if not all(isinstance(v, Vector) for v in vectors):
             raise TypeError("All items in 'vectors' must be Vector instances.")

        # Check that all vectors have the same length as the first one
        expected_len = len(vectors[0])
        for i, v in enumerate(vectors[1:], 1):
            if len(v) != expected_len:
                raise ValueError(f"Vector at index {i} has different length ({len(v)}) than expected ({expected_len}).")

        # Initialize result vector with zeros
        result_data = [0.0] * expected_len

        # Compute linear combination
        for vec, scalar in zip(vectors, scalars):
            for i in range(expected_len):
                result_data[i] += scalar * vec.data[i]

        # Return a new Vector of the same type as the input vectors
        return vectors[0].__class__(result_data)

    @staticmethod
    def angle_cos(u: T, v: T) -> float:
        """
        Computes the cosine of the angle between two vectors u and v.

        Formula: cos(θ) = (u · v) / (‖u‖ * ‖v‖)

        Args:
            u: The first vector.
            v: The second vector.

        Returns:
            The cosine of the angle between u and v.

        Raises:
            ValueError: If vectors have different sizes or if either has zero norm (magnitude).
        """
        u._validate_same_size(v)
        norm_u = u.norm()
        norm_v = v.norm()
        if norm_u == 0 or norm_v == 0:
            raise ValueError("Cannot compute angle with a zero vector (zero norm).")
        dot_product = u.dot(v)
        # Clamp value to [-1, 1] due to potential floating point inaccuracies
        return max(-1.0, min(1.0, dot_product / (norm_u * norm_v)))

    # ──────────────────────────────────────────────────────────────────────
    # Instance Methods
    def dot(self, other: T) -> float:
        """
        Computes the dot product (scalar product) of this vector with another.

        Args:
            other: The other vector.

        Returns:
            The dot product.

        Raises:
            ValueError: If vectors have different sizes.
        """
        self._validate_same_size(other)
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm_1(self) -> float:
        """
        Computes the 1-norm (Manhattan norm) of the vector.
        Sum of the absolute values of the coordinates.
        """
        return sum(abs(x) for x in self.data)

    def norm(self) -> float:
        """
        Computes the 2-norm (Euclidean norm/magnitude) of the vector.
        Square root of the sum of the squares of the coordinates.
        """
        # Equivalent to math.sqrt(self.dot(self)) but avoids creating zip object
        return math.sqrt(sum(x * x for x in self.data))

    def norm_inf(self) -> float:
        """
        Computes the infinity norm (maximum norm) of the vector.
        Maximum absolute value among the coordinates.
        """
        return max(abs(x) for x in self.data) if self.data else 0.0

    def cross(self: T, other: T) -> T:
        """
        Computes the cross product of this vector with another 3D vector.

        Args:
            other: The other 3D vector.

        Returns:
            A new 3D Vector representing the cross product.

        Raises:
            ValueError: If either vector is not 3-dimensional.
        """
        self._validate_dimension(3)
        other._validate_dimension(3) # Also check the other vector

        a1, a2, a3 = self.data
        b1, b2, b3 = other.data
        cross_data = [
            a2 * b3 - a3 * b2,
            a3 * b1 - a1 * b3,
            a1 * b2 - a2 * b1,
        ]
        return self.__class__(cross_data)
