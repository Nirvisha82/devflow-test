This repository contains a simple command-line interface (CLI) calculator application written in Python. It demonstrates an object-oriented design approach, specifically leveraging the Strategy pattern for handling different mathematical operations. The codebase has recently been extended to include more operations beyond just addition and subtraction.

## Repository Overview

1.  **Project Type**:
    This is a **CLI (Command-Line Interface) tool**. It's a standalone application that interacts with the user through text-based input and output in a terminal.

2.  **Architecture**:
    The application follows a modular and object-oriented architecture, clearly separating concerns into three main layers:
    *   **UI Layer (`app.py`)**: Responsible for user interaction, displaying menus, prompting for input, and presenting results.
    *   **Core Logic Layer (`calculator/calculator.py`)**: Manages the registration and dispatching of different mathematical operations. It acts as the "Context" in the Strategy design pattern.
    *   **Operations Layer (`calculator/operations.py`)**: Defines an abstract interface for operations and provides concrete implementations (strategies) for specific mathematical functions (e.g., addition, subtraction, division, multiplication, square, power).

    This design promotes extensibility, allowing new operations to be added with minimal changes to the core `Calculator` class or the `app.py` UI logic.

3.  **Technology Stack**:
    The project uses **pure Python 3**. It relies solely on Python's standard library (e.g., `abc` for abstract base classes, `typing` for type hints) without any external frameworks or third-party libraries.

4.  **Entry Points**:
    The main entry point for the application is `app.py`. When `app.py` is executed (e.g., `python app.py`), the `if __name__ == "__main__":` block ensures that the `main()` function is called. The `main()` function then initializes the `Calculator` and enters an interactive loop to handle user commands.

## File Analysis

### File: .gitignore

