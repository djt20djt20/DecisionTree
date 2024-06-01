import streamlit as st
from app import add  # Assuming add is a function defined in your existing code

st.title("My Streamlit App")

st.write("This is a simple Streamlit app.")

a = st.number_input("Enter a number:", value=0)
b = st.number_input("Enter another number:", value=0)

def add_numbers(a,b):
    return a+b

if st.button("Add"):
    result = add_numbers(a, b)
    st.write(f"The result is: {result}")
