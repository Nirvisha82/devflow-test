from abc import ABC, abstractmethod

class Operation(ABC):
    name: str
    is_unary: bool = False # Added: A flag to indicate if the operation is unary or binary

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...

class Add(Operation):
    name = "Add"
    is_unary = False # Explicitly set for clarity

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"
    is_unary = False # Explicitly set for clarity

    def execute(self, a: float, b: float) -> float:
        return a - b

class Cube(Operation):
    name = "Cube"
    is_unary = True # This is a unary operation

    def execute(self, a: float, b: float) -> float:
        # For unary operations, the second argument 'b' is ignored.
        return a ** 3
