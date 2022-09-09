# Assignment 2

This folder contains an implementation of a python array. Class implementation `Array` can be found  in the file `array_class.py` with it's attributes and methods.

## Running the code
`array_class.py` is primarily a class implementation that can be used in other scripts or notebooks. The notebook `notebook.py` shows some of the examples shown in the exercise. `array_class.py` can also be run in the terminal for a simple example:
```
python3 array_class.py
```
Which should give you the output
```
Array 1 = [1, 2, 3, 4]

Array 1 = [5, 6, 7, 8]

Array 1 + Array 2 = [6, 8, 10, 12]
```

## Tests
Tests for `array_class.py` are implemented in the file `test_array.py`. Note that [pytest](https://doc.pytest.org/en/latest/getting-started.html) is required to actually run the tests, as methods like `pytest.parametrize(...)` are used to test multiple examples. To run the test, execute in terminal:
```
pyest test_array.py
```
