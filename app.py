from calculator import Calculator
from calculator.operations import Square, Add, Subtract # Import specific operation classes for type checking

def prompt_number(label: str) -> float:
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main() -> None:
    calc = Calculator()

    print("Simple OOP Calculator") # Updated title to be more general
    print("=====================")

    while True:
        print("\nOptions:")
        # Dynamically display all registered operations
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

        selected_operation = calc.menu_items[choice]

        # Prompt for numbers based on the operation type
        a = prompt_number("first")
        b = 0.0 # Initialize b with a dummy value. It will be updated for binary ops.

        # If the operation is Square, it's unary, so we only need 'a'.
        # 'b' will be ignored by Square.execute(). For other operations, we need 'b'.
        if not isinstance(selected_operation, Square):
            b = prompt_number("second")

        try:
            result = calc.compute(choice, a, b)
            op_name = selected_operation.name

            # Format the output string based on the operation type
            if isinstance(selected_operation, Square):
                print(f"Result: Square of {a} = {result}")
            elif isinstance(selected_operation, Add):
                print(f"Result: {a} + {b} = {result}")
            elif isinstance(selected_operation, Subtract):
                print(f"Result: {a} - {b} = {result}")
            else:
                # Generic display for any other future binary operations
                print(f"Result: {op_name} of {a} and {b} = {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
