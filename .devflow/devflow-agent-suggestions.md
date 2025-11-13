# Square Root Functionality Implementation

## Analysis

The issue requests adding square root functionality to the calculator application. Currently, the calculator supports Add, Subtract, Divide, Multiply, Square, and Power operations. The square root operation is a mathematical function that differs from existing operations in that it typically requires only one number (unary operation) rather than two numbers (binary operations).

### Current State
- The calculator uses the **Strategy Pattern** with an `Operation` abstract base class
- All current operations are binary (take two parameters: `a` and `b`)
- The `Square` operation computes `a^2 + b^2` (sum of squares)
- The application prompts for two numbers regardless of the operation

### Challenge
The main challenge is that square root is a **unary operation** (operates on a single number), while the current architecture is designed for **binary operations** (operate on two numbers). We need to decide on the implementation approach:

**Option 1**: Implement square root as a unary operation and modify the architecture to support both unary and binary operations
**Option 2**: Keep it binary-compatible by computing the square root of the sum (sqrt(a^2 + b^2))
**Option 3**: Compute square root of only the first number (sqrt(a)) and ignore the second number

**Recommended**: Option 1 (proper unary operation support) - This is the most mathematically correct and extensible approach.

---

## Affected Files

1. **`calculator/operations.py`** - Add new `SquareRoot` operation class
2. **`calculator/calculator.py`** - Modify to support both unary and binary operations
3. **`calculator/__init__.py`** - Export the new `SquareRoot` class
4. **`app.py`** - Update UI to handle unary operations (prompt for one number when needed)

---

## Code Examples

### 1. Modified `calculator/operations.py`

Add the `SquareRoot` class and create a base distinction between unary and binary operations:

```python
from abc import ABC, abstractmethod
import math

class Operation(ABC):
    name: str
    symbol: str = ""
    is_unary: bool = False  # New attribute to distinguish unary operations

    @abstractmethod
    def execute(self, a: float, b: float = None) -> float:
        ...

class Add(Operation):
    name = "Add"
    symbol = "+"
    is_unary = False

    def execute(self, a: float, b: float = None) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"
    symbol = "-"
    is_unary = False

    def execute(self, a: float, b: float = None) -> float:
        return a - b

class Divide(Operation):
    name = "Divide"
    symbol = "/"
    is_unary = False

    def execute(self, a: float, b: float = None) -> float:
        return a / b

class Multiply(Operation):
    name = "Multiply"
    symbol = "*"
    is_unary = False

    def execute(self, a: float, b: float = None) -> float:
        return a * b

class Square(Operation):
    name = "Square"
    symbol = "^2"
    is_unary = False

    def execute(self, a: float, b: float = None) -> float:
        return a * a + b * b

class Power(Operation):
    name = "Power"
    symbol = "^"
    is_unary = False

    def execute(self, a: float, b: float = None) -> float:
        return a ** b

class SquareRoot(Operation):
    name = "Square Root"
    symbol = "sqrt"
    is_unary = True  # This is a unary operation

    def execute(self, a: float, b: float = None) -> float:
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return math.sqrt(a)
```

### 2. Modified `calculator/calculator.py`

Update to handle both unary and binary operations:

```python
from typing import Dict, Type
from .operations import Operation, Add, Subtract, Divide, Multiply, Square, Power, SquareRoot

class Calculator:
    """
    Simple OOP calculator that delegates to Operation objects.
    You can register new operations without changing the UI.
    Supports both unary and binary operations.
    """
    def __init__(self) -> None:
        self._operations: Dict[str, Operation] = {}
        self._register_default_operations()

    def _register_default_operations(self) -> None:
        self.register_operation("1", Add())
        self.register_operation("2", Subtract())
        self.register_operation("3", Divide())
        self.register_operation("4", Multiply())
        self.register_operation("5", Square())
        self.register_operation("6", Power())
        self.register_operation("7", SquareRoot())

    def register_operation(self, key: str, operation: Operation) -> None:
        self._operations[key] = operation

    @property
    def menu_items(self) -> Dict[str, Operation]:
        return self._operations

    def compute(self, key: str, a: float, b: float = None) -> float:
        if key not in self._operations:
            raise KeyError(f"Unknown operation key: {key}")
        operation = self._operations[key]
        
        # For unary operations, pass only the first number
        if operation.is_unary:
            return operation.execute(a)
        else:
            # For binary operations, pass both numbers
            return operation.execute(a, b)
```

### 3. Modified `calculator/__init__.py`

Export the new `SquareRoot` class:

```python
from .calculator import Calculator
from .operations import Operation, Add, Subtract, Divide, Multiply, Square, Power, SquareRoot

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Divide", "Multiply", "Square", "Power", "SquareRoot"]
```

### 4. Modified `app.py`

Update the UI to handle unary operations:

