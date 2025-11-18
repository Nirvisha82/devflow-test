This repository contains a simple command-line interface (CLI) calculator application written in Python. It demonstrates basic Object-Oriented Programming (OOP) principles, specifically the Strategy pattern, to allow for easy extension with new mathematical operations.

---

## Repository Overview

1.  **Project Type**:
    This is a **CLI (Command-Line Interface) tool**. It's designed to be run from a terminal, taking user input and displaying results directly in the console. It is not a web application, library, or framework.

2.  **Architecture**:
    The project follows a modular, object-oriented architecture based on the **Strategy pattern**.
    *   **Core Logic**: The `Calculator` class acts as the context, delegating the actual computation to various `Operation` strategies.
    *   **Operations**: Abstract `Operation` class defines the interface for all operations, and concrete classes like `Add` and `Subtract` implement specific algorithms.
    *   **User Interface**: The `app.py` file handles user interaction, input parsing, and output display, acting as the client that uses the `Calculator`.
    This separation of concerns makes the system flexible and extensible.

3.  **Technology Stack**:
    The project uses **pure Python 3**. No external frameworks or complex libraries are utilized beyond standard Python modules (like `abc` for abstract base classes and `typing` for type hints).

4.  **Entry Points**:
    The main entry point for the application is `app.py`.
    *   When `app.py` is executed (e.g., `python app.py`), the `if __name__ == "__main__":` block is triggered, which calls the `main()` function.
    *   The `main()` function initializes the `Calculator` and enters a loop to interact with the user.

---

## File Analysis

