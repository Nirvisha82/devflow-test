This repository contains a simple, object-oriented calculator application implemented in Python. It demonstrates a clear separation of concerns and the use of design patterns to make the codebase extensible.

---

## Repository Overview

1.  **Project Type**:
    This is a **CLI (Command-Line Interface) tool**. It provides an interactive console application for performing basic arithmetic operations (addition and subtraction).

2.  **Architecture**:
    The project follows a modular, object-oriented architecture, primarily leveraging the **Strategy Pattern**.
    *   **Core Logic (Calculator)**: A central `Calculator` class manages available operations and executes them. It acts as the context for the strategies.
    *   **Operations (Strategies)**: Abstract `Operation` class defines the interface for all arithmetic operations. Concrete `Add` and `Subtract` classes implement this interface, providing specific algorithms.
    *   **User Interface (App)**: A separate `app.py` file handles user interaction, input validation, and displays results, acting as the client that uses the `Calculator` core.

3.  **Technology Stack**:
    The project exclusively uses **Python 3.x** and its standard library features, including `abc` for abstract base classes and `typing` for type hints. No external frameworks or libraries are used.

4.  **Entry Points**:
    The main entry point for the application is `app.py`.
    *   When `app.py` is executed, the `if __name__ == "__main__":` block calls the `main()` function.
    *   The `main()` function then initializes the `Calculator` and enters a loop to interact with the user.

---

## File Analysis

### File: `calculator/__init__.py`

*   **Purpose**: This file serves as the package initializer for the `calculator` module. Its primary role is to define what symbols are exposed when `from calculator import *` is used and to simplify imports from submodules.
*   **Role**: It makes `Calculator`, `Operation`, `Add`, and `Subtract` directly accessible under the `calculator` namespace, improving module usability.
*   **Key Functions/Classes**:
    *   It imports `Calculator` from `calculator.calculator` and `Operation`, `Add`, `Subtract` from `calculator.operations`.
    *   `__all__ = ["Calculator", "Operation", "Add", "Subtract"]` explicitly defines the public API of the package.
*   **Dependencies**: Depends on `calculator.calculator` and `calculator.operations`.
*   **Business Logic**: Contains no business logic itself; it's purely for package structure and export management.

### File: `calculator/calculator.py`

*   **Purpose**: This file defines the core `Calculator` class, which orchestrates the execution of arithmetic operations.
*   **Role**: It acts as the central component that holds a registry of available operations and delegates computation requests to the appropriate operation object. It decouples the client (`app.py`) from the specific implementation of operations.
*   **Key Functions/Classes**:
    *   **`class Calculator`**:
        *   `__init__(self) -> None`: Initializes an empty dictionary `_operations` to store registered operations and calls `_register_default_operations()`.
        *   `_register_default_operations(self) -> None`: Registers the `Add` and `Subtract` operations with keys "1" and "2" respectively. This is where default operations are set up.
        *   `register_operation(self, key: str, operation: Operation) -> None`: Allows new operations to be added to the calculator's registry at runtime. This is a key extensibility point.
        *   `@property menu_items(self) -> Dict[str, Operation]`: Provides read-only access to the dictionary of registered operations, useful for displaying menu options to the user.
        *   `compute(self, key: str, a: float, b: float) -> float`: Takes an operation key and two numbers, retrieves the corresponding `Operation` object, and calls its `execute` method. Raises `KeyError` if the operation key is not found.
*   **Dependencies**: Depends on `calculator.operations` for the `Operation`, `Add`, and `Subtract` classes.
*   **Business Logic**: Manages the collection of operations and the delegation of computation tasks. It implements the logic for selecting and executing an operation based on a given key.

### File: `calculator/operations.py`

