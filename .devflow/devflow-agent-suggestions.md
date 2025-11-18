# Power

## Analysis

The GitHub issue requests the implementation of a **Power operation** that raises one input number to the power of the second input number. This feature should be integrated into the existing calculator application, which uses the Strategy pattern to manage different arithmetic operations.

### Current State
The calculator currently supports:
- **Add** (key "1"): Adds two numbers
- **Subtract** (key "2"): Subtracts the second number from the first

### Required Changes
To implement the Power operation, we need to:
1. Create a new `Power` class in `operations.py` that inherits from `Operation`
2. Register the new operation in `calculator.py`
3. Update the UI logic in `app.py` to handle the power symbol display
4. Update `__init__.py` to export the new `Power` class

### Design Pattern Alignment
The implementation follows the existing **Strategy Pattern**, ensuring consistency with the current architecture. The `Power` class will be a concrete strategy that implements the `Operation` interface.

---

## Affected Files

1. **operations.py** - Add the `Power` class
2. **calculator.py** - Register the Power operation in `_register_default_operations()`
3. **app.py** - Update symbol logic to handle power display
4. **__init__.py** - Export the new `Power` class

---

## Code Examples

### Example 1: Power Operation Usage
```python
# User selects option "3" for Power
# Enters first number: 2
# Enters second number: 3
# Result: 2 ^ 3 = 8
```

### Example 2: Power with Decimal Numbers
```python
# User selects option "3" for Power
# Enters first number: 2.5
# Enters second number: 2
# Result: 2.5 ^ 2 = 6.25
```

### Example 3: Power with Negative Exponent
```python
# User selects option "3" for Power
# Enters first number: 2
# Enters second number: -2
# Result: 2 ^ -2 = 0.25
```

---

## Implementation Steps

### Step 1: Add Power Class to operations.py

Add the following class to the end of `operations.py`:

```python
class Power(Operation):
    name = "Power"

    def execute(self, a: float, b: float) -> float:
        return a ** b
```

**Explanation:**
- Inherits from `Operation` abstract base class
- Sets `name` to "Power" for display in the menu
- Implements `execute()` method using Python's exponentiation operator `**`
- Accepts two float parameters: base (a) and exponent (b)
- Returns the result of a raised to the power of b

### Step 2: Register Power Operation in calculator.py

Modify the `_register_default_operations()` method in the `Calculator` class:

```python
def _register_default_operations(self) -> None:
    self.register_operation("1", Add())
    self.register_operation("2", Subtract())
    self.register_operation("3", Power())
```

**Explanation:**
- Registers the Power operation with key "3"
- Follows the existing pattern of operation registration
- The key "3" will be displayed in the menu for users to select

**Updated import statement:**
```python
from operations import Operation, Add, Subtract, Power
```

### Step 3: Update Symbol Logic in app.py

Modify the symbol assignment logic in the `main()` function to handle the power symbol:

**Before:**
```python
symbol = "+" if op_name == "Add" else "-"
```

**After:**
```python
if op_name == "Add":
    symbol = "+"
elif op_name == "Subtract":
    symbol = "-"
elif op_name == "Power":
    symbol = "^"
else:
    symbol = "?"
```

**Alternative (More Scalable):**
Consider adding a `symbol` property to the `Operation` interface for better extensibility:

```python
# In operations.py - Add to Operation class:
@property
@abstractmethod
def symbol(self) -> str:
    ...

# In each operation class:
class Add(Operation):
    name = "Add"
    symbol = "+"
    # ...

class Subtract(Operation):
    name = "Subtract"
    symbol = "-"
    # ...

class Power(Operation):
    name = "Power"
    symbol = "^"
    # ...

# In app.py - Simplify the logic:
symbol = calc.menu_items[choice].symbol
```

### Step 4: Update __init__.py

Modify the `__init__.py` file to export the `Power` class:

**Before:**
```python
__all__ = ["Calculator", "Operation", "Add", "Subtract"]
```

**After:**
```python
__all__ = ["Calculator", "Operation", "Add", "Subtract", "Power"]
```

**Updated import statement:**
```python
from operations import Operation, Add, Subtract, Power
```

---

## Testing Scenarios

### Test Case 1: Basic Power Operation
- **Input:** a=2, b=3
- **Expected Output:** 8
- **Verification:** 2^3 = 8

### Test Case 2: Power of Zero
- **Input:** a=5, b=0
- **Expected Output:** 1
- **Verification:** 5^0 = 1

### Test Case 3: Negative Exponent
- **Input:** a=2, b=-2
- **Expected Output:** 0.25
- **Verification:** 2^-2 = 1/4 = 0.25

### Test Case 4: Fractional Exponent
- **Input:** a=4, b=0.5
- **Expected Output:** 2.0
- **Verification:** 4^0.5 = sqrt(4) = 2

### Test Case 5: Decimal Base
- **Input:** a=1.5, b=2
- **Expected Output:** 2.25
- **Verification:** 1.5^2 = 2.25

### Test Case 6: Negative Base with Even Exponent
- **Input:** a=-2, b=2
- **Expected Output:** 4
- **Verification:** (-2)^2 = 4

### Test Case 7: Negative Base with Odd Exponent
- **Input:** a=-2, b=3
- **Expected Output:** -8
- **Verification:** (-2)^3 = -8

---

## Summary of Changes

| File | Change Type | Description |
|------|------------|-------------|
| `operations.py` | Addition | Add `Power` class implementing the power operation |
| `calculator.py` | Modification | Import `Power` and register it with key "3" |
| `app.py` | Modification | Update symbol logic to display "^" for power operations |
| `__init__.py` | Modification | Export `Power` class in `__all__` |

---

## Benefits of This Implementation

* **Consistency:** Follows the existing Strategy pattern and architecture
* **Extensibility:** Easy to add more operations in the future
* **Maintainability:** Minimal changes to existing code
* **User-Friendly:** Clear menu option and intuitive symbol display
* **Robust:** Handles all numeric types (integers, floats, negative numbers)
* **Scalable:** Symbol logic can be further improved by adding a `symbol` property to the `Operation` interface

---

## Optional Improvements

### 1. Add Symbol Property to Operation Interface
For better scalability and to avoid hardcoding symbol logic in `app.py`:

```python
# In operations.py
from abc import ABC, abstractmethod

class Operation(ABC):
    name: str

    @property
    @abstractmethod
    def symbol(self) -> str:
        ...

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...
```

### 2. Add Error Handling for Edge Cases
Consider adding validation for operations like division by zero or complex number results (e.g., negative base with fractional exponent).

### 3. Add Unit Tests
Create a test file to verify the Power operation works correctly:

```python
# test_operations.py
import unittest
from operations import Power

class TestPowerOperation(unittest.TestCase):
    def setUp(self):
        self.power = Power()

    def test_basic_power(self):
        self.assertEqual(self.power.execute(2, 3), 8)

    def test_power_of_zero(self):
        self.assertEqual(self.power.execute(5, 0), 1)

    def test_negative_exponent(self):
        self.assertEqual(self.power.execute(2, -2), 0.25)
```

---

## Implementation Checklist

- [ ] Add `Power` class to `operations.py`
- [ ] Update imports in `calculator.py` to include `Power`
- [ ] Register Power operation in `_register_default_operations()` with key "3"
- [ ] Update symbol logic in `app.py` to handle power display
- [ ] Update `__init__.py` to export `Power` class
- [ ] Test all scenarios (basic power, zero exponent, negative exponent, etc.)
- [ ] Verify menu displays correctly with 3 options
- [ ] Test user input validation still works
- [ ] Manual testing of the complete workflow
