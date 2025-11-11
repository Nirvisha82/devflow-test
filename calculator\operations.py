from abc import ABC, abstractmethod
from typing import Union, Tuple

class Operation(ABC):
    name: str

    @abstractmethod
    def execute(self, a: float, b: float) -> Union[float, Tuple[float, float]]:
        ...

class Add(Operation):
    name = "Add"

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"

    def execute(self, a: float, b: float) -> float:
        return a - b

class Cube(Operation):
    name = "Cube"

    def execute(self, a: float, b: float) -> Tuple[float, float]:
        return (a ** 3, b ** 3)
