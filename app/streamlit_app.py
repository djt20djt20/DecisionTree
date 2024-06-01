import streamlit as st
from app.streamlit_app import add_numbers

st.title("My Streamlit App")

st.write("This is a simple Streamlit app.")

a = st.number_input("Enter a number:", value=0)
b = st.number_input("Enter another number:", value=0)


if st.button("Add"):
    result = add_numbers(a, b)
    st.write(f"The result is: {result}")
