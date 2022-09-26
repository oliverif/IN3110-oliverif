"""
Tests for our array class
"""

from array_class import Array

import pytest

# 1D tests (Task 4)


def test_str_1d(capsys):
    # Tests both __str__ function itself and that printing the array yields expected results.

    # Test __str__ function
    assert Array((3,), 3, 2, 5).__str__() == "[3, 2, 5]"
    assert Array((4,), True, False, True, True).__str__() == "[True, False, True, True]"
    assert Array((3,), 5.2, 4.12, 87.445).__str__() == "[5.2, 4.12, 87.445]"

    # Test printing
    print(Array((3,), 3, 2, 5))
    captured = capsys.readouterr()
    assert captured.out == "[3, 2, 5]\n"

    print(Array((4,), True, False, True, True))
    captured = capsys.readouterr()
    assert captured.out == "[True, False, True, True]\n"

    print(Array((3,), 5.2, 4.12, 87.445))
    captured = capsys.readouterr()
    assert captured.out == "[5.2, 4.12, 87.445]\n"


def test_add_1d():
    # Tests if addition of array works as inteded for 1D cases. Note function __add__() is used here, however it is
    # possible to test with simply using the + operator. This could have been done using parametrize(which is used later).
    # Note that in most tests the class attribute flat_arr, which is a native python list, is used when
    # asserting equality. This avoids dependence on a working __eq__() function to test other functions.
    # Further note that both __add__() and __radd__() are tested by swapping places of arguments

    # Test int array addition
    intarr1 = Array((3,), 3, 2, 5)
    intarr2 = Array((3,), 4, 6, 4)
    intarr3 = Array((2,), 6, 9)
    add_res = (intarr1 + intarr2).flat_arr
    assert add_res == [7, 8, 9]  # This avoids being dependent on a working __eq__ to test this
    assert (intarr2 + intarr1).flat_arr == [7, 8, 9]
    assert (intarr1 + 10).flat_arr == [13, 12, 15]
    assert (10 + intarr1).flat_arr == [13, 12, 15]
    assert intarr1.__add__(intarr3) == NotImplemented

    # Test float array addition
    floatarr1 = Array((3,), 3.3, 2.1, 5.9)
    floatarr2 = Array((3,), 4.8, 6.9, 4.2)
    floatarr3 = Array((2,), 6.2, 9.3)
    add_res = (floatarr1 + floatarr2).flat_arr
    assert add_res == pytest.approx([8.1, 9.0, 10.1])  # Must use approx for float comparison due to machine precision
    assert (floatarr2 + floatarr1).flat_arr == pytest.approx([8.1, 9.0, 10.1])
    assert (floatarr1 + 10).flat_arr == pytest.approx([13.3, 12.1, 15.9])
    assert (10 + floatarr1).flat_arr == pytest.approx([13.3, 12.1, 15.9])
    assert floatarr1.__add__(floatarr3) == NotImplemented

    # Test bool array addition
    boolarr1 = Array((3,), True, False, False)
    boolarr2 = Array((3,), True, True, False)
    assert boolarr1.__add__(10) == NotImplemented
    assert boolarr1.__add__(boolarr2) == NotImplemented
    assert boolarr1.__add__(intarr1) == NotImplemented
    assert boolarr1.__add__(floatarr1) == NotImplemented
    assert intarr1.__add__(boolarr1) == NotImplemented
    assert floatarr1.__add__(boolarr1) == NotImplemented

    # Test int and float mix
    assert (intarr1 + floatarr1).flat_arr == pytest.approx([6.3, 4.1, 10.9])
    assert (floatarr1 + intarr1).flat_arr == pytest.approx([6.3, 4.1, 10.9])