*   **Purpose**: Specifies intentionally untracked files and directories that Git should ignore.
*   **Role**: Keeps the repository clean by preventing various temporary files, build artifacts, environment-specific files (like `__pycache__`, `.venv`, `*.egg-info`), and IDE-related files from being committed. This is a comprehensive `.gitignore` suitable for most Python projects.
*   **Key Functions/Classes**: N/A (configuration file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.

### File: README.md

*   **Purpose**: Provides a brief introduction to the project.
*   **Role**: Serves as the primary documentation for users and developers, explaining the project's purpose and the operations it supports.
*   **Key Functions/Classes**: N/A (documentation file).
*   **Dependencies**: N/A.
*   **Business Logic**: N/A.
*   **Note**: The `README.md` is outdated, stating only "Addition" and "Substraction" are supported, while the code now supports more operations.

### File: app.py

*   **Purpose**: Implements the user interface and the main application loop for the calculator.
*   **Role**: It acts as the orchestrator, handling user interaction, input validation, and displaying results by interacting with the `Calculator` core logic.
*   **Key Functions/Classes**:
    *   `prompt_number(label: str) -> float`: A utility function that repeatedly prompts the user for a numeric input (float) until valid input is provided. It includes basic error handling for `ValueError`.
    *   `main() -> None`: The core application function.
        *   Initializes a `Calculator` instance.
        *   Enters an infinite loop to display the menu of available operations, get user choice, prompt for two numbers, and compute the result.
        *   Handles user exit commands (`q`, `quit`, `exit`).
        *   Validates the user's operation choice against the registered operations.
        *   Calls `calc.compute()` to delegate the actual calculation.
        *   Constructs a string to display the result, including a symbol for the operation.
        *   Includes a generic `try-except Exception as e` block to catch and print any errors during computation.
*   **Dependencies**:
    *   `calculator.Calculator`: Depends on the `Calculator` class to manage and perform operations.
*   **Business Logic**:
    *   User input/output management (prompting, displaying menus and results).
    *   Basic input validation (ensuring numeric input and valid operation choice).
    *   Orchestration of the calculation process by interacting with the `Calculator` object.
    *   Mapping operation names to display symbols.

### File: calculator/__init__.py

*   **Purpose**: Marks the `calculator` directory as a Python package and controls what symbols are exposed when the package is imported.
*   **Role**: Simplifies imports for users of the `calculator` package. Instead of requiring `from calculator.calculator import Calculator`, users can simply write `from calculator import Calculator`. The `__all__` variable explicitly defines the public API of the package, making it clear what is intended for external use.
*   **Key Functions/Classes**:
    *   Imports `Calculator` from `calculator.calculator`.
    *   Imports `Operation`, `Add`, `Subtract`, `Divide`, `Multiply`, `Square`, `Power` from `calculator.operations`.
    *   `__all__ = ["Calculator", "Operation", "Add", "Subtract", "Divide", "Multiply", "Square", "Power"]`: Defines the public interface of the `calculator` package.
*   **Dependencies**:
    *   `calculator.calculator`
    *   `calculator.operations`
*   **Business Logic**: None directly; it's purely for package structure and import management.

### File: calculator/calculator.py

*   **Purpose**: Implements the `Calculator` class, which manages and executes different mathematical operations.
*   **Role**: This is the central component that holds a collection of `Operation` objects (strategies) and dispatches computation requests to the appropriate operation based on a key. It acts as the "Context" in the Strategy design pattern, providing a consistent interface for clients (like `app.py`) to perform operations without knowing their specific implementations.
*   **Key Functions/Classes**:
    *   `class Calculator`:
        *   `__init__(self) -> None`: Initializes an empty dictionary `_operations` to store registered operations and calls `_register_default_operations()` to set up initial operations.
        *   `_register_default_operations(self) -> None`: Registers the `Add`, `Subtract`, `Divide`, `Multiply`, `Square`, and `Power` operations with keys "1" through "6" respectively. This method is the primary place to add or remove default operations.
        *   `register_operation(self, key: str, operation: Operation) -> None`: A public method allowing external code to register new operations with a unique string key. This is the main extensibility point.
        *   `@property menu_items(self) -> Dict[str, Operation]`: Provides read-only access to the dictionary of registered operations, which `app.py` uses to display the menu.
        *   `compute(self, key: str, a: float, b: float) -> float`: The core method to perform a calculation. It checks if the `key` exists in `_operations`, and if so, retrieves the corresponding `Operation` object and calls its `execute()` method with the given numbers `a` and `b`. Raises a `KeyError` if the operation key is not found.
*   **Dependencies**:
    *   `typing.Dict`, `typing.Type` (for type hints).
    *   `calculator.operations.Operation`, `Add`, `Subtract`, `Divide`, `Multiply`, `Square`, `Power`.
*   **Business Logic**:
    *   Management and registration of available mathematical operations.
    *   Delegation of actual computation to specific `Operation` instances.
    *   Ensuring that only registered operations can be executed.

### File: calculator/operations.py

*   **Purpose**: Defines the abstract base class for all calculator operations and provides concrete implementations for various mathematical functions.
*   **Role**: This file establishes the contract (interface) for any operation that can be performed by the `Calculator`. It defines the "Strategy" interface and implements several concrete "Strategies" in the Strategy design pattern.
*   **Key Functions/Classes**:
    *   `class Operation(ABC)`: An abstract base class that defines the common interface for all operations.
        *   `name: str`: An abstract attribute to hold the human-readable name of the operation (e.g., "Add", "Divide").
        *   `@abstractmethod execute(self, a: float, b: float) -> float`: An abstract method that concrete operations must implement to perform their specific calculation.
    *   `class Add(Operation)`: Implements addition (`a + b`).
    *   `class Subtract(Operation)`: Implements subtraction (`a - b`).
    *   `class Divide(Operation)`: Implements division (`a / b`).
    *   `class Multiply(Operation)`: Implements multiplication (`a * b`).
    *   `class Square(Operation)`: Implements a specific calculation `a * a + b * b`.
    *   `class Power(Operation)`: Implements exponentiation (`a ** b`).
*   **Dependencies**:
    *   `abc.ABC`, `abc.abstractmethod` (for defining abstract classes and methods).
*   **Business Logic**:
    *   Defines the common interface for all mathematical operations, ensuring consistency.
    *   Encapsulates the specific mathematical logic for each supported operation.

## System Relationships

1.  **Data Flow**:
    *   The user interacts with `app.py`, providing an operation choice and two numbers.
    *   `app.py` validates this input and passes the operation key (e.g., "1") and the numbers (`a`, `b`) to the `Calculator` instance's `compute` method.
    *   The `Calculator` instance, within its `compute` method, looks up the corresponding `Operation` object (e.g., an `Add` instance) from its internal `_operations` dictionary using the provided key.
    *   The `Calculator` then invokes the `execute` method on the retrieved `Operation` object, passing `a` and `b`.
    *   The `Operation` object performs its specific calculation and returns the `float` result.
    *   This result is returned from `compute` back to `app.py`.
    *   `app.py` then formats the result and displays it to the user.

2.  **Key Components**:
    *   **`app.py` (User Interface / Orchestrator)**: The entry point and the primary interface for user interaction.
    *   **`Calculator` class (Core Logic / Context)**: The central hub for managing and delegating operations, crucial for the system's extensibility.
    *   **`Operation` ABC (Strategy Interface)**: Defines the contract for all mathematical operations, enabling polymorphism.
    *   **Concrete Operation Classes (`Add`, `Subtract`, `Divide`, `Multiply`, `Square`, `Power`) (Concrete Strategies)**: Encapsulate the specific algorithms for each mathematical function.

3.  **Integration Points**:
    *   `app.py` integrates with `calculator.Calculator` by:
        *   Instantiating `Calculator` (`calc = Calculator()`).
        *   Accessing the `menu_items` property to dynamically display available operations (`for key, op in calc.menu_items.items():`).
        *   Calling the `compute` method to execute an operation (`result = calc.compute(choice, a, b)`).
    *   `calculator.Calculator` integrates with `calculator.operations` by:
        *   Instantiating concrete `Operation` objects during its initialization (`self.register_operation("1", Add())`).
        *   Storing these `Operation` objects in its `_operations` dictionary.
        *   Invoking the `execute()` method on the stored `Operation` objects when `compute` is called.

4.  **API/Interface Design**:
    *   **`Calculator` Public API**:
        *   `__init__()`: Constructor to initialize the calculator.
        *   `register_operation(key: str, operation: Operation)`: Allows dynamic registration of new operations.
        *   `menu_items` (property): Provides a dictionary of registered operations for display.
        *   `compute(key: str, a: float, b: float) -> float`: The method to trigger a calculation for a given operation key and two operands.
    *   **`Operation` Interface**:
        *   `name: str` (abstract attribute): Provides a human-readable name for the operation.
        *   `execute(a: float, b: float) -> float` (abstract method): The core method that concrete operations must implement to perform their specific calculation.

    This design ensures loose coupling, allowing the UI, the core calculator logic, and individual operation implementations to evolve independently.

## Development Insights

1.  **Code Quality**:
    *   **Overall Assessment**: The code quality is generally good, exhibiting a clean, modular, and object-oriented structure.
    *   **Readability**: Variable and function names are descriptive, and the logic is straightforward, making the codebase easy to understand.
    *   **Modularity**: Excellent separation of concerns is achieved by dividing the application into UI, core logic, and operation implementations across different files and classes.
    *   **Type Hinting**: Extensive use of type hints (`-> None`, `: str`, `: float`, `Dict`) significantly enhances code clarity, enables static analysis, and improves maintainability.
    *   **Docstrings/Comments**: The `Calculator` class has a good docstring, and the overall simplicity of the code makes it largely self-documenting.

2.  **Design Patterns**:
    The primary design pattern employed is the **Strategy Pattern**:
    *   **Context**: The `Calculator` class acts as the context, holding a collection of `Operation` objects.
    *   **Strategy Interface**: The `Operation` abstract base class defines the common interface (`execute` method) that all concrete strategies must adhere to.
    *   **Concrete Strategies**: The `Add`, `Subtract`, `Divide`, `Multiply`, `Square`, and `Power` classes are concrete implementations of the `Operation` interface, each encapsulating a specific mathematical algorithm.
    This pattern allows the algorithm (the operation) to vary independently from the client (`Calculator` and `app.py`) that uses it, promoting flexibility and extensibility.

3.  **Potential Issues**:
    *   **Outdated `README.md`**: The `README.md` file explicitly states that only "Addition" and "Substraction" are supported, which is no longer true given the expanded functionality in the code. This should be updated to reflect the current capabilities.
    *   **Hardcoded Symbol Display in `app.py`**: The logic for displaying the operation symbol in `app.py` is implemented using a long, nested ternary operator chain:
        ```python
        symbol = "+" if op_name == "Add" else ("-" if op_name == "Subtract" else ("/" if op_name == "Divide" else ("*" if op_name == "Multiply" else ("²" if op_name == "Square" else "^"))))
        ```
        This approach is fragile and difficult to maintain. Every time a new operation is added, this line of code in `app.py` must be manually updated. A more robust solution would be to include a `symbol` attribute directly within the `Operation` abstract base class and its concrete implementations.
        ```python
        # In calculator/operations.py
        class Operation(ABC):
            name: str
            symbol: str # New attribute
            # ...

        class Add(Operation):
            name = "Add"
            symbol = "+"
            # ...

        # In app.py
        # ...
        op_symbol = calc.menu_items[choice].symbol # Access symbol directly from the operation object
        print(f"Result: {a} {op_symbol} {b} = {result}")
        # ...
        ```
    *   **Ambiguous `Square` Operation**: The `Square` operation is named "Square" but its `execute` method calculates `a * a + b * b`. Typically, a "square" operation takes a single number and returns its square (e.g., `a * a`). The current implementation calculates the sum of squares of two numbers. This is either a misnomer or an unusual definition for "Square" in a basic calculator context. If it's intended to be `a^2 + b^2`, it should be renamed (e.g., `SumOfSquares`). If it's intended to be `a^2`, it should only take one argument or use `b` as a dummy.
    *   **Limited Specific Error Handling**: While `prompt_number` handles `ValueError`, the `app.py`'s `try-except Exception as e` is very broad. For operations like `Divide`, specific error handling for division by zero (`ZeroDivisionError`) would be beneficial to provide more user-friendly messages rather than a generic "Error: division by zero".

4.  **Scalability**:
    *   **Operation Scalability**: Excellent. The design pattern makes adding new operations highly scalable. A new operation simply requires creating a new class inheriting from `Operation`, implementing its `execute` method, and registering it with the `Calculator`. No modifications are needed in `app.py` (apart from the symbol display issue mentioned above) or the core `Calculator.compute` logic.
    *   **Application Scalability**: As a standalone CLI tool, its scalability is inherently limited to a single user and process. It is not designed for high-throughput or concurrent usage. However, the well-structured `calculator` package could easily be reused as a library within a larger, more scalable application (e.g., a web service or a GUI application).

5.  **Maintainability**:
    *   **High Maintainability**: The clear separation of concerns, modular design, and adherence to the Strategy pattern contribute to high maintainability.
    *   **Easy to Understand**: The code is straightforward, uses standard Python features, and is well-typed, making it easy for new developers to understand and contribute.
    *   **Extensibility**: Adding new features (specifically new mathematical operations) is very easy and low-risk, as it primarily involves adding new files/classes rather than modifying existing, tested code.
    *   **Debugging**: The modular structure would simplify debugging, as issues can often be isolated to a specific operation's implementation or the UI layer's interaction logic. The main area for improvement in maintainability is addressing the hardcoded symbol display in `app.py`.