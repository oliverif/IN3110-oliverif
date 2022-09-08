"""
Tests for our array class
"""

from array_class import Array

import pytest

# 1D tests (Task 4)


def test_str_1d(capsys):
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
    ],
)
def test_eq_1d(lhs, rhs, expected):
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
    if expected is None:
        with pytest.raises(ValueError):
            lhs.is_equal(rhs)
    else:
        assert lhs.is_equal(rhs).flat_arr == expected


def test_smallest_1d():
    pass


def test_mean_1d():
    pass


# 2D tests (Task 6)


def test_add_2d():
    pass


def test_mult_2d():
    pass


def test_same_2d():
    pass


def test_mean_2d():
    pass


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
