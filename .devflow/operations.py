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
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
