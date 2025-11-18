This repository contains a simple, object-oriented calculator application implemented in Python. It demonstrates a clear separation of concerns, allowing for easy extension of arithmetic operations.

---

## Repository Overview

1.  **Project Type**:
    This is a **CLI (Command Line Interface) tool**. It provides an interactive console application for performing basic arithmetic operations (addition and subtraction).

2.  **Architecture**:
    The project follows an **Object-Oriented Programming (OOP)** architecture with a strong emphasis on the **Strategy Pattern**.
    *   **Core Logic**: The `Calculator` class acts as the context, managing and delegating operations.
    *   **Operations**: An abstract `Operation` class defines the interface for all arithmetic operations, with concrete implementations (`Add`, `Subtract`) providing the specific algorithms.
    *   **User Interface**: The `app.py` script handles user interaction, input parsing, and displays results, acting as the client that uses the `Calculator` core.
    This design promotes extensibility, as new operations can be added without modifying the `Calculator` or `app.py` logic.

3.  **Technology Stack**:
    The project uses **pure Python 3**. No external frameworks or libraries are utilized beyond Python's standard library (e.g., `abc` for abstract base classes, `typing` for type hints).

4.  **Entry Points**:
    The main entry point for the application is `app.py`. When executed, it initializes the `Calculator` and enters a loop to interact with the user.
    ```python
    # app.py
    if __name__ == "__main__":
        main()
    ```

---

## File Analysis

### File: `calculator/__init__.py`

1.  **Purpose**:
    This file serves as the package initializer for the `calculator` module. Its primary purpose is to define what symbols are exposed when the `calculator` package is imported.

2.  **Role**:
    It acts as the public interface for the `calculator` package, making `Calculator`, `Operation`, `Add`, and `Subtract` directly accessible when `from calculator import ...` is used. This simplifies imports for consumers of the package.

3.  **Key Functions/Classes**:
    *   It imports `Calculator` from `calculator.calculator` and `Operation`, `Add`, `Subtract` from `calculator.operations`.
    *   The `__all__` variable explicitly defines the public API of the package.

4.  **Dependencies**:
    It depends on `calculator.calculator` and `calculator.operations` within the same package.

5.  **Business Logic**:
    No direct business logic is implemented here; it's purely for package structuring and export control.

### File: `calculator/calculator.py`

1.  **Purpose**:
    This file defines the core `Calculator` class, which orchestrates the execution of arithmetic operations.

2.  **Role**:
    It acts as the central component that manages a collection of available operations and delegates the actual computation to the appropriate operation object based on user input. It decouples the client (e.g., `app.py`) from the specific implementation details of each operation.

3.  **Key Functions/Classes**:
    *   **`Calculator` class**:
        *   `__init__(self) -> None`: Initializes the calculator, creating an empty dictionary `_operations` to store registered operations and then calls `_register_default_operations`.
        *   `_register_default_operations(self) -> None`: Registers the `Add` and `Subtract` operations with specific keys ("1" and "2"). This method demonstrates how operations are initially set up.
        *   `register_operation(self, key: str, operation: Operation) -> None`: Allows new operations to be added to the calculator at runtime, associating them with a unique key.
        *   `@property menu_items(self) -> Dict[str, Operation]`: Provides read-only access to the registered operations, useful for displaying menu options to the user.
        *   `compute(self, key: str, a: float, b: float) -> float`: The main method for performing calculations. It looks up the operation by `key` and calls its `execute` method with the given operands. It raises a `KeyError` if the operation is not found.

4.  **Dependencies**:
    It depends on `calculator.operations` to import `Operation`, `Add`, and `Subtract`.

5.  **Business Logic**:
    *   Manages the registry of operations.
    *   Delegates the actual arithmetic computation to the specific `Operation` objects.
    *   Enforces that only registered operations can be executed.

### File: `calculator/operations.py`

1.  **Purpose**:
    This file defines the abstract base class `Operation` and concrete implementations for basic arithmetic operations like `Add` and `Subtract`.

2.  **Role**:
    It provides the extensible framework for defining any number of arithmetic operations. The `Operation` ABC establishes a contract (`execute` method) that all concrete operations must adhere to, ensuring polymorphism.

