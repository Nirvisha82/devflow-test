import streamlit as st
from calculator import Calculator

# Set page configuration
st.set_page_config(
    page_title="Calculator UI",
    page_icon="🧮",
    layout="centered"
)

# Title and description
st.title("🧮 Calculator Application")
st.markdown("A simple calculator UI built with Streamlit")
st.markdown("---")

# Initialize calculator
calc = Calculator()

# Create two columns for layout
col1, col2 = st.columns(2)

# Get available operations
operations = calc.menu_items
operation_names = {key: op.name for key, op in operations.items()}

# Select operation
st.subheader("Select Operation")
selected_op_name = st.selectbox(
    "Choose an operation:",
    options=list(operation_names.values()),
    index=0
)

# Find the key for the selected operation
selected_key = None
for key, name in operation_names.items():
    if name == selected_op_name:
        selected_key = key
        break

st.markdown("---")

# Input section
st.subheader("Enter Numbers")

# Create columns for input fields
input_col1, input_col2 = st.columns(2)

with input_col1:
    first_number = st.number_input(
        "First Number",
        value=0.0,
        step=0.1,
        format="%.2f"
    )

with input_col2:
    second_number = st.number_input(
        "Second Number",
        value=0.0,
        step=0.1,
        format="%.2f"
    )

st.markdown("---")

# Calculate button
if st.button("Calculate", use_container_width=True):
    try:
        result = calc.compute(selected_key, first_number, second_number)
        
        # Display result in a nice format
        st.success("✅ Calculation Successful!")
        
        # Create columns for result display
        result_col1, result_col2 = st.columns(2)
        
        with result_col1:
            st.metric(label="Operation", value=selected_op_name)
        with result_col2:
            st.metric(label="Result", value=f"{result:.2f}")
        
        st.info(f"**{first_number}** {selected_op_name} **{second_number}** = **{result:.2f}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

st.markdown("---")
st.markdown("*Built with Streamlit and Python*")
