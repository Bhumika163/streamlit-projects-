import streamlit as st

# Page config
st.set_page_config(page_title="Web Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed")
        else:
            result = num1 / num2
            st.success(f"Result: {result}")

    elif operation == "Exponentiation":
        result = num1 ** num2
        st.success(f"Result: {result}")

st.markdown("---")
st.caption("Built using Streamlit")
