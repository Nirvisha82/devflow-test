from abc import ABC, abstractmethod

class Operation(ABC):
    name: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        # Abstract method for an operation. 'b' might be ignored for unary operations.
        pass

class Add(Operation):
    name = "Add"

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"

    def execute(self, a: float, b: float) -> float:
        return a - b

class Square(Operation):
    name = "Square"

    def execute(self, a: float, b: float) -> float:
        # For unary operations like Square, 'b' is ignored.
        return a * a