*   **Purpose**: This file defines the abstract interface for all arithmetic operations and provides concrete implementations for addition and subtraction.
*   **Role**: It establishes a contract (`Operation` ABC) that all specific operation classes must adhere to, ensuring they have an `execute` method. This allows the `Calculator` to interact with any operation uniformly, without knowing its specific type.
*   **Key Functions/Classes**:
    *   **`class Operation(ABC)`**:
        *   `name: str`: An abstract attribute (implicitly, as it's defined in the base class and expected in subclasses) to hold the human-readable name of the operation.
        *   `@abstractmethod execute(self, a: float, b: float) -> float`: The abstract method that all concrete operation classes must implement. This method performs the actual arithmetic calculation.
    *   **`class Add(Operation)`**:
        *   `name = "Add"`: Sets the name for this operation.
        *   `execute(self, a: float, b: float) -> float`: Implements addition (`a + b`).
    *   **`class Subtract(Operation)`**:
        *   `name = "Subtract"`: Sets the name for this operation.
        *   `execute(self, a: float, b: float) -> float`: Implements subtraction (`a - b`).
*   **Dependencies**: Depends on Python's built-in `abc` module for Abstract Base Classes.
*   **Business Logic**: Defines the fundamental behavior of an arithmetic operation and implements the specific mathematical logic for addition and subtraction.

### File: `.gitignore`

*   **Purpose**: Specifies intentionally untracked files that Git should ignore.
*   **Role**: Prevents temporary files, build artifacts, environment-specific files, and IDE-related files from being committed to the repository, keeping the version control clean and focused on source code.
*   **Key Functions/Classes**: N/A (configuration file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: `README.md`

*   **Purpose**: Provides a brief description of the project.
*   **Role**: Serves as the initial documentation for anyone encountering the repository, explaining its purpose.
*   **Key Functions/Classes**: N/A (documentation file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: `app.py`

*   **Purpose**: This is the main application file, responsible for the user interface and overall application flow.
*   **Role**: It acts as the client of the `calculator` module, handling user input, displaying menus, validating input, and presenting results. It orchestrates the interaction between the user and the `Calculator` core.
*   **Key Functions/Classes**:
    *   `prompt_number(label: str) -> float`: A utility function that repeatedly prompts the user for a numeric input until a valid float is entered. Includes error handling for `ValueError`.
    *   `main() -> None`:
        *   Initializes `Calculator`.
        *   Enters an infinite loop to display options (from `calc.menu_items`).
        *   Prompts the user for a choice (operation key or 'q' to quit).
        *   Handles exit conditions and invalid choices.
        *   If a valid operation is chosen, it prompts for two numbers using `prompt_number`.
        *   Calls `calc.compute()` to get the result.
        *   Displays the result, including a hardcoded symbol (`+` or `-`) based on the operation name.
        *   Includes a generic `try-except Exception` block for `compute` errors.
*   **Dependencies**: Depends on `calculator.Calculator`.
*   **Business Logic**: Manages the user interaction loop, input/output, and basic error reporting for the UI layer.

---

## System Relationships

1.  **Data Flow**:
    *   **User Input**: The `app.py` module prompts the user for an operation choice and two numbers.
    *   **Delegation to Calculator**: This input (choice, number A, number B) is passed to the `Calculator` instance in `app.py` via the `compute()` method.
    *   **Operation Selection**: The `Calculator` uses the `choice` (key) to look up the corresponding `Operation` object from its `_operations` dictionary.
    *   **Execution**: The `Calculator` then calls the `execute()` method on the selected `Operation` object, passing numbers A and B.
    *   **Result Return**: The `Operation` subclass performs the calculation and returns the result (a float) to the `Calculator`.
    *   **Result Display**: The `Calculator` returns the result to `app.py`, which then formats and prints it to the console for the user.

2.  **Key Components**:
    *   **`Calculator` (in `calculator/calculator.py`)**: The central orchestrator. It manages the available operations and delegates the actual computation.
    *   **`Operation` (ABC in `calculator/operations.py`)**: The abstract interface that defines the contract for all arithmetic operations. It's crucial for the extensibility of the system.
    *   **`Add`, `Subtract` (in `calculator/operations.py`)**: Concrete implementations of the `Operation` interface, embodying the specific arithmetic logic. These are the "strategies."
    *   **`app.py`**: The user interface layer, responsible for interaction, input/output, and driving the application flow.

3.  **Integration Points**:
    *   `app.py` integrates with `calculator.Calculator` by instantiating it and calling its `menu_items` property and `compute()` method.
    *   `calculator.Calculator` integrates with `calculator.operations.Operation` (and its concrete subclasses) by storing instances of `Operation` and calling their `execute()` method.
    *   `calculator/__init__.py` integrates the `calculator` package by exposing its core components.

4.  **API/Interface Design**:
    *   **`Calculator`'s Public API**:
        *   `register_operation(key: str, operation: Operation)`: Allows external code to add new operations.
        *   `menu_items` (property): Provides a way to query available operations for display.
        *   `compute(key: str, a: float, b: float)`: The main method for performing calculations.
    *   **`Operation` Interface**:
        *   `name: str`: A descriptive name for the operation.
        *   `execute(a: float, b: float) -> float`: The method that performs the actual calculation.
    This design promotes loose coupling. `app.py` only needs to know about the `Calculator`'s interface, and `Calculator` only needs to know about the `Operation` interface, not the specific `Add` or `Subtract` implementations.

---

## Development Insights

1.  **Code Quality**:
    *   **Good**: The code is generally clean, well-structured, and follows Python best practices.
    *   **Readability**: Variable and function names are descriptive.
    *   **Type Hinting**: Extensive use of type hints (`-> None`, `: str`, `: float`, `Dict`, `Type`) significantly improves code clarity and maintainability, making it easier to understand expected inputs and outputs.
    *   **OOP Principles**: Strong adherence to Object-Oriented Programming principles, especially encapsulation and polymorphism.
    *   **Modularity**: The separation of UI (`app.py`), core logic (`calculator.py`), and operation definitions (`operations.py`) is excellent.

2.  **Design Patterns**:
    *   **Strategy Pattern**: This is the most prominent pattern.
        *   `Operation` is the **Strategy interface**.
        *   `Add` and `Subtract` are **Concrete Strategies**.
        *   `Calculator` is the **Context**, which holds a reference to a `Strategy` object (or a collection of them) and delegates the request to it.
    *   **Dependency Injection (Implicit)**: The `Calculator`'s `register_operation` method allows `Operation` instances to be "injected" into the calculator, rather than the calculator instantiating them directly. This enhances flexibility.

3.  **Potential Issues**:
    *   **Generic Error Handling in `app.py`**: The `except Exception as e:` block in `app.py` is too broad. While it catches errors from `calc.compute`, it doesn't differentiate between a `KeyError` (unknown operation) and other potential issues. More specific error handling could provide better user feedback.
    *   **Hardcoded Symbol Logic in `app.py`**: The line `symbol = "+" if op_name == "Add" else "-"` in `app.py` is a minor maintainability concern. If new operations like "Multiply" or "Divide" were added, this line would need to be updated. A better approach would be to add a `symbol` attribute or method to the `Operation` ABC, allowing each operation to define its display symbol.
    *   **No Unit Tests**: There are no unit tests provided, which is crucial for verifying the correctness of the calculator logic and ensuring that future changes don't introduce regressions.
    *   **Operation Keys**: Using "1", "2" as string keys for operations is functional but could be less readable or prone to conflicts if many operations are added. An `Enum` or more descriptive string keys might be considered for larger applications.

4.  **Scalability**:
    *   **Operation Scalability**: Highly scalable in terms of adding new operations. To add a new operation (e.g., `Multiply`), one simply needs to:
        1.  Create a new class `Multiply(Operation)` in `operations.py`.
        2.  Implement its `execute` method.
        3.  Register it with the `Calculator` instance (e.g., `calc.register_operation("3", Multiply())`).
        No changes are required in `calculator.py` or `app.py` (apart from potentially updating the `symbol` logic if not refactored).
    *   **Application Scalability**: As a CLI application, it's not designed for concurrent users or large-scale data processing. Its scalability is limited to the scope of a single user interaction.

5.  **Maintainability**:
    *   **High**: The codebase is very maintainable due to its clear structure, modularity, and adherence to design patterns.
    *   **Separation of Concerns**: Changes to the UI (`app.py`) generally won't affect the core logic (`calculator.py` or `operations.py`), and vice-versa. Adding new operations is straightforward and isolated to `operations.py` and a registration call.
    *   **Extensibility**: The Strategy Pattern makes it very easy to extend the calculator with new operations without modifying existing core logic.
    *   **Readability**: Type hints and clear naming contribute significantly to understanding the code quickly.
    *   The minor issues mentioned under "Potential Issues" (like the hardcoded symbol logic) are small points that could slightly impact maintainability if not addressed as the project grows.