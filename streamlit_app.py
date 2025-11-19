import streamlit as st
from calculator import Calculator

def main():
    st.set_page_config(page_title="Calculator App", layout="centered")
    st.title("Simple Calculator")
    st.write("A basic calculator built with Streamlit")

    # Initialize calculator
    calc = Calculator()

    # Create two columns for input
    col1, col2 = st.columns(2)

    with col1:
        first_number = st.number_input(
            "First Number",
            value=0.0,
            step=0.1,
            format="%.2f"
        )

    with col2:
        second_number = st.number_input(
            "Second Number",
            value=0.0,
            step=0.1,
            format="%.2f"
        )

    # Operation selection
    operation_names = {op.name: key for key, op in calc.menu_items.items()}
    selected_operation = st.selectbox(
        "Select Operation",
        options=list(operation_names.keys())
    )

    # Calculate button
    if st.button("Calculate", use_container_width=True):
        try:
            operation_key = operation_names[selected_operation]
            result = calc.compute(operation_key, first_number, second_number)

            # Display result
            st.success(f"✓ Result")
            st.metric(
                label=f"{first_number} {selected_operation.lower()} {second_number}",
                value=f"{result:.2f}"
            )
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
