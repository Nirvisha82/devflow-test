import streamlit as st
from calculator import Calculator

# Page configuration
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🧮 Simple Calculator")
st.markdown("A simple calculator UI built with Streamlit")
st.markdown("---")

# Initialize calculator
calc = Calculator()

# Create columns for layout
col1, col2 = st.columns(2)

# Input section
with col1:
    st.subheader("Inputs")
    first_number = st.number_input(
        "First Number",
        value=0.0,
        step=0.1,
        format="%.2f"
    )

with col2:
    st.subheader("Inputs")
    second_number = st.number_input(
        "Second Number",
        value=0.0,
        step=0.1,
        format="%.2f"
    )

# Operation selection
st.subheader("Select Operation")

# Create operation buttons in columns
operation_cols = st.columns(len(calc.menu_items))

selected_operation = None
for idx, (key, operation) in enumerate(calc.menu_items.items()):
    with operation_cols[idx]:
        if st.button(operation.name, use_container_width=True):
            selected_operation = key

# Perform calculation and display result
if selected_operation is not None:
    try:
        result = calc.compute(selected_operation, first_number, second_number)
        op_name = calc.menu_items[selected_operation].name
        symbol = "+" if op_name == "Add" else ("-" if op_name == "Subtract" else ("/" if op_name == "Divide" else ("*" if op_name == "Multiply" else "²")))
        
        # Display result in a nice format
        st.markdown("---")
        st.subheader("Result")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.metric("First Number", first_number)
        with col2:
            st.metric("Operation", symbol)
        with col3:
            st.metric("Second Number", second_number)
        
        st.success(f"**Result: {first_number} {symbol} {second_number} = {result}**", icon="✅")
    except Exception as e:
        st.error(f"Error: {e}", icon="❌")
