import streamlit as st

# Title
st.title("Simple Streamlit App")

# User input
name = st.text_input("What's your name?")

# Display output
if name:
    st.write(f"Hello, {name}! 👋")
