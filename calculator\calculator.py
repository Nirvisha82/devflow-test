from typing import Dict, Type
from .operations import Operation, Add, Subtract, Square # Import the new Square operation

class Calculator:
    """
    Simple OOP calculator that delegates to Operation objects.
    You can register new operations without changing the UI.
    """
    def __init__(self) -> None:
        self._operations: Dict[str, Operation] = {}
        self._register_default_operations()

    def _register_default_operations(self) -> None:
        # Register default binary operations
        self.register_operation("1", Add())
        self.register_operation("2", Subtract())
        # Register the new unary Square operation
        self.register_operation("3", Square())

    def register_operation(self, key: str, operation: Operation) -> None:
        self._operations[key] = operation

    @property
    def menu_items(self) -> Dict[str, Operation]:
        return self._operations

    def compute(self, key: str, a: float, b: float) -> float:
        if key not in self._operations:
            raise KeyError(f"Unknown operation key: {key}")
        # The execute method of the specific operation handles whether 'b' is used or ignored.
        return self._operations[key].execute(a, b)