### File: `.gitignore`
*   **Purpose**: Specifies intentionally untracked files that Git should ignore.
*   **Role**: Prevents temporary files, build artifacts, environment-specific files, and other non-source code from being committed to the repository. This is a standard practice for Python projects.
*   **Key Functions/Classes**: N/A (configuration file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: `README.md`
*   **Purpose**: Provides a brief description and introduction to the project.
*   **Role**: Serves as the primary documentation for anyone encountering the repository, explaining its purpose.
*   **Key Functions/Classes**: N/A (documentation file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: `__init__.py`
*   **Purpose**: Marks the directory (`devflow-test` in this case, implicitly as it's the root) as a Python package. It also defines what symbols are exposed when the package is imported.
*   **Role**: When other modules (like `app.py`) import from this package, this file controls which classes and functions are directly accessible.
    ```python
    from .calculator import Calculator
    from .operations import Operation, Add, Subtract

    __all__ = ["Calculator", "Operation", "Add", "Subtract"]
    ```
    This `__all__` variable explicitly lists the public API of the package.
*   **Key Functions/Classes**: N/A (package initialization).
*   **Dependencies**: Depends on `calculator.py` and `operations.py` to import their respective classes.
*   **Business Logic**: N/A.

### File: `app.py`
*   **Purpose**: Implements the user interface and application flow for the calculator.
*   **Role**: It's the client code that orchestrates the interaction between the user and the `Calculator` core logic. It handles input, displays the menu, calls the calculator, and prints results.
*   **Key Functions/Classes**:
    *   `prompt_number(label: str) -> float`:
        *   **Logic**: Continuously prompts the user to enter a number until valid numeric input is provided. Uses a `try-except` block to catch `ValueError` for non-numeric input.
        *   **Business Logic**: Ensures that only valid numerical inputs are passed to the calculator operations.
    *   `main() -> None`:
        *   **Logic**:
            1.  Initializes `Calculator`.
            2.  Enters an infinite loop to display options and process user choices.
            3.  Presents a menu of operations dynamically retrieved from `calc.menu_items`.
            4.  Handles exit conditions (`q`, `quit`, `exit`).
            5.  Validates user choice against available operations.
            6.  Prompts for two numbers using `prompt_number`.
            7.  Calls `calc.compute()` to get the result.
            8.  Prints the result or any error encountered during computation.
        *   **Business Logic**: Manages the entire user interaction lifecycle, from displaying the menu to showing results and handling basic errors. It also contains the specific logic for how the operation symbol is displayed (`+` or `-`).
*   **Dependencies**: Depends on `calculator.py` (specifically the `Calculator` class).
*   **Business Logic**: User interaction flow, input validation for numbers, menu display, choice validation, result formatting.

### File: `calculator.py`
*   **Purpose**: Implements the core calculator logic, managing and delegating to different operations.
*   **Role**: Acts as the "context" in the Strategy design pattern. It holds a collection of `Operation` objects and provides a method to execute a chosen operation without knowing its specific implementation.
*   **Key Functions/Classes**:
    *   `class Calculator`:
        *   **Logic**:
            *   `__init__(self) -> None`: Initializes an empty dictionary `_operations` to store operations and calls `_register_default_operations()`.
            *   `_register_default_operations(self) -> None`: Registers `Add` and `Subtract` operations with keys "1" and "2" respectively.
            *   `register_operation(self, key: str, operation: Operation) -> None`: Allows adding new operations dynamically by associating a key (e.g., "3") with an `Operation` instance.
            *   `@property menu_items(self) -> Dict[str, Operation]`: Provides read-only access to the registered operations, used by `app.py` to display the menu.
            *   `compute(self, key: str, a: float, b: float) -> float`:
                *   **Logic**: Retrieves the `Operation` instance associated with the given `key`. If the key is not found, it raises a `KeyError`. Otherwise, it calls the `execute()` method of the retrieved `Operation` with the provided numbers `a` and `b`.
                *   **Business Logic**: Centralizes the dispatching of computation requests to the correct operation strategy.
*   **Dependencies**: Depends on `operations.py` (specifically the `Operation` ABC, `Add`, and `Subtract` classes) and `typing` for type hints.
*   **Business Logic**: Registration of operations, mapping operation keys to concrete operation implementations, and delegating the actual arithmetic computation.

### File: `operations.py`
*   **Purpose**: Defines the abstract base class for all calculator operations and provides concrete implementations for addition and subtraction.
*   **Role**: Establishes the interface (contract) that all operations must adhere to, enabling polymorphism. It's the "strategy" part of the Strategy pattern.
*   **Key Functions/Classes**:
    *   `class Operation(ABC)`:
        *   **Logic**:
            *   `name: str`: An abstract attribute that concrete operations must define, providing a human-readable name.
            *   `@abstractmethod execute(self, a: float, b: float) -> float`: An abstract method that concrete operations must implement, defining how the operation performs its calculation.
        *   **Business Logic**: Defines the common interface for all arithmetic operations.
    *   `class Add(Operation)`:
        *   **Logic**:
            *   `name = "Add"`: Sets the operation's name.
            *   `execute(self, a: float, b: float) -> float`: Returns the sum of `a` and `b`.
        *   **Business Logic**: Implements the addition operation.
    *   `class Subtract(Operation)`:
        *   **Logic**:
            *   `name = "Subtract"`: Sets the operation's name.
            *   `execute(self, a: float, b: float) -> float`: Returns the difference between `a` and `b`.
        *   **Business Logic**: Implements the subtraction operation.
*   **Dependencies**: Depends on `abc` for `ABC` and `abstractmethod`, and `typing` for type hints.
*   **Business Logic**: Encapsulates the specific algorithms for addition and subtraction.

---

## System Relationships

1.  **Data Flow**:
    *   **Input**: User enters choice and numbers in `app.py`.
    *   **Processing**:
        1.  `app.py` receives user choice and numbers.
        2.  `app.py` calls `calculator.Calculator.compute(choice, a, b)`.
        3.  `calculator.Calculator` looks up the `Operation` instance corresponding to `choice`.
        4.  `calculator.Calculator` calls `operation.execute(a, b)` on the selected `Operation` instance (e.g., `operations.Add.execute`).
        5.  The `execute` method performs the calculation and returns the result.
    *   **Output**:
        1.  The result flows back to `calculator.Calculator`.
        2.  The result flows back to `app.py`.
        3.  `app.py` formats and prints the result to the console.

2.  **Key Components**:
    *   `Calculator` class (`calculator.py`): The central orchestrator, responsible for managing and dispatching operations.
    *   `Operation` ABC (`operations.py`): Defines the contract for all operations, crucial for extensibility.
    *   `Add` and `Subtract` classes (`operations.py`): Concrete implementations of the `Operation` interface, containing the actual arithmetic logic.
    *   `main()` function (`app.py`): The application's entry point and user interaction loop.

3.  **Integration Points**:
    *   `app.py` integrates with `calculator.py` by instantiating `Calculator` and calling its `menu_items` property and `compute` method.
    *   `calculator.py` integrates with `operations.py` by importing `Operation` and its concrete subclasses (`Add`, `Subtract`) and storing instances of these subclasses. It interacts with them polymorphically via the `Operation` interface.
    *   `__init__.py` integrates `calculator.py` and `operations.py` by making their key classes available for external imports.

4.  **API/Interface Design**:
    *   **`Calculator`'s Public API**:
        *   `register_operation(key: str, operation: Operation)`: Allows external code to add new operations.
        *   `menu_items` (property): Provides a dictionary of registered operations for display purposes.
        *   `compute(key: str, a: float, b: float) -> float`: The primary method for performing calculations.
    *   **`Operation`'s Interface**:
        *   `name: str`: A public attribute for the operation's display name.
        *   `execute(a: float, b: float) -> float`: The core method that all concrete operations must implement to perform their specific calculation.
    This design promotes loose coupling: `app.py` doesn't need to know the details of how `Add` or `Subtract` work, only that `Calculator` can compute using an `Operation`. Similarly, `Calculator` doesn't need to know the specific type of `Operation` it's executing, only that it conforms to the `Operation` interface.

---

## Development Insights

1.  **Code Quality**:
    *   **Overall**: The code quality is good. It's clean, well-structured, and easy to understand.
    *   **Readability**: Variable and function names are descriptive.
    *   **Type Hinting**: Extensive use of type hints (`-> float`, `: str`, `Dict[str, Operation]`) significantly improves code clarity and maintainability, making it easier to reason about data types and potential errors.
    *   **Modularity**: The separation into `app.py`, `calculator.py`, and `operations.py` is excellent, promoting clear responsibilities for each module.
    *   **Docstrings**: While not exhaustive, the `Calculator` class has a good docstring explaining its purpose and extensibility. Adding more docstrings to functions and methods would further enhance clarity.

2.  **Design Patterns**:
    *   **Strategy Pattern**: This is the most prominent design pattern.
        *   `Operation` acts as the **Strategy interface**.
        *   `Add` and `Subtract` are **Concrete Strategies**.
        *   `Calculator` is the **Context**, which holds a reference to a Strategy object and delegates the request to it.
        This pattern allows the algorithm (the specific arithmetic operation) to vary independently from the clients that use it (`Calculator` and `app.py`).
    *   **Dependency Inversion Principle (DIP)**: The `Calculator` (high-level module) depends on the `Operation` abstraction (interface), not on the concrete `Add` or `Subtract` implementations (low-level modules). This is a core tenet of good OOP design.

3.  **Potential Issues**:
    *   **Limited Error Handling**: While `ValueError` for numbers and `KeyError` for unknown operations are handled, other potential issues (e.g., division by zero if a `Divide` operation were added) are not explicitly covered at the `app.py` level. The `compute` method in `calculator.py` simply re-raises exceptions from `execute`, which is good, but `app.py`'s generic `except Exception as e:` could be more specific.
    *   **Hardcoded Symbol Display**: In `app.py`, the display of the operation symbol (`+` or `-`) is hardcoded based on the operation's name:
        ```python
        symbol = "+" if op_name == "Add" else "-"
        ```
        If a `Multiply` operation were added, this logic would need to be updated. A better approach would be to include a `symbol` attribute in the `Operation` class itself (e.g., `name: str`, `symbol: str`) or have the `Operation` object provide a formatted string for its display.
    *   **No Input Validation for Operation Choice**: The `app.py` only checks if `choice in calc.menu_items`. It doesn't handle cases where the user enters non-numeric choices that are not 'q' or a valid operation key. This is minor but could be improved.

4.  **Scalability**:
    *   **Operations**: Highly scalable. Adding new operations (e.g., Multiply, Divide, Power) is straightforward:
        1.  Create a new class inheriting from `Operation`.
        2.  Implement its `execute` method.
        3.  Register it in `Calculator._register_default_operations()` or via `Calculator.register_operation()`.
        No changes are required in `app.py` or the core `Calculator.compute()` logic (except for the symbol display issue mentioned above).
    *   **UI**: As a CLI application, its UI scalability is inherently limited. If the project were to grow into a complex application, a different UI framework (e.g., web, GUI) would be needed, which would involve a complete rewrite of `app.py`. However, the core `Calculator` and `Operation` logic would remain reusable.

5.  **Maintainability**:
    *   **High Maintainability**: The clear separation of concerns, adherence to OOP principles, and use of the Strategy pattern make this codebase very easy to maintain.
    *   **Extensibility**: Adding new features (operations) is simple and localized.
    *   **Debugging**: The modular structure and type hints aid in debugging by making it easier to isolate issues and understand data flow.
    *   **Testing**: The `Operation` classes are pure functions (given inputs, produce outputs) and are easily testable in isolation. The `Calculator` class can also be tested by mocking or providing `Operation` instances. `app.py` would require more integration-style testing.

In summary, this is a well-designed and implemented small Python application that effectively demonstrates core OOP principles and design patterns for creating extensible and maintainable code.