def test_sub_1d():
    # Tests if elementwise subtraction works as intended for 1D cases. Tests the __sub__() and __rsub()__ functions by using the
    # - operator.
    # Test int array subtraction
    intarr1 = Array((3,), 3, 2, 5)
    intarr2 = Array((3,), 4, 6, 4)
    intarr3 = Array((2,), 6, 9)
    assert (intarr1 - intarr2).flat_arr == [-1, -4, 1]  # This avoids being dependent on a working __eq__ to test this
    assert (intarr2 - intarr1).flat_arr == [1, 4, -1]
    assert (intarr1 - 10).flat_arr == [-7, -8, -5]
    assert (10 - intarr1).flat_arr == [7, 8, 5]
    assert intarr1.__sub__(intarr3) == NotImplemented

    # Test float array subtraction
    floatarr1 = Array((3,), 3.3, 2.1, 5.9)
    floatarr2 = Array((3,), 4.8, 6.9, 4.2)
    floatarr3 = Array((2,), 6.2, 9.3)
    assert (floatarr1 - floatarr2).flat_arr == pytest.approx([-1.5, -4.8, 1.7])  # Must use approx for float comparison
    assert (floatarr2 - floatarr1).flat_arr == pytest.approx([1.5, 4.8, -1.7])
    assert (floatarr1 - 10).flat_arr == pytest.approx([-6.7, -7.9, -4.1])
    assert (10 - floatarr1).flat_arr == pytest.approx([6.7, 7.9, 4.1])
    assert floatarr1.__sub__(floatarr3) == NotImplemented
    assert floatarr1.__rsub__(floatarr3) == NotImplemented

    # Test bool array subtraction
    boolarr1 = Array((3,), True, False, False)
    boolarr2 = Array((3,), True, True, False)
    assert boolarr1.__sub__(10) == NotImplemented
    assert boolarr1.__sub__(boolarr2) == NotImplemented
    assert boolarr1.__sub__(intarr1) == NotImplemented
    assert boolarr1.__sub__(floatarr1) == NotImplemented
    assert intarr1.__sub__(boolarr1) == NotImplemented
    assert floatarr1.__sub__(boolarr1) == NotImplemented
    assert boolarr1.__rsub__(10) == NotImplemented
    assert boolarr1.__rsub__(boolarr2) == NotImplemented
    assert boolarr1.__rsub__(intarr1) == NotImplemented
    assert boolarr1.__rsub__(floatarr1) == NotImplemented
    assert intarr1.__rsub__(boolarr1) == NotImplemented
    assert floatarr1.__rsub__(boolarr1) == NotImplemented

    # Test int and float mix
    assert (intarr1 - floatarr1).flat_arr == pytest.approx([-0.3, -0.1, -0.9])
    assert (floatarr1 - intarr1).flat_arr == pytest.approx([0.3, 0.1, 0.9])


def test_mul_1d():
    # Tests if elementwise multiplication works as intended for 1D cases. Tests the __mul__() and __rmul()__ functions by using the
    # * operator.
    # Test int array multiplication
    intarr1 = Array((3,), 3, 2, 5)
    intarr2 = Array((3,), 4, 6, 4)
    intarr3 = Array((2,), 6, 9)
    assert (intarr1 * intarr2).flat_arr == [12, 12, 20]  # This avoids being dependent on a working __eq__ to test this
    assert (intarr2 * intarr1).flat_arr == [12, 12, 20]
    assert (intarr1 * 10).flat_arr == [30, 20, 50]
    assert (10 * intarr1).flat_arr == [30, 20, 50]
    assert intarr1.__mul__(intarr3) == NotImplemented

    # Test float array multiplication
    floatarr1 = Array((3,), 3.3, 2.1, 5.9)
    floatarr2 = Array((3,), 4.8, 6.9, 4.2)
    floatarr3 = Array((2,), 6.2, 9.3)
    assert (floatarr1 * floatarr2).flat_arr == pytest.approx([15.84, 14.49, 24.78])
    assert (floatarr2 * floatarr1).flat_arr == pytest.approx([15.84, 14.49, 24.78])
    assert (floatarr1 * 10).flat_arr == pytest.approx([33.0, 21.0, 59.0])
    assert (10 * floatarr1).flat_arr == pytest.approx([33.0, 21.0, 59.0])
    assert floatarr1.__mul__(floatarr3) == NotImplemented

    # Test bool array multiplication
    boolarr1 = Array((3,), True, False, False)
    boolarr2 = Array((3,), True, True, False)
    assert boolarr1.__mul__(10) == NotImplemented
    assert boolarr1.__mul__(boolarr2) == NotImplemented
    assert boolarr1.__mul__(intarr1) == NotImplemented
    assert boolarr1.__mul__(floatarr1) == NotImplemented
    assert intarr1.__mul__(boolarr1) == NotImplemented
    assert floatarr1.__mul__(boolarr1) == NotImplemented
    assert boolarr1.__rmul__(10) == NotImplemented
    assert boolarr1.__rmul__(boolarr2) == NotImplemented
    assert boolarr1.__rmul__(intarr1) == NotImplemented
    assert boolarr1.__rmul__(floatarr1) == NotImplemented
    assert intarr1.__rmul__(boolarr1) == NotImplemented
    assert floatarr1.__rmul__(boolarr1) == NotImplemented

    # Test int and float mix
    assert (intarr1 * floatarr1).flat_arr == pytest.approx([9.9, 4.2, 29.5])
    assert (floatarr1 * intarr1).flat_arr == pytest.approx([9.9, 4.2, 29.5])


