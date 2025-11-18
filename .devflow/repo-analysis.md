This repository contains a simple, object-oriented calculator application implemented in Python. It demonstrates a clear separation of concerns and the use of design patterns for extensibility.

---

## Repository Overview

1.  **Project Type**:
    This is a **CLI (Command Line Interface) tool**. It provides an interactive console application for performing basic arithmetic operations.

2.  **Architecture**:
    The project follows a modular and object-oriented architecture, primarily leveraging the **Strategy design pattern**.
    *   **Core Logic (Calculator)**: The `Calculator` class acts as the context, managing and delegating operations.
    *   **Operations (Strategies)**: Abstract `Operation` class defines the interface for all operations, with concrete implementations (`Add`, `Subtract`) providing specific algorithms.
    *   **User Interface (App)**: The `app.py` file handles user interaction, input/output, and orchestrates the use of the `Calculator` core.
    This structure promotes extensibility, allowing new operations to be added without modifying the core `Calculator` logic or the UI.

3.  **Technology Stack**:
    The project uses **pure Python 3**. No external frameworks or libraries are utilized beyond Python's standard library (`abc` for abstract base classes, `typing` for type hints).

4.  **Entry Points**:
    The main entry point for the application is `app.py`. When executed, the `if __name__ == "__main__":` block calls the `main()` function, which initializes the calculator and starts the interactive loop.

---

## File Analysis

### File: `calculator/__init__.py`

*   **Purpose**: This file serves as the package initializer for the `calculator` module. It defines what symbols are exposed when the `calculator` package is imported.
*   **Role**: It acts as an API gateway for the `calculator` package, making `Calculator`, `Operation`, `Add`, and `Subtract` directly accessible from `from calculator import ...`.
*   **Key Functions/Classes**:
    *   `from .calculator import Calculator`: Imports the main `Calculator` class.
    *   `from .operations import Operation, Add, Subtract`: Imports the base `Operation` class and its concrete implementations.
    *   `__all__ = [...]`: Explicitly defines the public interface of the package.
*   **Dependencies**: Depends on `calculator.py` and `operations.py` within the same package.
*   **Business Logic**: None. Its logic is purely for package structure and export management.

### File: `calculator/calculator.py`

*   **Purpose**: This file contains the core logic for the `Calculator` class, which manages and executes different arithmetic operations.
*   **Role**: It acts as the central orchestrator for computations. It maintains a registry of available operations and delegates the actual calculation to the appropriate operation object based on user input.
*   **Key Functions/Classes**:
    *   **`class Calculator`**:
        *   `__init__(self) -> None`: Initializes the calculator, creating an empty dictionary `_operations` to store registered operations and then calls `_register_default_operations()`.
        *   `_register_default_operations(self) -> None`: Registers the default "Add" and "Subtract" operations with keys "1" and "2" respectively. This method encapsulates the initial setup of operations.
        *   `register_operation(self, key: str, operation: Operation) -> None`: Allows new operations to be added to the calculator's registry at runtime, associating them with a unique `key`.
        *   `@property menu_items(self) -> Dict[str, Operation]`: Provides read-only access to the registered operations, useful for displaying menu options.
        *   `compute(self, key: str, a: float, b: float) -> float`: The main method for performing calculations. It looks up the operation by `key` and calls its `execute` method with the given operands `a` and `b`. Raises `KeyError` if the operation is not found.
*   **Dependencies**: Depends on `operations.py` for the `Operation`, `Add`, and `Subtract` classes.
*   **Business Logic**:
    *   Manages the collection of available operations.
    *   Delegates the execution of specific operations to the respective `Operation` objects.
    *   Ensures that only registered operations can be computed.

### File: `calculator/operations.py`

