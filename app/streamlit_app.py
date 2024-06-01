import streamlit as st
from utils import add_numbers
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("Starting Streamlit app")
st.title("My Streamlit App")

st.write("This is a simple Streamlit app.")

a = st.number_input("Enter a number:", value=0)
b = st.number_input("Enter another number:", value=0)


if st.button("Add"):
    result = add_numbers(a, b)
    st.write(f"The result is: {result}")
