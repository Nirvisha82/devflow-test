This repository contains a simple command-line interface (CLI) calculator application written in Python. It demonstrates an object-oriented design approach, specifically leveraging the Strategy pattern (or a variation of the Command pattern) for handling different mathematical operations.

---

## Repository Overview

1.  **Project Type**:
    This is a **CLI (Command-Line Interface) tool**. It's a standalone application that interacts with the user through text-based input and output in a terminal.

2.  **Architecture**:
    The application follows a modular and object-oriented architecture. It separates the user interface logic from the core calculator logic and the individual operation implementations.
    *   **UI Layer (`app.py`)**: Handles user input, displays menus, and presents results.
    *   **Core Logic Layer (`calculator/calculator.py`)**: Manages and dispatches operations. It acts as a context for the Strategy pattern, holding references to various operation strategies.
    *   **Operations Layer (`calculator/operations.py`)**: Defines an abstract interface for operations and provides concrete implementations (strategies) for specific mathematical functions like addition and subtraction.

    This design promotes extensibility, allowing new operations to be added without modifying the core `Calculator` class or the `app.py` UI logic.

3.  **Technology Stack**:
    The project uses **pure Python 3**. No external frameworks or libraries are utilized beyond Python's standard library (e.g., `abc` for abstract base classes).

4.  **Entry Points**:
    The main entry point for the application is `app.py`.
    When `app.py` is executed (e.g., `python app.py`), the `if __name__ == "__main__":` block ensures that the `main()` function is called, which then initializes and runs the calculator's interactive loop.

---

## File Analysis

### File: .gitignore

