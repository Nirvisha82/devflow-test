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

class Divide(Operation):
    name = "Divide"

    def execute(self, a: float, b: float) -> float:
        return a / b

class Multiply(Operation):
    name = "Multiply"

    def execute(self, a: float, b: float) -> float:
        return a * b

class Square(Operation):
    name = "Square"

    def execute(self, a: float, b: float) -> float:
        return a * a + b * b

class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