*   **Purpose**: This file defines the abstract base class for all operations and provides concrete implementations for basic arithmetic operations.
*   **Role**: It establishes a common interface for any operation that the `Calculator` can perform, allowing for polymorphic behavior. It also provides the actual algorithms for addition and subtraction.
*   **Key Functions/Classes**:
    *   **`class Operation(ABC)`**: An abstract base class that defines the interface for all operations.
        *   `name: str`: An abstract attribute to hold the human-readable name of the operation.
        *   `@abstractmethod execute(self, a: float, b: float) -> float`: An abstract method that concrete operations must implement to perform their specific calculation.
    *   **`class Add(Operation)`**:
        *   `name = "Add"`: Sets the operation's name.
        *   `execute(self, a: float, b: float) -> float`: Implements addition (`a + b`).
    *   **`class Subtract(Operation)`**:
        *   `name = "Subtract"`: Sets the operation's name.
        *   `execute(self, a: float, b: float) -> float`: Implements subtraction (`a - b`).
*   **Dependencies**: Depends on Python's built-in `abc` module for abstract base class functionality.
*   **Business Logic**:
    *   Defines the contract for any calculable operation (`execute` method).
    *   Implements the specific algorithms for addition and subtraction.

### File: `app.py`

*   **Purpose**: This file provides the command-line user interface for the calculator application.
*   **Role**: It handles user input, displays menu options, validates input, interacts with the `Calculator` core, and presents results to the user. It acts as the application's entry point and main loop.
*   **Key Functions/Classes**:
    *   `prompt_number(label: str) -> float`: A helper function that repeatedly prompts the user for a numeric input until a valid float is entered. It handles `ValueError` for non-numeric input.
    *   `main() -> None`: The main function that orchestrates the application flow:
        *   Initializes a `Calculator` instance.
        *   Enters an infinite loop to display options, get user choice, and perform calculations.
        *   Handles "q" for exit.
        *   Validates user choice against available operations.
        *   Prompts for two numbers using `prompt_number`.
        *   Calls `calc.compute()` to get the result.
        *   Displays the result in a user-friendly format.
        *   Includes basic error handling for `calc.compute()`.
*   **Dependencies**: Depends on the `Calculator` class from the `calculator` package.
*   **Business Logic**:
    *   Manages the interactive user session.
    *   Presents menu options dynamically based on registered operations.
    *   Handles user input validation and conversion.
    *   Orchestrates the interaction with the `Calculator` object.
    *   Formats and displays calculation results.

### File: `.gitignore`

*   **Purpose**: Specifies intentionally untracked files that Git should ignore.
*   **Role**: Prevents various temporary files, build artifacts, environment-specific files, and IDE-related files from being committed to the repository. This is a standard and comprehensive Python `.gitignore` template.
*   **Key Functions/Classes**: N/A
*   **Dependencies**: N/A
*   **Business Logic**: N/A

### File: `README.md`

*   **Purpose**: Provides a brief description of the project.
*   **Role**: Serves as the initial documentation for anyone encountering the repository.
*   **Key Functions/Classes**: N/A
*   **Dependencies**: N/A
*   **Business Logic**: N/A

---

## System Relationships

1.  **Data Flow**:
    *   **User Input**: The `app.py` module prompts the user for an operation choice and two numbers.
    *   **Input Processing**: `app.py` validates the choice and converts number inputs to `float`.
    *   **Delegation to Calculator**: The `app.py` calls the `Calculator.compute(choice, a, b)` method.
    *   **Operation Lookup**: The `Calculator` instance looks up the `Operation` object associated with the `choice` key in its `_operations` dictionary.
    *   **Execution**: The `Calculator` calls the `execute(a, b)` method on the retrieved `Operation` object (e.g., `Add.execute()` or `Subtract.execute()`).
    *   **Result Return**: The `execute` method returns the calculated `float` result to the `Calculator`.
    *   **Result Display**: The `Calculator` returns the result to `app.py`, which then formats and prints it to the console.

2.  **Key Components**:
    *   **`Calculator` class**: The central component that manages operations and performs computations by delegating.
    *   **`Operation` ABC**: The abstract interface that defines the contract for all arithmetic operations.
    *   **`Add` and `Subtract` classes**: Concrete implementations of the `Operation` interface, providing specific calculation logic.
    *   **`app.py` (main loop)**: The user-facing component that drives the application, handles I/O, and orchestrates the interaction with the `Calculator`.

3.  **Integration Points**:
    *   `app.py` integrates with `calculator.Calculator` by instantiating it and calling its `menu_items` property and `compute` method.
    *   `calculator.Calculator` integrates with `calculator.operations.Operation` (and its subclasses) by storing instances of `Operation` and calling their `execute` method polymorphically.
    *   `calculator/__init__.py` integrates the `calculator.py` and `operations.py` modules into a cohesive package.

