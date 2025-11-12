import streamlit as st
from calculator import Calculator

# Page configuration
st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1.1rem;
        border-radius: 0.5rem;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #ffcccc;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff0000;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize calculator
calc = Calculator()

# Title
st.title("🧮 Simple Calculator")
st.markdown("---")

# Sidebar for information
with st.sidebar:
    st.header("About")
    st.info("""
    This is a simple OOP-based calculator with the following operations:
    - **Add**: Addition of two numbers
    - **Subtract**: Subtraction of two numbers
    - **Multiply**: Multiplication of two numbers
    - **Divide**: Division of two numbers
    - **Square**: Sum of squares of two numbers (a² + b²)
    """)
    st.markdown("---")
    st.markdown("**Built with:** Python, Streamlit & OOP Design Patterns")

# Main content area
col1, col2 = st.columns(2)

# Operation selection
with col1:
    st.subheader("Select Operation")
    operation_names = [op.name for op in calc.menu_items.values()]
    selected_operation = st.selectbox(
        "Choose an operation:",
        operation_names,
        index=0,
        key="operation_select"
    )

# Find the key for the selected operation
selected_key = None
for key, op in calc.menu_items.items():
    if op.name == selected_operation:
        selected_key = key
        break

# Input numbers
with col2:
    st.subheader("Enter Numbers")

col1, col2 = st.columns(2)

with col1:
    num_a = st.number_input("First Number", value=0.0, step=0.1, key="num_a")

with col2:
    num_b = st.number_input("Second Number", value=0.0, step=0.1, key="num_b")

# Calculate button
if st.button("Calculate", use_container_width=True, type="primary"):
    try:
        result = calc.compute(selected_key, num_a, num_b)
        st.markdown(f"""
        <div class="result-box">
            <h3>Result</h3>
            <p><strong>{num_a}</strong> {selected_operation.lower()} <strong>{num_b}</strong> = <strong style="font-size: 1.5rem; color: #1f77b4;">{result}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    except ZeroDivisionError:
        st.markdown("""
        <div class="error-box">
            <strong>Error:</strong> Cannot divide by zero!
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"""
        <div class="error-box">
            <strong>Error:</strong> {str(e)}
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("**Tip:** Use the sidebar to learn more about each operation.")
