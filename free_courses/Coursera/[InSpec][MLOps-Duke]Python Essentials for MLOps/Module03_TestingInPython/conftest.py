'''
This file is created for running pytest:
-   As soon as pytest starts collecting tests, it will load conftest.py
-   That line prepends our src/ foler to Python's import search path.
-   This allow doing 'from calculator import Calculator' in our test files works for pytest.
'''


import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
