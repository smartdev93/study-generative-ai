# MODULE 03 - TESTING IN PYTHON

## I - The `unittest` framework

### Running the test
```
python -m unittest
```
By running above command, the `unittest` will discover all subcasses of unittest.TestCase in files named `test*.py` by default. Or 
```
python -m unittest discover -s tests -p "test_*.py" -v
```
to tell the unittest to start directly at the `tests` directory and look for the file with the filename like `test_*.py`. Or
```
python main.py [operation] [value a] [value b]
```
To test one specific operation of the calculator with specific input values.


### Advantages of `unittest`
- Standard Library: No external dependency, immediately available.
- Fine-grained control: We can build complex test suites by hand if needed.

### Limitations of `unittest`
- Boilerplate Overhead: We must subclass `TestCase`, prefix method with `test_`, and call assertion methods on `self`.
- Limited Fixture Parametrization: While we can do `setUp`/`tearDown`, there's no first-class, function-scoped or dependcy injection mechanism like pytest's.

## II - `pytest` framwork

`pytest` is a third-party testing framework that builds on top of (and can even run) `unittest`.

Some features of `pytest`:
- Function-based tests: Do not need to create a class. Any file named `test*.py` or `*_test.py` is picked up.
- Scoped fixtures: `function` (default), `class`, `module`, or `session`.
- Parametrization: Run a single test with multiple sets of inputs.

### Running the test
Simply run the command:
```
pytest
```
