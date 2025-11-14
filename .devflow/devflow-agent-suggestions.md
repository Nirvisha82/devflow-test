# Square Root Feature Implementation

## Analysis

The issue requests adding a **Square Root** operation to the calculator application. The feature should:
1. Calculate the square root of both input numbers
2. Validate that both numbers are positive (non-negative)
3. Throw an error if either number is negative

This aligns perfectly with the existing **Strategy Pattern** architecture where new operations are implemented as concrete `Operation` classes. The current codebase already has infrastructure for `Divide` and `Multiply` operations, so adding `SquareRoot` follows the same pattern.

### Current State
- The calculator supports: Add, Subtract, Multiply, Divide
- Operations are registered with keys "1", "2", "3", "4"
- The `Operation` ABC defines the interface for all operations
- Input validation occurs in `app.py` via `prompt_number()` function

### Implementation Approach
The Square Root operation differs from binary operations (Add, Subtract, etc.) as it conceptually operates on a single number. However, the issue specifies "square root of both input numbers", so we'll implement it to:
- Accept two numbers from the user
- Calculate square root of each
- Return the results appropriately
- Validate both numbers are non-negative before computation

## Affected Files

1. **`calculator/operations.py`** - Add new `SquareRoot` class
2. **`calculator/calculator.py`** - Register the new operation (update import)
3. **`calculator/__init__.py`** - Export the new `SquareRoot` class
4. **`app.py`** - Update symbol mapping for display
5. **`README.md`** - Update documentation to include Square Root

## Code Examples

### Example 1: SquareRoot Operation Class
```python
import math
from abc import ABC, abstractmethod

class SquareRoot(Operation):
    name = "Square Root"
    
    def execute(self, a: float, b: float) -> tuple:
        """
        Calculate square root of both input numbers.
        
        Args:
            a: First number (must be non-negative)
            b: Second number (must be non-negative)
            
        Returns:
            Tuple of (sqrt(a), sqrt(b))
            
        Raises:
            ValueError: If either number is negative
        """
        if a < 0 or b < 0:
            raise ValueError(f"Cannot calculate square root of negative numbers. Got a={a}, b={b}")
        
        return (math.sqrt(a), math.sqrt(b))
```

### Example 2: Updated Calculator Registration
```python
from .operations import Operation, Add, Subtract, Multiply, Divide, SquareRoot

class Calculator:
    def _register_default_operations(self) -> None:
        self.register_operation("1", Add())
        self.register_operation("2", Subtract())
        self.register_operation("3", Multiply())
        self.register_operation("4", Divide())
        self.register_operation("5", SquareRoot())
```

### Example 3: Updated Symbol Mapping in app.py
```python
# Enhanced symbol mapping
symbol_map = {
    "Add": "+",
    "Subtract": "-",
    "Multiply": "*",
    "Divide": "/",
    "Square Root": "sqrt"
}

try:
    result = calc.compute(choice, a, b)
    op_name = calc.menu_items[choice].name
    symbol = symbol_map.get(op_name, "?")
    
    # Handle tuple return for Square Root
    if isinstance(result, tuple):
        sqrt_a, sqrt_b = result
        print(f"Result: sqrt({a}) = {sqrt_a:.4f}, sqrt({b}) = {sqrt_b:.4f}")
    else:
        print(f"Result: {a} {symbol} {b} = {result}")
except ValueError as e:
    print(f"Validation Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

## Implementation Steps

### Step 1: Update `calculator/operations.py`
Add the `SquareRoot` class at the end of the file:

```python
import math

class SquareRoot(Operation):
    name = "Square Root"

    def execute(self, a: float, b: float) -> tuple:
        """
        Calculate square root of both input numbers.
        Validates that both numbers are non-negative.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Tuple containing (sqrt(a), sqrt(b))
            
        Raises:
            ValueError: If either number is negative
        """
        if a < 0 or b < 0:
            raise ValueError(
                f"Square root requires non-negative numbers. "
                f"Received: a={a}, b={b}"
            )
        
        return (math.sqrt(a), math.sqrt(b))
```

**Key Points:**
- Import `math` module for `sqrt()` function
- Implement validation before calculation
- Return tuple of results for both numbers
- Provide clear error message for negative inputs

### Step 2: Update `calculator/calculator.py`
Modify the imports and registration:

```python
from typing import Dict, Type, Union, Tuple
from .operations import Operation, Add, Subtract, Multiply, Divide, SquareRoot

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
        self.register_operation("3", Multiply())
        self.register_operation("4", Divide())
        self.register_operation("5", SquareRoot())

    def register_operation(self, key: str, operation: Operation) -> None:
        self._operations[key] = operation

    @property
    def menu_items(self) -> Dict[str, Operation]:
        return self._operations

    def compute(self, key: str, a: float, b: float) -> Union[float, Tuple[float, float]]:
        if key not in self._operations:
            raise KeyError(f"Unknown operation key: {key}")
        return self._operations[key].execute(a, b)