4.  **API/Interface Design**:
    *   **`Calculator`'s Public API**:
        *   `register_operation(key: str, operation: Operation)`: For adding new operations.
        *   `menu_items` (property): For retrieving available operations to display.
        *   `compute(key: str, a: float, b: float)`: For performing calculations.
    *   **`Operation`'s Interface**:
        *   `name` (attribute): To provide a display name for the operation.
        *   `execute(a: float, b: float)`: The core method that all operations must implement to perform their specific calculation.
    This design ensures that `app.py` only needs to know how to interact with the `Calculator`, and the `Calculator` only needs to know how to interact with the generic `Operation` interface, promoting loose coupling.

---

## Development Insights

1.  **Code Quality**:
    *   **Overall Assessment**: The code quality is good. It is clean, well-structured, and adheres to Python best practices.
    *   **Readability**: Variable and function names are descriptive. The logic is straightforward and easy to follow.
    *   **Type Hinting**: Extensive use of type hints (`-> None`, `: str`, `: float`, `Dict`, `Type`) significantly improves code clarity, maintainability, and allows for static analysis.
    *   **Docstrings**: The `Calculator` class has a clear docstring explaining its purpose and design. Adding docstrings to `Operation` and its subclasses, as well as `prompt_number` and `main`, would further enhance documentation.
    *   **Modularity**: The separation of concerns into `app.py`, `calculator.py`, and `operations.py` is excellent.

2.  **Design Patterns**:
    *   **Strategy Pattern**: This is the most prominent design pattern used.
        *   `Operation` is the **Strategy** interface.
        *   `Add` and `Subtract` are **Concrete Strategies**.
        *   `Calculator` is the **Context**, which holds a reference to a Strategy object (implicitly, it holds multiple strategies and selects one at runtime) and delegates the execution to it.
    This pattern makes the system highly extensible, as new operations can be added by simply creating new `Operation` subclasses and registering them with the `Calculator`, without modifying existing code.

3.  **Potential Issues**:
    *   **Limited Error Handling**: While `prompt_number` handles `ValueError` for non-numeric input and `compute` handles `KeyError` for unknown operations, there's no specific error handling for potential issues within the `execute` methods (e.g., division by zero, if a `Divide` operation were added). The `app.py` catches a generic `Exception`, which is a good fallback but could be more specific.
    *   **Input Validation for `compute`**: The `compute` method assumes `a` and `b` are valid floats. While `prompt_number` ensures this for user input, if `compute` were called directly with non-float values, it could lead to runtime errors (though type hints help here).
    *   **No Configuration for Default Operations**: The default operations (`Add`, `Subtract`) are hardcoded in `_register_default_operations`. For a more complex application, these might be loaded from a configuration file or dynamically discovered. However, for this simple calculator, it's acceptable.

4.  **Scalability**:
    *   **Operational Scalability**: The design is highly scalable in terms of adding new operations. Thanks to the Strategy pattern, new operations (e.g., Multiply, Divide, Power) can be introduced by simply creating new `Operation` subclasses and registering them. This does not require changes to the `Calculator` class or the `app.py` UI logic (beyond potentially updating the display of available options).
    *   **UI Scalability**: As a CLI application, its UI scalability is inherently limited. If the project were to evolve into a GUI or web application, the core `Calculator` and `Operation` logic could be reused, but a new UI layer would need to be built.

5.  **Maintainability**:
    *   **High Maintainability**: The code is very easy to maintain and understand due to its clear structure, modularity, and adherence to OOP principles.
    *   **Extensibility**: Adding new features (new operations) is straightforward and localized, minimizing the risk of introducing bugs into existing code.
    *   **Testability**: Each component (e.g., `Calculator`, `Add`, `Subtract`) is relatively independent, making unit testing straightforward. One could easily write tests for `Add.execute()`, `Subtract.execute()`, and `Calculator.compute()` in isolation.
    *   **Readability**: The use of type hints and meaningful names contributes significantly to readability, making it easier for new developers to onboard and understand the codebase.