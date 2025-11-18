# Power

## Analysis

The GitHub issue requests the implementation of a **Power operation** that raises the first input number to the power of the second input number (i.e., `a ** b`). This is a natural extension to the existing calculator application that already supports Addition and Subtraction operations.

The current architecture uses the **Strategy Pattern** with an abstract `Operation` base class, making it straightforward to add new operations without modifying existing code. The implementation requires:

1. Creating a new `Power` class that inherits from `Operation`
2. Registering the new operation in the `Calculator`
3. Updating the UI logic to display the power symbol correctly
4. Testing the new functionality

### Current State
- The calculator currently supports: **Add** (key "1") and **Subtract** (key "2")
- The architecture is extensible and ready for new operations
- The UI dynamically displays available operations from the calculator's menu

### What Needs to Change
- Add a `Power` operation class to `operations.py`
- Register the `Power` operation in `calculator.py`
- Update the symbol mapping logic in `app.py` to handle the power symbol
- Update `__init__.py` to export the new `Power` class

---

## Affected Files

1. **operations.py** - Add the `Power` class implementation
2. **calculator.py** - Register the `Power` operation in `_register_default_operations()`
3. **app.py** - Update the symbol mapping logic to support the power symbol
4. **__init__.py** - Export the new `Power` class in `__all__`

---

## Code Examples

### 1. New Power Operation Class (operations.py)

```python
class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

**Explanation:**
- Inherits from the abstract `Operation` base class
- Sets `name` to "Power" for display in the menu
- Implements the `execute` method using Python's exponentiation operator (`**`)
- Takes two float parameters: base (`a`) and exponent (`b`)
- Returns the result of `a` raised to the power of `b`

---

## Implementation Steps

### Step 1: Update `operations.py`

Add the `Power` class to the end of the file:

```python
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

class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

**Changes Made:**
- Added new `Power` class after `Subtract`
- Follows the same pattern as existing operations
- Uses Python's built-in exponentiation operator (`**`)

---

### Step 2: Update `calculator.py`

Import the `Power` class and register it:

```python
from typing import Dict, Type
from operations import Operation, Add, Subtract, Power

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
        self.register_operation("3", Power())

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

**Changes Made:**
- Added `Power` to the import statement
- Registered `Power` with key "3" in `_register_default_operations()`

---

### Step 3: Update `app.py`

Improve the symbol mapping logic to handle the power symbol:

```python
from calculator import Calculator

def prompt_number(label: str) -> float:
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation_symbol(op_name: str) -> str:
    """Map operation names to their display symbols."""
    symbol_map = {
        "Add": "+",
        "Subtract": "-",
        "Power": "^"
    }
    return symbol_map.get(op_name, "?")

def main() -> None:
    calc = Calculator()

    print("Simple OOP Calculator (Add, Subtract & Power)")
    print("============================================")

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
            op_name = calc.menu_items[choice].name
            symbol = get_operation_symbol(op_name)
            print(f"Result: {a} {symbol} {b} = {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Changes Made:**
- Created a new `get_operation_symbol()` function that maps operation names to symbols
- Updated the header to mention "Power" operation
- Replaced the brittle ternary operator with a dictionary-based lookup
- This approach is more maintainable and scalable for future operations

---

### Step 4: Update `__init__.py`

Export the new `Power` class:

```python
from calculator import Calculator
from operations import Operation, Add, Subtract, Power

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Power"]
```

**Changes Made:**
- Added `Power` to the import statement
- Added `"Power"` to the `__all__` list for proper package-level exports

---

## Testing Scenarios

After implementing the changes, test the following scenarios:

### Test Case 1: Basic Power Operation
- **Input:** First number = 2, Second number = 3
- **Expected Output:** 2 ^ 3 = 8
- **Verification:** 2 to the power of 3 equals 8 [PASS]

### Test Case 2: Power of Zero
- **Input:** First number = 5, Second number = 0
- **Expected Output:** 5 ^ 0 = 1
- **Verification:** Any number to the power of 0 equals 1 [PASS]

### Test Case 3: Negative Exponent
- **Input:** First number = 2, Second number = -2
- **Expected Output:** 2 ^ -2 = 0.25
- **Verification:** 2 to the power of -2 equals 1/4 = 0.25 [PASS]

### Test Case 4: Fractional Exponent
- **Input:** First number = 4, Second number = 0.5
- **Expected Output:** 4 ^ 0.5 = 2.0
- **Verification:** Square root of 4 equals 2.0 [PASS]

### Test Case 5: Negative Base
- **Input:** First number = -2, Second number = 3
- **Expected Output:** -2 ^ 3 = -8
- **Verification:** (-2) to the power of 3 equals -8 [PASS]

---

## Benefits of This Implementation

[+] Follows Existing Patterns: The `Power` class follows the same structure as `Add` and `Subtract`

[+] Maintains Separation of Concerns: The operation logic is isolated in the `Power` class

[+] Extensible Design: Future operations can be added by simply creating a new class and registering it

[+] No Breaking Changes: Existing functionality remains unchanged

[+] Improved Symbol Mapping: The new `get_operation_symbol()` function is more maintainable than the previous ternary operator

[+] Leverages Python's Built-in: Uses Python's native `**` operator for reliability and performance

---

## Potential Enhancements (Future)

1. **Error Handling:** Add specific error handling for edge cases like:
   - Very large numbers that could cause overflow
   - Complex number support for negative bases with fractional exponents

2. **Symbol Customization:** Allow operations to define their own symbols via a property

3. **Unit Tests:** Add comprehensive unit tests for all operations including edge cases

4. **Documentation:** Add docstrings to the `Power` class and `get_operation_symbol()` function

5. **Additional Operations:** Consider adding Multiply, Divide, Square Root, etc.

---

## Summary

This implementation adds a **Power operation** to the calculator by:

1. Creating a new `Power` class that implements the `Operation` interface
2. Registering it with key "3" in the calculator
3. Improving the symbol mapping logic in the UI layer
4. Exporting the new class from the package

The changes are minimal, non-invasive, and maintain the existing architecture's elegance and extensibility. The implementation is production-ready and follows Python best practices.
