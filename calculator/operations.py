import math
from abc import ABC, abstractmethod

class Operation(ABC):
    name: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...

class Add(Operation):
    name = "Add"

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"

    def execute(self, a: float, b: float) -> float:
        return a - b

class Factorial(Operation):
    name = "Factorial"

    def execute(self, a: float, b: float) -> float:
        # Factorial is a unary operation, so 'b' is ignored.
        # It is defined only for non-negative integers.
        if not isinstance(a, (int, float)) or a < 0 or a != int(a):
            raise ValueError("Factorial is only defined for non-negative integers.")
        
        # Convert to int for math.factorial function
        n = int(a)
        return float(math.factorial(n))