*   **Purpose**: Specifies intentionally untracked files that Git should ignore.
*   **Role**: Prevents various temporary files, build artifacts, environment-specific files, and IDE-related files from being committed to the repository. This is a standard practice for Python projects to keep the repository clean.
*   **Key Functions/Classes**: N/A (configuration file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: README.md

*   **Purpose**: Provides a brief introduction and description of the project.
*   **Role**: Serves as the primary documentation for anyone encountering the repository, explaining its purpose and supported features.
*   **Key Functions/Classes**: N/A (documentation file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: app.py

*   **Purpose**: Implements the user interface and the main application loop for the calculator.
*   **Role**: It is the orchestrator of the application, handling user interaction, input validation, and displaying results by interacting with the `Calculator` core logic.
*   **Key Functions/Classes**:
    *   `prompt_number(label: str) -> float`: A utility function to repeatedly prompt the user for a numeric input until a valid float is provided. It includes basic error handling for `ValueError`.
    *   `main() -> None`: The core application function.
        *   Initializes a `Calculator` instance.
        *   Enters an infinite loop to display the menu, get user choice, prompt for numbers, and compute the result.
        *   Handles user exit commands (`q`, `quit`, `exit`).
        *   Validates user's operation choice.
        *   Calls `calc.compute()` to perform the calculation.
        *   Displays the result or any errors.
*   **Dependencies**:
    *   `calculator.Calculator`: Depends on the `Calculator` class to perform operations.
*   **Business Logic**:
    *   User input/output management.
    *   Menu display and navigation.
    *   Basic input validation (numeric input, valid operation choice).
    *   Orchestration of the calculation process.
    *   Error display for invalid inputs or computation issues.

### File: calculator/__init__.py

*   **Purpose**: Marks the `calculator` directory as a Python package and controls what symbols are exposed when the package is imported.
*   **Role**: Simplifies imports for users of the `calculator` package. Instead of `from calculator.calculator import Calculator`, one can simply do `from calculator import Calculator`. The `__all__` variable explicitly defines the public API of the package.
*   **Key Functions/Classes**:
    *   Imports `Calculator` from `calculator.calculator`.
    *   Imports `Operation`, `Add`, `Subtract` from `calculator.operations`.
    *   `__all__ = ["Calculator", "Operation", "Add", "Subtract"]`: Defines the public interface.
*   **Dependencies**:
    *   `calculator.calculator`
    *   `calculator.operations`
*   **Business Logic**: None directly; it's purely for package structure and import management.

### File: calculator/calculator.py

*   **Purpose**: Implements the `Calculator` class, which manages and executes different mathematical operations.
*   **Role**: This is the central component that holds a collection of `Operation` objects (strategies) and dispatches computation requests to the appropriate operation based on a key. It acts as the "Context" in the Strategy design pattern.
*   **Key Functions/Classes**:
    *   `class Calculator`:
        *   `__init__(self) -> None`: Initializes an empty dictionary `_operations` to store registered operations and calls `_register_default_operations()`.
        *   `_register_default_operations(self) -> None`: Registers the `Add` and `Subtract` operations with keys "1" and "2" respectively. This method can be extended to add more default operations.
        *   `register_operation(self, key: str, operation: Operation) -> None`: Allows external code to register new operations with a unique key. This is the extensibility point.
        *   `@property menu_items(self) -> Dict[str, Operation]`: Provides read-only access to the registered operations, which is used by `app.py` to display the menu.
        *   `compute(self, key: str, a: float, b: float) -> float`: The core method to perform a calculation. It looks up the `Operation` object by `key` and calls its `execute()` method with the given numbers. Raises `KeyError` if the operation is not found.
*   **Dependencies**:
    *   `typing.Dict`, `typing.Type` (for type hints).
    *   `calculator.operations.Operation`, `Add`, `Subtract`.
*   **Business Logic**:
    *   Management of available operations.
    *   Delegation of actual computation to specific `Operation` instances.
    *   Ensuring that only registered operations can be executed.

### File: calculator/operations.py

*   **Purpose**: Defines the abstract base class for all calculator operations and provides concrete implementations for addition and subtraction.
*   **Role**: This file establishes the contract (interface) for any operation that can be performed by the `Calculator`. It is the "Strategy" interface and concrete "Strategies" in the Strategy design pattern.
*   **Key Functions/Classes**:
    *   `class Operation(ABC)`: An abstract base class.
        *   `name: str`: An abstract attribute to hold the human-readable name of the operation.
        *   `@abstractmethod execute(self, a: float, b: float) -> float`: An abstract method that concrete operations must implement to perform their specific calculation.
    *   `class Add(Operation)`:
        *   `name = "Add"`: Sets the operation's name.
        *   `execute(self, a: float, b: float) -> float`: Implements addition (`a + b`).
    *   `class Subtract(Operation)`:
        *   `name = "Subtract"`: Sets the operation's name.
        *   `execute(self, a: float, b: float) -> float`: Implements subtraction (`a - b`).
*   **Dependencies**:
    *   `abc.ABC`, `abc.abstractmethod` (for defining abstract classes and methods).
*   **Business Logic**:
    *   Defines the common interface for all mathematical operations.
    *   Encapsulates the specific logic for addition and subtraction.

---

## System Relationships

1.  **Data Flow**:
    *   The user provides input (operation choice, numbers) to `app.py`.
    *   `app.py` validates the input and passes the operation key and numbers to an instance of `Calculator`.
    *   The `Calculator` instance, in its `compute` method, retrieves the appropriate `Operation` object (e.g., `Add` or `Subtract`) from its internal dictionary using the provided key.
    *   The `Calculator` then calls the `execute` method on the retrieved `Operation` object, passing the numbers `a` and `b`.
    *   The `Operation` object performs the calculation and returns the result (a `float`).
    *   The result flows back to the `Calculator`, then back to `app.py`.
    *   `app.py` formats and displays the result to the user.

2.  **Key Components**:
    *   **`app.py` (User Interface / Orchestrator)**: Handles all user interaction, input, output, and the main application loop. It's the entry point and the bridge between the user and the calculator's core logic.
    *   **`Calculator` class (Core Logic / Context)**: Manages the collection of available operations and delegates the actual computation. It's crucial for the extensibility of the system.
    *   **`Operation` ABC (Strategy Interface)**: Defines the common interface that all concrete operations must adhere to. This is fundamental for polymorphism and extensibility.
    *   **`Add`, `Subtract` classes (Concrete Strategies)**: Implement the specific mathematical logic for their respective operations.

3.  **Integration Points**:
    *   `app.py` integrates with `calculator.Calculator` by:
        *   Instantiating `Calculator`.
        *   Accessing `calc.menu_items` to display the menu.
        *   Calling `calc.compute(choice, a, b)` to perform calculations.
    *   `calculator.Calculator` integrates with `calculator.operations` by:
        *   Instantiating `Add` and `Subtract` objects during its initialization.
        *   Storing these `Operation` objects in its `_operations` dictionary.
        *   Calling the `execute()` method on the stored `Operation` objects.

4.  **API/Interface Design**:
    *   **`Calculator` Public API**:
        *   `__init__()`: Constructor.
        *   `register_operation(key: str, operation: Operation)`: For adding new operations.
        *   `menu_items` (property): To get the list of available operations for display.
        *   `compute(key: str, a: float, b: float) -> float`: To execute an operation.
    *   **`Operation` Interface**:
        *   `name: str` (abstract attribute): To provide a display name.
        *   `execute(a: float, b: float) -> float` (abstract method): The core method for performing the calculation.

    This design ensures loose coupling between the UI (`app.py`), the `Calculator` core, and the individual `Operation` implementations.

---

## Development Insights

1.  **Code Quality**:
    *   **Overall Assessment**: The code quality is good. It's clean, well-structured, and follows Python best practices.
    *   **Readability**: Variable and function names are descriptive. The logic is straightforward and easy to follow.
    *   **Modularity**: Excellent modularity with clear separation of concerns into `app.py`, `calculator.py`, and `operations.py`.
    *   **Type Hinting**: Extensive use of type hints (`-> None`, `: str`, `: float`, `Dict`, `Type`) significantly improves code clarity, maintainability, and allows for static analysis.
    *   **Docstrings/Comments**: While not extensively documented with docstrings for every method, the code is self-explanatory due to its simplicity and good naming. A class-level docstring for `Calculator` is present.

2.  **Design Patterns**:
    The primary design pattern used here is the **Strategy Pattern**.
    *   **Context**: The `Calculator` class acts as the context, holding a reference to various `Operation` objects.
    *   **Strategy Interface**: The `Operation` abstract base class defines the common interface (`execute` method) for all concrete strategies.
    *   **Concrete Strategies**: The `Add` and `Subtract` classes are concrete implementations of the `Operation` interface, each encapsulating a specific algorithm (addition, subtraction).
    This pattern allows the algorithm (the operation) to vary independently from the client (`Calculator` and `app.py`) that uses it.

    One could also argue for elements of the **Command Pattern**, where each `Operation` object could be seen as a command that encapsulates a request. However, given that the `Calculator` directly executes the `execute` method and doesn't typically store commands for undo/redo, Strategy is a more fitting description for the interchangeable algorithms.

3.  **Potential Issues**:
    *   **Limited Error Handling**: While `prompt_number` handles `ValueError` for non-numeric input, specific mathematical errors (e.g., division by zero if a `Divide` operation were added) are not explicitly handled beyond a generic `try-except Exception as e` in `app.py`.
    *   **Hardcoded Symbol Display**: In `app.py`, the `symbol` for the result display is hardcoded based on the operation name (`+` for "Add", `-` for "Subtract"). If new operations like "Multiply" or "Divide" were added, this logic would need to be updated. A better approach would be to include a `symbol` attribute in the `Operation` ABC and its concrete implementations.
        ```python
        # In operations.py
        class Operation(ABC):
            name: str
            symbol: str # New attribute

            @abstractmethod
            def execute(self, a: float, b: float) -> float:
                ...

        class Add(Operation):
            name = "Add"
            symbol = "+" # Concrete symbol
            # ...

        # In app.py
        # ...
        op_symbol = calc.menu_items[choice].symbol # Use the symbol from the operation object
        print(f"Result: {a} {op_symbol} {b} = {result}")
        # ...
        ```
    *   **Input Choice Flexibility**: The current input choice (`1`, `2`) is tied to the registration order. While `register_operation` allows custom keys, the `_register_default_operations` hardcodes `1` and `2`. This is fine for a small app but could be more dynamic if operations were loaded from configuration.

4.  **Scalability**:
    *   **Operation Scalability**: Excellent. Adding new operations (e.g., Multiply, Divide, Power) is very straightforward. One only needs to:
        1.  Create a new class inheriting from `Operation`.
        2.  Implement its `execute` method and set its `name` (and `symbol` if the suggestion above is implemented).
        3.  Register the new operation in `Calculator._register_default_operations` or via `Calculator.register_operation`.
        No changes are required in `app.py` or the core `Calculator.compute` logic.
    *   **Application Scalability**: As a CLI tool, it's not designed for high-throughput or concurrent users. Its scalability is limited by the single-user, single-process nature of a CLI application. However, the core `Calculator` logic could easily be reused in a web service or GUI application.

5.  **Maintainability**:
    *   **High Maintainability**: The clear separation of concerns and the use of the Strategy pattern make this codebase highly maintainable.
    *   **Easy to Understand**: The code is simple, direct, and uses standard Python constructs.
    *   **Extensibility**: As noted under scalability, adding new features (operations) is very easy and low-risk, as it involves adding new files/classes rather than modifying existing, tested code.
    *   **Debugging**: The modular structure would make debugging relatively easy, as issues can often be isolated to a specific operation or the UI layer.

---