3.  **Key Functions/Classes**:
    *   **`Operation` (ABC)**:
        *   `name: str`: An abstract attribute to hold the human-readable name of the operation.
        *   `@abstractmethod execute(self, a: float, b: float) -> float`: The abstract method that concrete operations must implement to perform their specific calculation.
    *   **`Add(Operation)`**:
        *   `name = "Add"`: Sets the operation's name.
        *   `execute(self, a: float, b: float) -> float`: Implements addition (`a + b`).
    *   **`Subtract(Operation)`**:
        *   `name = "Subtract"`: Sets the operation's name.
        *   `execute(self, a: float, b: float) -> float`: Implements subtraction (`a - b`).

4.  **Dependencies**:
    It depends on Python's built-in `abc` module for Abstract Base Classes. It has no dependencies on other files within the `calculator` package.

5.  **Business Logic**:
    *   Defines the interface for all arithmetic operations.
    *   Implements the specific logic for addition and subtraction.

### File: `.gitignore`

1.  **Purpose**:
    This file specifies intentionally untracked files and directories that Git should ignore.

2.  **Role**:
    It ensures that temporary files, build artifacts, environment-specific configurations, and other non-essential files are not committed to the repository, keeping the version control clean and focused on source code.

3.  **Key Functions/Classes**: N/A (configuration file).

4.  **Dependencies**: N/A.

5.  **Business Logic**: N/A.

### File: `README.md`

1.  **Purpose**:
    This file provides a brief description of the repository.

2.  **Role**:
    It serves as the initial documentation for anyone visiting the repository, explaining its purpose.

3.  **Key Functions/Classes**: N/A (documentation file).

4.  **Dependencies**: N/A.

5.  **Business Logic**: N/A.

### File: `app.py`

1.  **Purpose**:
    This file contains the main application logic for the command-line interface (CLI) calculator. It handles user interaction, input, and output.

2.  **Role**:
    It acts as the client of the `calculator` package. It initializes the `Calculator` object, presents a menu to the user, prompts for input, calls the `Calculator` to perform operations, and displays the results.

3.  **Key Functions/Classes**:
    *   **`prompt_number(label: str) -> float`**:
        *   Prompts the user to enter a number, continuously retrying until valid numeric input is provided. This function handles input validation for numbers.
    *   **`main() -> None`**:
        *   The main application loop.
        *   Initializes `Calculator`.
        *   Displays a menu of available operations using `calc.menu_items`.
        *   Handles user choice for operations or exit.
        *   Prompts for two numbers (`a` and `b`).
        *   Calls `calc.compute()` to get the result.
        *   Prints the result in a user-friendly format.
        *   Includes basic error handling for computation.

4.  **Dependencies**:
    It depends on the `Calculator` class from the `calculator` package.

5.  **Business Logic**:
    *   Manages the interactive user session.
    *   Validates user input (ensuring numbers are entered).
    *   Maps user choices to calculator operations.
    *   Displays menu and results.

---

## System Relationships

1.  **Data Flow**:
    *   **User Input**: The `app.py` script prompts the user for an operation choice and two numbers.
    *   **Delegation to Calculator**: The `app.py` script passes the chosen operation key and numbers to the `Calculator.compute()` method.
    *   **Delegation to Operation**: The `Calculator` instance, based on the `key`, retrieves the corresponding `Operation` object (e.g., `Add` or `Subtract`) from its `_operations` dictionary.
    *   **Execution**: The `Operation` object's `execute()` method performs the actual calculation.
    *   **Result Return**: The result flows back from the `Operation` to the `Calculator`, and then from the `Calculator` back to `app.py`.
    *   **User Output**: `app.py` formats and displays the result to the user.

2.  **Key Components**:
    *   **`Calculator` class**: The central orchestrator. It knows about all available operations and delegates tasks. It's the "Context" in the Strategy pattern.
    *   **`Operation` Abstract Base Class**: Defines the common interface for all arithmetic strategies. It's the "Strategy" interface.
    *   **`Add`, `Subtract` classes**: Concrete implementations of the `Operation` interface, providing specific algorithms. These are the "Concrete Strategies".
    *   **`app.py` (main function)**: The client that interacts with the user and utilizes the `Calculator` to perform tasks.

3.  **Integration Points**:
    *   `app.py` integrates with `calculator.Calculator` by instantiating it and calling its `compute` and `menu_items` methods.
    *   `calculator.Calculator` integrates with `calculator.operations.Operation` (and its concrete subclasses) by storing instances of them and calling their `execute` method polymorphically.
    *   `calculator/__init__.py` integrates the `calculator.calculator` and `calculator.operations` modules by importing and exposing their key classes.

