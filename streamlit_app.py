import streamlit as st
from calculator import Calculator

# Initialize calculator
calc = Calculator()

# Set page config
st.set_page_config(page_title="Calculator", layout="centered")

# Title
st.title("Simple OOP Calculator")
st.write("A basic calculator UI built with Streamlit")

# Create columns for layout
col1, col2 = st.columns(2)

# Input for first number
with col1:
    a = st.number_input(
        label="First Number",
        value=0.0,
        step=1.0,
        format="%.2f"
    )

# Input for second number
with col2:
    b = st.number_input(
        label="Second Number",
        value=0.0,
        step=1.0,
        format="%.2f"
    )

# Operation selection
st.write("### Select Operation")
operation_options = {op.name: key for key, op in calc.menu_items.items()}
selected_operation = st.selectbox(
    label="Choose an operation",
    options=list(operation_options.keys()),
    index=0
)

# Calculate button
if st.button("Calculate", type="primary"):
    try:
        operation_key = operation_options[selected_operation]
        result = calc.compute(operation_key, a, b)
        st.success(f"**Result:** {a} {selected_operation.lower()} {b} = **{result}**")
    except Exception as e:
        st.error(f"Error: {e}")
