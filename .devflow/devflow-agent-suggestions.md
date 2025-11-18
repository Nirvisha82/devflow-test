# Power

## Analysis

The GitHub issue requests adding functionality to raise one input number to the power of another. This is a natural extension to the existing calculator application, which already implements the Strategy design pattern for operations (Add, Subtract, Multiply, Divide).

The current codebase is well-structured with:
- An abstract `Operation` base class that defines the interface for all operations
- Concrete operation implementations (Add, Subtract, Multiply, Divide)
- A `Calculator` class that manages and delegates to operations
- A CLI interface in `app.py` that displays menu options and handles user interaction

To implement the Power functionality, we need to:
1. Create a new `Power` operation class that implements the `Operation` interface
2. Register the Power operation in the Calculator's default operations
3. Export the Power class from the package
4. Update the CLI to handle the Power operation symbol display

## Affected Files

1. **calculator/operations.py** - Add the `Power` class
2. **calculator/calculator.py** - Register Power operation in `_register_default_operations()`
3. **calculator/__init__.py** - Export the `Power` class
4. **app.py** - Add Power symbol handling in the result display logic

## Code Examples

### Example 1: Power Operation Class
The Power operation should follow the same pattern as existing operations:

```python
class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

This implementation:
- Inherits from `Operation` abstract base class
- Sets the `name` attribute to "Power"
- Implements the `execute` method using Python's exponentiation operator (`**`)
- Returns a float result
- Handles both integer and float bases/exponents

### Example 2: Registering Power in Calculator
Update the `_register_default_operations()` method:

```python
def _register_default_operations(self) -> None:
    self.register_operation("1", Add())
    self.register_operation("2", Subtract())
    self.register_operation("3", Multiply())
    self.register_operation("4", Divide())
    self.register_operation("5", Power())
```

### Example 3: CLI Symbol Handling
Update the result display logic in `app.py`:

```python
try:
    result = calc.compute(choice, a, b)
    op_name = calc.menu_items[choice].name
    if op_name == "Add":
        symbol = "+"
    elif op_name == "Subtract":
        symbol = "-"
    elif op_name == "Multiply":
        symbol = "*"
    elif op_name == "Divide":
        symbol = "/"
    elif op_name == "Power":
        symbol = "^"
    print(f"Result: {a} {symbol} {b} = {result}")
except Exception as e:
    print(f"Error: {e}")
```

## Implementation Steps

### Step 1: Add Power Class to calculator/operations.py
Add the following class definition to the end of the `operations.py` file:

```python
class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

**Rationale**: This follows the established pattern for all other operations and integrates seamlessly with the Strategy pattern used throughout the codebase.

### Step 2: Register Power in calculator/calculator.py
Update the `_register_default_operations()` method to include:

```python
self.register_operation("5", Power())
```

Add this line after the Divide registration. The complete method should look like:

```python
def _register_default_operations(self) -> None:
    self.register_operation("1", Add())
    self.register_operation("2", Subtract())
    self.register_operation("3", Multiply())
    self.register_operation("4", Divide())
    self.register_operation("5", Power())
```

**Rationale**: This registers the Power operation with key "5" (following the sequential pattern) and makes it available through the Calculator's menu.

### Step 3: Update Package Exports in calculator/__init__.py
Update the import statement and `__all__` list:

```python
from .calculator import Calculator
from .operations import Operation, Add, Subtract, Multiply, Divide, Power

__all__ = ["Calculator", "Operation", "Add", "Subtract", "Multiply", "Divide", "Power"]
```

**Rationale**: This exposes the Power class as part of the public API of the calculator package, maintaining consistency with how other operations are exported.

### Step 4: Update CLI Symbol Handling in app.py
Modify the result display section to handle the Power operation:

```python
try:
    result = calc.compute(choice, a, b)
    op_name = calc.menu_items[choice].name
    if op_name == "Add":
        symbol = "+"
    elif op_name == "Subtract":
        symbol = "-"
    elif op_name == "Multiply":
        symbol = "*"
    elif op_name == "Divide":
        symbol = "/"
    elif op_name == "Power":
        symbol = "^"
    print(f"Result: {a} {symbol} {b} = {result}")
except Exception as e:
    print(f"Error: {e}")
```

**Rationale**: This ensures that when the Power operation is selected, the result is displayed with the caret symbol (^) to represent exponentiation, making the output user-friendly and mathematically clear.

## Testing Recommendations

### Unit Tests
1. **Test basic power operations**:
   - `Power().execute(2, 3)` should return `8.0`
   - `Power().execute(5, 2)` should return `25.0`
   - `Power().execute(10, 0)` should return `1.0`

2. **Test edge cases**:
   - `Power().execute(0, 0)` should return `1.0` (Python's behavior)
   - `Power().execute(2, -1)` should return `0.5`
   - `Power().execute(2.5, 2)` should return `6.25`

3. **Test Calculator integration**:
   - `calc.compute("5", 2, 3)` should return `8.0`
   - Verify that "5" is in `calc.menu_items`
   - Verify that `calc.menu_items["5"].name` equals "Power"

### Manual Testing
1. Run the application and verify that option "5. Power" appears in the menu
2. Test with various inputs:
   - Positive integers: `2 ^ 3 = 8`
   - Positive floats: `2.5 ^ 2 = 6.25`
   - Negative exponents: `2 ^ -1 = 0.5`
   - Zero exponent: `5 ^ 0 = 1`
3. Verify the output format displays correctly with the `^` symbol

## Benefits

[+] Minimal Code Changes: Only 4 lines of new code in operations.py, plus updates to imports and registration
[+] Consistent Design: Follows the existing Strategy pattern and code conventions
[+] Extensible: Future operations can be added using the same approach
[+] User-Friendly: Clear menu display and intuitive symbol representation
[+] No Breaking Changes: Existing functionality remains unchanged
[+] Type-Safe: Maintains type hints and Python best practices

## Potential Considerations

### Edge Cases
- **Very large exponents**: May result in `OverflowError` for large bases (e.g., `1000 ** 1000`). Consider adding error handling if needed.
- **Negative base with fractional exponent**: May result in complex numbers. Python will raise a `ValueError` in this case, which will be caught by the existing exception handler in `app.py`.

### Future Enhancements
- Add input validation to prevent overflow errors
- Add support for more mathematical operations (sqrt, log, etc.)
- Consider using a more scalable approach for operation registration (e.g., configuration file or plugin system)

## Summary

Implementing the Power functionality is straightforward given the well-designed architecture of the calculator application. By creating a new `Power` class that implements the `Operation` interface, registering it in the `Calculator`, and updating the CLI to display the appropriate symbol, we can add this feature with minimal changes and maximum consistency with the existing codebase.
