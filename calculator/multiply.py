from .operations import Operation

class Multiply(Operation):
    name = "Multiply"
    def execute(self, a: float, b: float) -> float:
        return a * b
