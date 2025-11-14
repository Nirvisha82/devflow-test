# Add a feature to divide

## Analysis

The GitHub issue requests adding a divide feature to divide two input numbers. Based on the repository analysis, this is a well-structured CLI calculator application using the **Strategy design pattern**. The current implementation supports `Add` and `Subtract` operations, but the `app.py` file references additional operations (`Divide`, `Multiply`, `Square`) that are not yet implemented.

### Current State
- [DONE] Architecture: Modular and extensible design with `Operation` abstract base class
- [DONE] Pattern: Strategy pattern allows easy addition of new operations
- [TODO] Missing: `Divide` operation implementation
- [ISSUE] Issue: The `__init__.py` exports operations that don't exist yet
- [ISSUE] Issue: `app.py` has hardcoded symbol logic that doesn't scale well

### What Needs to Be Done
1. Implement `Divide` operation class in `operations.py`
2. Register the `Divide` operation in `Calculator._register_default_operations()`
3. Update `calculator/__init__.py` to include `Divide` in exports
4. Enhance the `Operation` ABC with a `symbol` attribute to eliminate hardcoded logic in `app.py`
5. Update `app.py` to use the `symbol` attribute from operations
6. Add error handling for division by zero

---

## Affected Files

1. **`calculator/operations.py`** - Add `Divide` class and update `Operation` ABC
2. **`calculator/calculator.py`** - Register the new `Divide` operation
3. **`calculator/__init__.py`** - Export the `Divide` class
4. **`app.py`** - Use symbol attribute instead of hardcoded logic

---

## Code Examples

### Example 1: Division Operation
```python
class Divide(Operation):
    name = "Divide"
    symbol = "/"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
```

### Example 2: Updated Operation ABC
```python
class Operation(ABC):
    name: str
    symbol: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...
```

### Example 3: Symbol-Based Display
```python
# Instead of:
symbol = "+" if op_name == "Add" else ("-" if op_name == "Subtract" else ...)

# Use:
op_symbol = calc.menu_items[choice].symbol
print(f"Result: {a} {op_symbol} {b} = {result}")
```

---

## Implementation Steps

### Step 1: Update the `Operation` Abstract Base Class
**File**: `calculator/operations.py`

Add a `symbol` attribute to the `Operation` ABC to store the mathematical symbol for each operation. This eliminates the need for hardcoded symbol logic in `app.py`.

```python
from abc import ABC, abstractmethod

class Operation(ABC):
    name: str
    symbol: str  # NEW: Add symbol attribute

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...
```

### Step 2: Add Symbol Attributes to Existing Operations
**File**: `calculator/operations.py`

Update the `Add` and `Subtract` classes to include the `symbol` attribute:

```python
class Add(Operation):
    name = "Add"
    symbol = "+"  # NEW

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"
    symbol = "-"  # NEW

    def execute(self, a: float, b: float) -> float:
        return a - b
```

### Step 3: Implement the `Divide` Operation Class
**File**: `calculator/operations.py`

Add a new `Divide` class that implements division with error handling for division by zero:

```python
class Divide(Operation):
    name = "Divide"
    symbol = "/"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
```

### Step 4: Register the `Divide` Operation
**File**: `calculator/calculator.py`

Update the `_register_default_operations()` method to register the new `Divide` operation:

```python
def _register_default_operations(self) -> None:
    self.register_operation("1", Add())
    self.register_operation("2", Subtract())
    self.register_operation("3", Divide())  # NEW
```

### Step 5: Update Package Exports
**File**: `calculator/__init__.py`

Update the imports and `__all__` list to include the `Divide` class:

```python
from .calculator import Calculator
from .operations import Operation, Add, Subtract, Divide  # NEW: Add Divide

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Divide"]
```

### Step 6: Simplify Symbol Logic in `app.py`
**File**: `app.py`

Replace the hardcoded symbol logic with a dynamic approach using the `symbol` attribute from the operation object:

**Before**:
```python
op_name = calc.menu_items[choice].name
symbol = "+" if op_name == "Add" else ("-" if op_name == "Subtract" else ("/" if op_name == "Divide" else ("*" if op_name == "Multiply" else ("^2" if op_name == "Square" else "^"))))
print(f"Result: {a} {symbol} {b} = {result}")
```

**After**:
```python
op_symbol = calc.menu_items[choice].symbol
print(f"Result: {a} {op_symbol} {b} = {result}")
```

### Step 7: Update the Print Statement (Complete Context)
**File**: `app.py`

Update the entire try-except block to use the new symbol approach:

