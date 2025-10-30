from calculator import Calculator, Operation

def prompt_number(label: str) -> float:
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main() -> None:
    calc = Calculator()

    print("Simple OOP Calculator (Add, Subtract, Cube)")
    print("===========================================")

    while True:
        print("\nOptions:")
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

        selected_op: Operation = calc.menu_items[choice] # Get the selected operation object

        a: float
        b: float

        if selected_op.is_unary:
            a = prompt_number("number") # For unary operations, only one number is needed
            b = 0.0 # A dummy value for 'b', as unary operations ignore it
        else:
            a = prompt_number("first")
            b = prompt_number("second")

        try:
            result = calc.compute(choice, a, b)
            
            if selected_op.is_unary:
                print(f"Result: {selected_op.name}({a}) = {result}")
            else:
                # Original logic for binary operations
                symbol = "+" if selected_op.name == "Add" else "-"
                print(f"Result: {a} {symbol} {b} = {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