```

**Key Points:**
- Add `SquareRoot` to imports
- Register with key "5"
- Update return type hint to `Union[float, Tuple[float, float]]` to reflect variable return types

### Step 3: Update `calculator/__init__.py`
Export the new `SquareRoot` class:

```python
from .calculator import Calculator
from .operations import Operation, Add, Subtract, Multiply, Divide, SquareRoot

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Multiply", "Divide", "SquareRoot"]
```

### Step 4: Update `app.py`
Enhance the UI to handle the new operation:

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

    print("Simple OOP Calculator (Add, Subtract, Multiply, Divide & Square Root)")
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
            op_name = calc.menu_items[choice].name
            
            # Symbol mapping for operations
            symbol_map = {
                "Add": "+",
                "Subtract": "-",
                "Multiply": "*",
                "Divide": "/",
                "Square Root": "sqrt"
            }
            symbol = symbol_map.get(op_name, "?")
            
            # Handle different return types
            if isinstance(result, tuple):
                # Square Root returns tuple of two values
                sqrt_a, sqrt_b = result
                print(f"Result: sqrt({a}) = {sqrt_a:.4f}, sqrt({b}) = {sqrt_b:.4f}")
            else:
                # Other operations return single float
                print(f"Result: {a} {symbol} {b} = {result}")
                
        except ValueError as e:
            print(f"Validation Error: {e}")
        except ZeroDivisionError as e:
            print(f"Math Error: Cannot divide by zero")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Key Points:**
- Create `symbol_map` dictionary for cleaner symbol management
- Check if result is a tuple (Square Root) vs single float
- Format Square Root output with "sqrt" notation
- Add specific error handling for `ValueError` (validation errors)
- Add specific handling for `ZeroDivisionError`

### Step 5: Update `README.md`
Update documentation to include the new feature:

```markdown
# devflow-test

Test Calculator app using python for DevFlow Agent.

The app supports following operations:
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Square Root

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract second number from first
- **Multiplication**: Multiply two numbers
- **Division**: Divide first number by second (with zero-check)
- **Square Root**: Calculate square root of both input numbers
  - Validates that both numbers are non-negative
  - Returns error if negative numbers are provided
  - Displays results with 4 decimal places

## Usage

Run the application:
```bash
python app.py
```

Follow the on-screen menu to select an operation and enter two numbers.

## Error Handling

- **Negative numbers for Square Root**: The application will display a validation error message
- **Division by zero**: The application will display an appropriate error message
- **Invalid input**: Non-numeric inputs are rejected with a prompt to re-enter
```

## Testing Recommendations

### Test Case 1: Valid Square Root Inputs
```
Input: a = 16, b = 25
Expected Output: Result: sqrt(16) = 4.0000, sqrt(25) = 5.0000
```

### Test Case 2: Negative Number Validation
```
Input: a = -4, b = 9
Expected Output: Validation Error: Square root requires non-negative numbers. Received: a=-4, b=9
```

### Test Case 3: Zero Input
```
Input: a = 0, b = 4
Expected Output: Result: sqrt(0) = 0.0000, sqrt(4) = 2.0000
```

### Test Case 4: Decimal Inputs
```
Input: a = 2.25, b = 6.25
Expected Output: Result: sqrt(2.25) = 1.5000, sqrt(6.25) = 2.5000
```

### Test Case 5: Large Numbers
```
Input: a = 10000, b = 1000000
Expected Output: Result: sqrt(10000) = 100.0000, sqrt(1000000) = 1000.0000
```

## Design Rationale

1. **Tuple Return Type**: The Square Root operation returns a tuple `(sqrt(a), sqrt(b))` to handle the requirement of calculating square root for both input numbers while maintaining consistency with the existing binary operation interface.

2. **Validation at Operation Level**: Input validation (checking for negative numbers) is performed in the `SquareRoot.execute()` method, following the principle of encapsulation and keeping validation logic close to the business logic.

3. **Error Messages**: Clear, descriptive error messages help users understand why their input was rejected.

4. **Symbol Mapping Dictionary**: Moving to a dictionary-based symbol mapping makes the code more maintainable and scalable for future operations.

5. **Type Hints**: Updated type hints in `Calculator.compute()` reflect the variable return types, improving code clarity and enabling better IDE support.

## Additional Considerations

### Future Enhancements
- Consider adding a `symbol` attribute to the `Operation` ABC to further decouple the UI from operation details
- Implement a configuration file for operation registration instead of hardcoding in `_register_default_operations()`
- Add logging for debugging and monitoring
- Create unit tests for the new `SquareRoot` operation

### Edge Cases Handled
- Negative numbers: Raises ValueError
- Zero: Returns 0.0
- Decimal numbers: Properly calculated
- Large numbers: No overflow issues with Python's float handling

### Backward Compatibility
- Existing operations (Add, Subtract, Multiply, Divide) remain unchanged
- Menu system automatically includes new operation
- No breaking changes to public API

## Summary of Changes

| File | Changes |
|------|---------|
| `calculator/operations.py` | Add `SquareRoot` class with validation logic |
| `calculator/calculator.py` | Import `SquareRoot`, register in `_register_default_operations()`, update return type hint |
| `calculator/__init__.py` | Export `SquareRoot` class |
| `app.py` | Add symbol mapping dictionary, handle tuple returns, enhance error handling |
| `README.md` | Document new Square Root feature and usage |

All changes follow the existing Strategy Pattern architecture and maintain backward compatibility with existing operations.
