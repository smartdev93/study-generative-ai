class Calculator():
    """
        Simulation of a normal calculator
    """
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
        except Exception as error:
            result = error
        return result