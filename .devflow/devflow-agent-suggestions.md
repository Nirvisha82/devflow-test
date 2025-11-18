# Power

## Analysis

The GitHub issue requests adding a **Power** feature to the calculator that raises the first input number to the power of the second input number (i.e., `a ** b`).

### Current State
The calculator application already follows a well-designed **Strategy pattern** with:
- An abstract `Operation` base class defining the interface
- Concrete operation classes: `Add`, `Subtract`, `Multiply`, and `Divide`
- A `Calculator` class that manages and dispatches operations
- An `app.py` CLI interface that displays the menu and processes user input

### Implementation Approach
To add the Power feature, we need to:
1. Create a new `Power` operation class in `operations.py`
2. Register the Power operation in `calculator.py`
3. Update the symbol mapping in `app.py` to support the Power operator
4. Update `__init__.py` to export the new `Power` class

This approach maintains the existing architecture and follows the established patterns.

---

## Affected Files

1. **`operations.py`** - Add the `Power` class
2. **`calculator.py`** - Register the Power operation
3. **`app.py`** - Add Power symbol to the symbols dictionary
4. **`__init__.py`** - Export the new Power class

---

## Code Examples

### Example 1: Power Operation Class
```python
class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

### Example 2: Registering Power in Calculator
```python
def _register_default_operations(self) -> None:
    self.register_operation("1", Add())
    self.register_operation("2", Subtract())
    self.register_operation("3", Multiply())
    self.register_operation("4", Divide())
    self.register_operation("5", Power())  # NEW LINE
```

### Example 3: Symbol Mapping Update
```python
symbols = {
    "Add": "+",
    "Subtract": "-",
    "Multiply": "*",
    "Divide": "/",
    "Power": "^"  # NEW LINE
}
```

### Example 4: Expected User Interaction
```
Options:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
q. Exit
Enter your choice: 5
Enter first number: 2
Enter second number: 3
Result: 2 ^ 3 = 8.0
```

---

## Implementation Steps

### Step 1: Update `operations.py`
Add the `Power` class after the `Divide` class:

```python
class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

**Why**: This creates a new operation following the established `Operation` interface pattern. The `execute` method uses Python's exponentiation operator (`**`) to raise `a` to the power of `b`.

---

### Step 2: Update `calculator.py`
Modify the imports and registration method:

**Update the import statement:**
```python
from operations import Operation, Add, Subtract, Multiply, Divide, Power
```

**Update the `_register_default_operations` method:**
```python
def _register_default_operations(self) -> None:
    self.register_operation("1", Add())
    self.register_operation("2", Subtract())
    self.register_operation("3", Multiply())
    self.register_operation("4", Divide())
    self.register_operation("5", Power())
```

**Why**: This registers the Power operation with key "5" in the calculator's operation registry, making it available for use through the CLI menu.

---

### Step 3: Update `app.py`
Modify the symbols dictionary in the `main()` function:

**Update the symbols dictionary:**
```python
symbols = {
    "Add": "+",
    "Subtract": "-",
    "Multiply": "*",
    "Divide": "/",
    "Power": "^"
}
```

**Why**: This ensures that when a Power operation is performed, the result is displayed with the `^` symbol (e.g., "2 ^ 3 = 8.0"), making the output clear and consistent with mathematical notation.

---

### Step 4: Update `__init__.py`
Add `Power` to the imports and `__all__` list:

```python
from .calculator import Calculator
from .operations import Operation, Add, Subtract, Multiply, Divide, Power

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Multiply", "Divide", "Power"]
```

**Why**: This exposes the `Power` class as part of the package's public API, maintaining consistency with how other operations are exported and allowing external code to import and use the Power operation if needed.

---

## Testing Recommendations

### Test Cases to Verify

1. **Basic Power Operations**
   - Test: `2 ^ 3` should return `8.0`
   - Test: `5 ^ 2` should return `25.0`
   - Test: `10 ^ 0` should return `1.0`

2. **Fractional Exponents**
   - Test: `4 ^ 0.5` should return `2.0` (square root)
   - Test: `8 ^ (1/3)` should return `2.0` (cube root)

3. **Negative Exponents**
   - Test: `2 ^ -1` should return `0.5`
   - Test: `10 ^ -2` should return `0.01`

4. **Edge Cases**
   - Test: `0 ^ 0` should return `1.0` (Python's behavior)
   - Test: Negative base with integer exponent (e.g., `-2 ^ 3` should return `-8.0`)

5. **Menu Integration**
   - Verify that option "5" appears in the menu
   - Verify that the Power operation is correctly executed when selected
   - Verify that the result displays with the `^` symbol

---

## Additional Considerations

### Design Pattern Compliance
[OK] The implementation maintains the **Strategy pattern** established in the codebase:
- `Power` is a concrete strategy implementing the `Operation` interface
- The `Calculator` context remains unchanged in its core logic
- The CLI (`app.py`) remains decoupled from specific operation implementations

### Error Handling
The current implementation does not include specific error handling for Power operations. Consider these scenarios:
- **Very large exponents**: Python can handle large numbers, but computation may be slow
- **Complex numbers**: Negative bases with fractional exponents result in complex numbers, which the current `float` return type cannot represent

For the current scope, these edge cases are acceptable as they align with Python's standard behavior.

### Future Extensibility
This implementation maintains the extensibility of the calculator:
- New operations can be added by creating new `Operation` subclasses
- The symbol mapping in `app.py` is centralized and easy to update
- No changes to core `Calculator` logic are needed for new operations

---

## Summary

The Power feature can be implemented with minimal changes across 4 files:
1. **`operations.py`**: Add the `Power` class (4 lines)
2. **`calculator.py`**: Import `Power` and register it (2 lines modified)
3. **`app.py`**: Add Power symbol mapping (1 line)
4. **`__init__.py`**: Export `Power` class (2 lines modified)

Total: ~9 lines of code added/modified, maintaining full architectural consistency with the existing codebase.
