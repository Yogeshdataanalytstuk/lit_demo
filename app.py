import streamlit as st

# Title of the web app
st.title('Simple Streamlit App')

# Text input from the user
user_input = st.text_input("Enter some text")

# Numeric input from the user
number_input = st.number_input("Enter a number", min_value=1, max_value=100, step=1)

# Button to perform an action
if st.button('Multiply by 10'):
    # Displaying the entered text
    st.write(f'You entered: {user_input}')

    # Calculating and displaying the result of the multiplication
    result = number_input * 10
    st.write(f'The result of multiplying {number_input} by 10 is {result}')
