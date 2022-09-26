from math import prod
from statistics import mean

"""
Array class for assignment 2
"""


class Array:
    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Check if the values are of valid types
        if not isinstance(shape, tuple) and not all([type(x) in [int, bool, float] for x in values]):
            raise TypeError("Invalid type for shape or values")

        if not len(set([type(x) for x in values])) == 1:
            raise ValueError("Given values are not all of the same type")

        # Check that the amount of values corresponds to the shape
        if not prod(shape) == len(values):
            raise ValueError("The amount of values given does not correspond to the shape")

        # Set instance attributes
        self.flat_arr = self.array = list(values)
        self.shape = shape

        # For each dimension, subdivide into lists containing dim slices of the previous list
        # If len(shape) == 1 this for loop will simply be skipped.
        # This allows n dimensional arrays
        for i in range(len(shape) - 1, 0, -1):
            dim = shape[i]
            self.array = [self.array[i : i + dim] for i in range(0, len(self.array), dim)]

    def __getitem__(self, key):
        """Returns the value of array at index key.

        Enables indexing of Array

        Args:
            key (int): The index key of the array for the item to be returned

        Returns:
            Union(List, Union(int, float, bool)): Returns either a sublist or the number itself(if inner dimension is
            reached)

        Raises:
            TypeError: If key is wrong type or contains wrong types
        """

        if not isinstance(key, int) or (isinstance(key, tuple) and not all([type(x) == int for x in key])):
            raise TypeError("Index should be integer or tuple of integers")

        return self.array[key]

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return str(self.array)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        if (
            not isinstance(other, (Array, int, float))  # wrong type
            or (isinstance(other, Array) and other.shape != self.shape)  # array but non-equal shape
            or isinstance(self.flat_arr[0], bool)  # self is bool type Array
            or (isinstance(other, Array) and isinstance(other.flat_arr[0], bool))  # other is bool type Array
        ):
            return NotImplemented

        if isinstance(other, Array):
            return Array(self.shape, *[sum(vals) for vals in zip(self.flat_arr, other.flat_arr)])
        return Array(self.shape, *[val + other for val in self.flat_arr])

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        if (
            not isinstance(other, (Array, int, float))
            or (isinstance(other, Array) and other.shape != self.shape)
            or isinstance(self.flat_arr[0], bool)
            or (isinstance(other, Array) and isinstance(other.flat_arr[0], bool))
        ):
            return NotImplemented

        if isinstance(other, Array):
            return Array(self.shape, *[l - r for l, r in zip(self.flat_arr, other.flat_arr)])
        return Array(self.shape, *[val - other for val in self.flat_arr])

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        if (
            not isinstance(other, (Array, int, float))
            or (isinstance(other, Array) and other.shape != self.shape)
            or isinstance(self.flat_arr[0], bool)
            or (isinstance(other, Array) and isinstance(other.flat_arr[0], bool))
        ):
            return NotImplemented

        if isinstance(other, Array):
            return Array(self.shape, *[r - l for l, r in zip(self.flat_arr, other.flat_arr)])
        return Array(self.shape, *[other - val for val in self.flat_arr])

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if (
            not isinstance(other, (Array, int, float))
            or (isinstance(other, Array) and other.shape != self.shape)
            or isinstance(self.flat_arr[0], bool)
            or (isinstance(other, Array) and isinstance(other.flat_arr[0], bool))
        ):
            return NotImplemented

        if isinstance(other, Array):
            return Array(self.shape, *[l * r for l, r in zip(self.flat_arr, other.flat_arr)])
        return Array(self.shape, *[val * other for val in self.flat_arr])

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods   ... but not rsub though right?
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if not isinstance(other, Array):
            return False
        elif not self.shape == other.shape:
            return False
        else:
            return self.flat_arr == other.flat_arr

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("The shapes of the compared arrays are not equal")
            else:
                return Array(self.shape, *[a == b for a, b in zip(self.flat_arr, other.flat_arr)])

        elif not isinstance(other, (int, float, bool)):
            raise TypeError("Invalid type of 'other'")

        return Array(self.shape, *[a == other for a in self.flat_arr])

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """

        if isinstance(self.flat_arr[0], bool):
            raise TypeError("Cannot find minimum of boolean array")
        return float(min(self.flat_arr))

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        if isinstance(self.flat_arr[0], bool):
            raise TypeError("Cannot find minimum of boolean array")
        return mean(self.flat_arr)


if __name__ == "__main__":
    arr1 = Array((4,), 1, 2, 3, 4)
    print(f"Array 1 = {arr1}\n")
    arr2 = Array((4,), 5, 6, 7, 8)
    print(f"Array 1 = {arr2}\n")
    print(f"Array 1 + Array 2 = {arr1+arr2}")