```python
try:
    result = calc.compute(choice, a, b)
    op_symbol = calc.menu_items[choice].symbol
    print(f"Result: {a} {op_symbol} {b} = {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

---

## Complete File Changes

### File: `calculator/operations.py` (Complete Updated Content)
```python
from abc import ABC, abstractmethod

class Operation(ABC):
    name: str
    symbol: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...

class Add(Operation):
    name = "Add"
    symbol = "+"

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"
    symbol = "-"

    def execute(self, a: float, b: float) -> float:
        return a - b

class Divide(Operation):
    name = "Divide"
    symbol = "/"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
```

### File: `calculator/calculator.py` (Complete Updated Content)
```python
from typing import Dict, Type
from .operations import Operation, Add, Subtract, Divide

class Calculator:
    """
    Simple OOP calculator that delegates to Operation objects.
    You can register new operations without changing the UI.
    """
    def __init__(self) -> None:
        self._operations: Dict[str, Operation] = {}
        self._register_default_operations()

    def _register_default_operations(self) -> None:
        self.register_operation("1", Add())
        self.register_operation("2", Subtract())
        self.register_operation("3", Divide())

    def register_operation(self, key: str, operation: Operation) -> None:
        self._operations[key] = operation

    @property
    def menu_items(self) -> Dict[str, Operation]:
        return self._operations

    def compute(self, key: str, a: float, b: float) -> float:
        if key not in self._operations:
            raise KeyError(f"Unknown operation key: {key}")
        return self._operations[key].execute(a, b)
```

### File: `calculator/__init__.py` (Complete Updated Content)
```python
from .calculator import Calculator
from .operations import Operation, Add, Subtract, Divide

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Divide"]
```

### File: `app.py` (Complete Updated Content)
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

    print("Simple OOP Calculator (Add, Subtract, Divide)")
    print("======================================")

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

        a = prompt_number("first")
        b = prompt_number("second")

        try:
            result = calc.compute(choice, a, b)
            op_symbol = calc.menu_items[choice].symbol
            print(f"Result: {a} {op_symbol} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

---

## Testing Recommendations

### Test Case 1: Basic Division
```
Input: 10 / 2
Expected Output: Result: 10.0 / 2.0 = 5.0
```

### Test Case 2: Division by Zero
```
Input: 10 / 0
Expected Output: Error: Cannot divide by zero!
```

### Test Case 3: Decimal Division
```
Input: 7.5 / 2.5
Expected Output: Result: 7.5 / 2.5 = 3.0
```

### Test Case 4: Negative Numbers
```
Input: -10 / 2
Expected Output: Result: -10.0 / 2.0 = -5.0
```

### Test Case 5: Menu Display
```
Expected Output should show:
1. Add
2. Subtract
3. Divide
q. Exit
```

---

## Benefits of This Implementation

[PASS] Follows Strategy Pattern: Maintains the existing design pattern for easy extensibility
[PASS] Error Handling: Includes division by zero validation
[PASS] Code Reusability: Symbol attribute eliminates hardcoded logic
[PASS] Scalability: Easy to add more operations (Multiply, Square, etc.) in the future
[PASS] Maintainability: Clean, readable code with consistent structure
[PASS] Type Safety: Maintains type hints throughout
[PASS] Backward Compatible: Existing Add and Subtract operations continue to work

---

## Future Enhancements

For future iterations, consider implementing:
1. **Multiply Operation** - Similar structure to Divide
2. **Square Operation** - For squaring a single number (may need to modify interface)
3. **Power Operation** - For raising to a power
4. **Modulo Operation** - For remainder calculations
5. **Input Validation** - Range checks, precision limits
6. **History Feature** - Track previous calculations
7. **Configuration File** - Load operations from external config

---

## Key Changes Summary

### What Changed:
1. Added `symbol` attribute to `Operation` ABC
2. Added symbol values to `Add` and `Subtract` classes
3. Implemented new `Divide` class with division by zero error handling
4. Registered `Divide` operation in Calculator
5. Updated package exports in `__init__.py`
6. Simplified symbol logic in `app.py` to use dynamic symbol attribute
7. Improved error handling for division operations

### Why These Changes:
- **Maintainability**: Removes hardcoded symbol logic, making the code more maintainable
- **Extensibility**: Makes it trivial to add new operations without modifying `app.py`
- **Robustness**: Includes proper error handling for division by zero
- **Consistency**: Follows the existing Strategy pattern and code style
- **Type Safety**: Maintains Python type hints throughout

---

## Implementation Order

1. First, update `calculator/operations.py` with symbol attributes and Divide class
2. Then, update `calculator/calculator.py` to register Divide
3. Next, update `calculator/__init__.py` to export Divide
4. Finally, update `app.py` to use the symbol attribute

This order ensures that each file builds on the previous changes and maintains consistency.
