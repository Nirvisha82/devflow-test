from calculator import Calculator

def prompt_number(label: str) -> float:
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main() -> None:
    calc = Calculator()

    print("Simple OOP Calculator (Add, Subtract, Multiply)") # Updated title
    print("===============================================")

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

        a = prompt_number("first")
        b = prompt_number("second")

        try:
            result = calc.compute(choice, a, b)
            op_name = calc.menu_items[choice].name
            # Dynamically determine the symbol based on operation name
            symbol = "?"
            if op_name == "Add":
                symbol = "+"
            elif op_name == "Subtract":
                symbol = "-"
            elif op_name == "Multiply": # Added multiplication symbol
                symbol = "*"

            print(f"Result: {a} {symbol} {b} = {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