4.  **API/Interface Design**:
    *   **`Calculator`'s Public API**:
        *   `register_operation(key: str, operation: Operation)`: For adding new operations.
        *   `menu_items: Dict[str, Operation]`: For retrieving available operations (e.g., for menu display).
        *   `compute(key: str, a: float, b: float) -> float`: For performing calculations.
    *   **`Operation`'s Public API (Interface)**:
        *   `name: str`: A property to identify the operation.
        *   `execute(a: float, b: float) -> float`: The method to perform the actual calculation.
    This design ensures that `app.py` only needs to know about the `Calculator`'s interface, and `Calculator` only needs to know about the `Operation` interface, promoting loose coupling.

---

## Development Insights

1.  **Code Quality**:
    The code quality is **good**.
    *   **Readability**: The code is well-structured, uses meaningful variable and class names, and includes docstrings for the `Calculator` class.
    *   **Type Hinting**: Type hints are consistently used (`-> None`, `: str`, `: float`, `Dict`, `Type`), which significantly improves code clarity, maintainability, and allows for static analysis.
    *   **Modularity**: The project is highly modular, with clear separation of concerns between the UI (`app.py`), the calculator logic (`calculator.calculator`), and the operation definitions (`calculator.operations`).
    *   **OOP Principles**: It effectively utilizes encapsulation, abstraction (via `Operation` ABC), and polymorphism.

2.  **Design Patterns**:
    The primary design pattern used is the **Strategy Pattern**:
    *   **Context**: The `Calculator` class.
    *   **Strategy Interface**: The `Operation` abstract base class.
    *   **Concrete Strategies**: The `Add` and `Subtract` classes.
    This pattern allows the algorithm (the specific arithmetic operation) to vary independently from the client that uses it (`Calculator`). New operations can be added without changing the `Calculator` class.

3.  **Potential Issues**:
    *   **Generic Error Handling in `app.py`**: The `except Exception as e:` block in `app.py` is very broad. While it catches errors, it doesn't differentiate between potential issues (e.g., `KeyError` from `compute` vs. other unexpected errors). More specific error handling could provide better user feedback.
    *   **Hardcoded Operation Keys**: The keys "1" and "2" for Add and Subtract are hardcoded in `_register_default_operations`. While simple for this example, in a larger application, a more robust mechanism for key generation or user-friendly identifiers might be preferred.
    *   **Brittle Symbol Determination**: In `app.py`, the symbol for printing the result (`+` or `-`) is determined by string comparison (`op_name == "Add"`). This is brittle; if the `name` attribute of `Add` or `Subtract` ever changes, this logic will break. A better approach would be to include a `symbol` attribute or method in the `Operation` interface.
    *   **Lack of Unit Tests**: There are no unit tests provided, which makes it harder to ensure correctness and prevent regressions when making changes or adding new features.
    *   **Limited Operations**: Currently, only two operations are implemented. While the design allows for easy extension, the current functionality is basic.

4.  **Scalability**:
    *   **Operation Scalability**: The design is highly scalable for adding new arithmetic operations. A new operation (e.g., `Multiply`, `Divide`, `Power`) can be added by simply creating a new class that inherits from `Operation` and implementing its `execute` method, then registering it with the `Calculator`. This requires no changes to `Calculator` or `app.py`.
    *   **UI Scalability**: The current CLI is simple and effective for a few operations. For a significantly larger number of operations or more complex user interactions (e.g., chaining operations, memory functions), the CLI might become cumbersome, and a different UI approach (e.g., a GUI or web interface) would be more appropriate. However, the core `calculator` logic would remain reusable.

5.  **Maintainability**:
    The project exhibits **high maintainability**:
    *   **Clear Separation of Concerns**: Changes to the UI won't affect the core calculation logic, and changes to how an operation works won't affect the `Calculator` or `app.py`.
    *   **Extensibility**: Adding new operations is straightforward and isolated, minimizing the risk of introducing bugs into existing code.
    *   **Readability and Type Hints**: Make it easy for new developers to understand and work with the codebase.
    *   **Modularity**: The `calculator` package is well-defined, making it potentially reusable in other projects.

Overall, this is a well-designed and implemented small project that effectively demonstrates good OOP principles and design patterns for creating extensible systems.