@pytest.mark.parametrize(
    "lhs,rhs,expected",
    [
        (Array((3,), 3, 2, 5), Array((3,), 4, 6, 4), False),
        (Array((3,), 3, 2, 5), Array((3,), 3, 2, 5), True),
        (Array((3,), 3, 2, 5), Array((2,), 3, 2), False),
        (Array((3,), 3.3, 2.1, 5.9), Array((3,), 4.8, 6.9, 4.2), False),
        (Array((3,), 3.3, 2.1, 5.9), Array((3,), 3.3, 2.1, 5.9), True),
        (Array((3,), 3.3, 2.1, 5.9), Array((2,), 6.2, 9.3), False),
        (Array((3,), True, False, False), Array((3,), True, True, False), False),
        (Array((3,), True, False, False), Array((3,), True, False, False), True),
        (Array((3,), True, False, False), Array((2,), True, True), False),
        (Array((3,), 3, 2, 5), Array((3,), 3.3, 2.1, 5.9), False),
        (Array((3,), 3, 2, 5), Array((3,), True, False, False), False),
        (Array((3,), True, False, False), Array((3,), 3.3, 2.1, 5.9), False),
        (Array((3,), 3, 2, 5), "Not an array", False),
        (Array((3,), 3, 2, 5), 10, False),
    ],
)
def test_eq_1d(lhs, rhs, expected):
    # Tests the __eq__() function by using the == operator for 1D cases
    assert (lhs == rhs) == expected


@pytest.mark.parametrize(
    "lhs,rhs,expected",
    [
        (Array((3,), 3, 2, 5), Array((3,), 2, 2, 2), [False, True, False]),
        (Array((3,), 3, 2, 5), 2, [False, True, False]),
        (Array((3,), 3, 2, 5), Array((2,), 3, 2), None),
        (Array((3,), 3.3, 2.1, 5.9), Array((3,), 4.8, 2.1, 4.2), [False, True, False]),
        (Array((3,), 3.3, 2.1, 5.9), 5.9, [False, False, True]),
        (Array((3,), 3.3, 2.1, 5.9), Array((2,), 6.2, 9.3), None),
        (Array((3,), True, False, False), Array((3,), True, True, False), [True, False, True]),
        (Array((3,), True, False, False), False, [False, True, True]),
        (Array((3,), True, False, False), Array((2,), True, True), None),
        (Array((3,), 3, 2, 5), Array((3,), 3.3, 2.1, 5.9), [False, False, False]),
        (Array((3,), 3, 2, 5), Array((3,), True, False, False), [False, False, False]),
        (Array((3,), 3.3, 2.1, 5.9), Array((3,), True, False, False), [False, False, False]),
    ],
)
def test_same_1d(lhs, rhs, expected):
    # Tests the is_equal() function for 1D cases
    if expected is None:
        with pytest.raises(ValueError):
            lhs.is_equal(rhs)
    else:
        assert lhs.is_equal(rhs).flat_arr == expected


@pytest.mark.parametrize(
    "arr,expected",
    [
        (Array((3,), 3, 2, 5), 2),
        (Array((3,), -3, 2, 5), -3),
        (Array((3,), 3.3, 2.1, 5.9), 2.1),
        (Array((3,), -3.3, 2.1, 5.9), -3.3),
        (Array((3,), True, False, False), None),
    ],
)
def test_smallest_1d(arr, expected):
    # Tests the min_element() function for 1D cases
    if expected is None:
        with pytest.raises(TypeError):
            arr.min_element()
    else:
        assert arr.min_element() == pytest.approx(expected)


@pytest.mark.parametrize(
    "arr,expected",
    [
        (Array((3,), 3, 2, 5), 3.333333333),
        (Array((3,), 3.3, 2.1, 5.9), 3.766666666),
        (Array((3,), True, False, False), None),
    ],
)
def test_mean_1d(arr, expected):
    # Tests the mean_element() function for 1D cases
    if expected is None:
        with pytest.raises(TypeError):
            arr.mean_element()
    else:
        assert arr.mean_element() == pytest.approx(expected)


