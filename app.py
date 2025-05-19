import streamlit as st

st.title("Simple Unit Converter")

# Choose conversion type
conversion_type = st.selectbox("Select conversion type", [
    "Length (Meters to Feet)",
    "Length (Feet to Meters)",
    "Weight (Kilograms to Pounds)",
    "Weight (Pounds to Kilograms)",
    "Temperature (Celsius to Fahrenheit)",
    "Temperature (Fahrenheit to Celsius)"
])

# Input value
value = st.number_input("Enter the value:", format="%.2f")

# Convert based on selection
def convert():
    if conversion_type == "Length (Meters to Feet)":
        return value * 3.28084
    elif conversion_type == "Length (Feet to Meters)":
        return value / 3.28084
    elif conversion_type == "Weight (Kilograms to Pounds)":
        return value * 2.20462
    elif conversion_type == "Weight (Pounds to Kilograms)":
        return value / 2.20462
    elif conversion_type == "Temperature (Celsius to Fahrenheit)":
        return (value * 9/5) + 32
    elif conversion_type == "Temperature (Fahrenheit to Celsius)":
        return (value - 32) * 5/9

# Show result
if st.button("Convert"):
    result = convert()
    st.success(f"Converted Value: {result:.2f}")