```python
from calculator import Calculator

def prompt_number(label: str) -> float:
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main() -> None:
    calc = Calculator()

    print("Simple OOP Calculator (Add, Subtract, Divide, Multiply, Square, Power & Square Root)")
    print("===================================================================================")

    while True:
        print("\nOptions:")
        for key, op in calc.menu_items.items():
            print(f"{key}. {op.name}")
        print("q. Exit")

        choice = input("Enter your choice: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Exiting... Goodbye!")
            break

        if choice not in calc.menu_items:
            print("Invalid choice! Try again.")
            continue

        operation = calc.menu_items[choice]
        
        # Prompt for the appropriate number of inputs
        a = prompt_number("first")
        
        if operation.is_unary:
            # For unary operations, only use the first number
            try:
                result = calc.compute(choice, a)
                print(f"Result: sqrt({a}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            # For binary operations, prompt for second number
            b = prompt_number("second")
            try:
                result = calc.compute(choice, a, b)
                print(f"Result: {a} {operation.symbol} {b} = {result}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

---

## Implementation Steps

### Step 1: Update `calculator/operations.py`
- Import the `math` module at the top: `import math`
- Add `symbol` attribute to the `Operation` ABC with default value `""`
- Add `is_unary` attribute to the `Operation` ABC with default value `False`
- Update all existing operation classes to include the `symbol` attribute
- Update the `execute` method signature to make `b` parameter optional: `def execute(self, a: float, b: float = None) -> float:`
- Add the new `SquareRoot` class with:
  - `name = "Square Root"`
  - `symbol = "sqrt"`
  - `is_unary = True`
  - Validation to check if `a >= 0` before computing square root
  - Implementation using `math.sqrt(a)`

### Step 2: Update `calculator/calculator.py`
- Import the `SquareRoot` class from operations
- Update the `compute` method to accept optional `b` parameter: `def compute(self, key: str, a: float, b: float = None) -> float:`
- Add logic to check if operation is unary:
  - If `operation.is_unary` is `True`, call `operation.execute(a)`
  - Otherwise, call `operation.execute(a, b)`
- Register the `SquareRoot` operation with key `"7"` in `_register_default_operations()`
- Update the docstring to mention support for unary operations

### Step 3: Update `calculator/__init__.py`
- Import `SquareRoot` from operations: `from .operations import ..., SquareRoot`
- Add `SquareRoot` to the `__all__` list

### Step 4: Update `app.py`
- Update the header comment to include "Square Root"
- Modify the main loop to check if the selected operation is unary
- If unary:
  - Prompt only for the first number
  - Call `calc.compute(choice, a)` without the second parameter
  - Display result as `sqrt(a) = result`
- If binary:
  - Prompt for both numbers (existing behavior)
  - Call `calc.compute(choice, a, b)`
  - Display result using the operation's symbol from the operation object

### Step 5: Testing
After implementation, test the following scenarios:
1. Square root of positive numbers (e.g., sqrt(4) = 2, sqrt(9) = 3, sqrt(16) = 4)
2. Square root of decimal numbers (e.g., sqrt(2) = 1.414...)
3. Square root of zero (sqrt(0) = 0)
4. Error handling for negative numbers (should display error message)
5. Verify existing operations (Add, Subtract, etc.) still work correctly
6. Verify menu displays all 7 operations correctly

---

## Benefits of This Implementation

1. **Extensibility**: The architecture now supports both unary and binary operations, making it easy to add other unary operations (e.g., absolute value, negation, factorial) or binary operations in the future.

2. **Maintainability**: The `is_unary` flag clearly indicates the nature of each operation, making the code self-documenting.

3. **User Experience**: The UI intelligently prompts for the correct number of inputs based on the operation type.

4. **Error Handling**: Proper validation for negative numbers in square root computation.

5. **Symbol Support**: Using the `symbol` attribute from the operation object eliminates hardcoded symbol logic in `app.py`.

6. **Backward Compatibility**: Existing operations continue to work without modification.

---

## Alternative Approach (Simpler but Less Flexible)

If you prefer a simpler implementation that doesn't refactor the architecture:

```python
# In operations.py - Add only:
class SquareRoot(Operation):
    name = "Square Root"

    def execute(self, a: float, b: float) -> float:
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return math.sqrt(a)

# In app.py - Modify the result display:
if op_name == "Square Root":
    print(f"Result: sqrt({a}) = {result}")
else:
    symbol = "+" if op_name == "Add" else (...)
    print(f"Result: {a} {symbol} {b} = {result}")
```

This simpler approach still requires the user to enter two numbers but only uses the first one. The recommended approach above is better as it provides a cleaner user experience.

---

## Summary

The square root functionality can be cleanly added to the calculator by:
1. Creating a new `SquareRoot` operation class
2. Extending the architecture to support unary operations
3. Updating the UI to handle single-input operations
4. Adding proper error handling for negative numbers

This implementation maintains the Strategy pattern, improves code maintainability, and sets up the foundation for adding other unary operations in the future.