# 2D tests (Task 6)


@pytest.mark.parametrize(
    "lhs,rhs,expected",
    [  # Ints
        (Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 4, 6, 4, 1, 0, -1), Array((3, 2), 7, 8, 9, 5, 9, 19)),
        (Array((3, 2), 4, 6, 4, 1, 0, -1), Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 7, 8, 9, 5, 9, 19)),
        (Array((3, 2), 3, 2, 5, 4, 9, 20), 2, Array((3, 2), 5, 4, 7, 6, 11, 22)),  # Scalar
        (2, Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 5, 4, 7, 6, 11, 22)),
        # Floats
        (
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 8.1, 9.0, 10.1, 6.9, 11.7, 7.8),
        ),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((3, 2), 8.1, 9.0, 10.1, 6.9, 11.7, 7.8),
        ),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            3.1,
            Array((3, 2), 7.9, 10.0, 7.3, 8.7, 7.0, 10.4),
        ),  # Scalar
        (
            3.1,
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 7.9, 10.0, 7.3, 8.7, 7.0, 10.4),
        ),
        # Bools
        (Array((2, 2), True, False, False, True), Array((2, 2), True, True, False, False), NotImplemented),
        (
            Array((3, 2), True, False, False, True, False, False),
            Array((2, 2), True, True, False, False),
            NotImplemented,
        ),
        # Mix of types
        (
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 7.8, 8.9, 9.2, 9.6, 12.9, 27.3),
        ),
        (Array((3, 2), 3, 2, 5, 4, 9, 20), 2.1, Array((3, 2), 5.1, 4.1, 7.1, 6.1, 11.1, 22.1)),  # Scalar
        (2.1, Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 5.1, 4.1, 7.1, 6.1, 11.1, 22.1)),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            3,
            Array((3, 2), 7.8, 9.9, 7.2, 8.6, 6.9, 10.3),
        ),
        (
            3,
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 7.8, 9.9, 7.2, 8.6, 6.9, 10.3),
        ),
        (
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((3, 2), True, False, False, True, False, False),
            NotImplemented,
        ),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), True, False, False, True, False, False),
            NotImplemented,
        ),
        (
            Array((3, 2), True, False, False, True, False, False),
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            NotImplemented,
        ),
        (
            Array((3, 2), True, False, False, True, False, False),
            2,
            NotImplemented,
        ),
        (
            Array((3, 2), True, False, False, True, False, False),
            2.1,
            NotImplemented,
        ),
        # Non-equal shapes
        (Array((3, 2), 3, 2, 5, 4, 9, 20), Array((2, 2), 4, 6, 4, 1), NotImplemented),
        (  # check flipped dim
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((2, 3), 4, 6, 4, 1, 0, -1),
            NotImplemented,
        ),
        (
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((2, 2), 4.8, 6.9, 4.2, 5.6),
            NotImplemented,
        ),
    ],
)
def test_add_2d(lhs, rhs, expected):
    # Tests if elementwise addition works as intended for 2D cases
    if expected is NotImplemented:
        with pytest.raises(TypeError):
            res = lhs + rhs
    else:
        assert (lhs + rhs).flat_arr == pytest.approx(expected.flat_arr)


@pytest.mark.parametrize(
    "lhs,rhs,expected",
    [  # Ints
        (Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 4, 6, 4, 1, 0, -1), Array((3, 2), 12, 12, 20, 4, 0, -20)),
        (Array((3, 2), 4, 6, 4, 1, 0, -1), Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 12, 12, 20, 4, 0, -20)),
        (Array((3, 2), 3, 2, 5, 4, 9, 20), 2, Array((3, 2), 6, 4, 10, 8, 18, 40)),  # Scalar
        (2, Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 6, 4, 10, 8, 18, 40)),
        # Floats
        (
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 15.84, 14.49, 24.78, 7.28, 30.42, 3.65),
        ),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((3, 2), 15.84, 14.49, 24.78, 7.28, 30.42, 3.65),
        ),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            3.1,
            Array((3, 2), 14.88, 21.39, 13.02, 17.36, 12.09, 22.63),
        ),  # Scalar
        (
            3.1,
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 14.88, 21.39, 13.02, 17.36, 12.09, 22.63),
        ),
        # Bools
        (Array((2, 2), True, False, False, True), Array((2, 2), True, True, False, False), NotImplemented),
        (
            Array((3, 2), True, False, False, True, False, False),
            Array((2, 2), True, True, False, False),
            NotImplemented,
        ),
        # Mix of types
        (
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 14.4, 13.8, 21.0, 22.4, 35.1, 146.0),
        ),
        (Array((3, 2), 3, 2, 5, 4, 9, 20), 2.1, Array((3, 2), 6.3, 4.2, 10.5, 8.4, 18.9, 42.0)),  # Scalar
        (2.1, Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 6.3, 4.2, 10.5, 8.4, 18.9, 42.0)),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            3,
            Array((3, 2), 14.4, 20.7, 12.6, 16.8, 11.7, 21.9),
        ),
        (
            3,
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), 14.4, 20.7, 12.6, 16.8, 11.7, 21.9),
        ),
        (
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((3, 2), True, False, False, True, False, False),
            NotImplemented,
        ),
        (
            Array((3, 2), 4.8, 6.9, 4.2, 5.6, 3.9, 7.3),
            Array((3, 2), True, False, False, True, False, False),
            NotImplemented,
        ),
        (
            Array((3, 2), True, False, False, True, False, False),
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            NotImplemented,
        ),
        (
            Array((3, 2), True, False, False, True, False, False),
            2,
            NotImplemented,
        ),
        (
            Array((3, 2), True, False, False, True, False, False),
            2.1,
            NotImplemented,
        ),
        # Non-equal shapes
        (Array((3, 2), 3, 2, 5, 4, 9, 20), Array((2, 2), 4, 6, 4, 1), NotImplemented),
        (  # check flipped dim
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((2, 3), 4, 6, 4, 1, 0, -1),
            NotImplemented,
        ),
        (
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((2, 2), 4.8, 6.9, 4.2, 5.6),
            NotImplemented,
        ),
    ],
)
def test_mult_2d(lhs, rhs, expected):
    # Tests if elementwise multiplication works as intended for 2D cases
    if expected is NotImplemented:
        with pytest.raises(TypeError):
            res = lhs * rhs
    else:
        assert (lhs * rhs).flat_arr == pytest.approx(expected.flat_arr)


@pytest.mark.parametrize(
    "lhs,rhs,expected",
    [
        (Array((3, 2), 3, 2, 5, 4, 9, 20), Array((3, 2), 3, 6, 5, 7, 9, 20), [True, False, True, False, True, True]),
        (Array((3, 2), 3, 2, 5, 4, 3, 2), 2, [False, True, False, False, False, True]),
        (Array((3, 2), 3, 2, 5, 4, 3, 2), Array((2, 2), 3, 2, 3, 5), None),
        (
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((3, 2), 3.2, 2.1, 5.9, 1.3, 7.8, 0.6),
            [False, True, True, True, True, False],
        ),
        (Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5), 5.9, [False, False, True, False, False, False]),
        (Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5), Array((2, 2), 6.2, 9.3, 3.4, 5.2), None),
        (Array((2, 2), True, False, False, True), Array((2, 2), True, True, False, True), [True, False, True, True]),
        (Array((2, 2), True, False, False, True), True, [True, False, False, True]),
        (Array((2, 2), True, False, False, True), Array((3, 2), True, True, False, True, False, True), None),
        (
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            [False, False, False, False, False, False],
        ),
        (
            Array((3, 2), 3, 2, 5, 4, 9, 20),
            Array((3, 2), True, True, False, True, False, True),
            [False, False, False, False, False, False],
        ),
        (
            Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5),
            Array((3, 2), True, True, False, True, False, True),
            [False, False, False, False, False, False],
        ),
    ],
)
def test_same_2d(lhs, rhs, expected):
    # Tests the is_equal() function for 2D cases
    if expected is None:
        with pytest.raises(ValueError):
            lhs.is_equal(rhs)
    else:
        assert lhs.is_equal(rhs).flat_arr == expected


@pytest.mark.parametrize(
    "arr,expected",
    [
        (Array((3, 2), 3, 2, 5, 4, 9, 20), 7.166666666),
        (Array((3, 2), 3.3, 2.1, 5.9, 1.3, 7.8, 0.5), 3.48333333),
        (Array((3, 2), True, True, False, True, False, True), None),
    ],
)
def test_mean_2d(arr, expected):
    # Tests the mean_element() function for 2D cases
    if expected is None:
        with pytest.raises(TypeError):
            arr.mean_element()
    else:
        assert arr.mean_element() == pytest.approx(expected)
