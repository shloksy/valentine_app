import streamlit as st
import random

# Valentine's Day Question Page
st.title("Valentine's Day Question")

if st.button('Yes'):
    st.balloons()
    st.image('https://your-image-url-placeholder.com/image.jpg')  # Placeholder for your image
    st.write('You + Me Forever!')
else:
    messages = ["Are you sure?", "Think again!", "It's a tough question!", "Choices matter!"]
    random_message = random.choice(messages)
    st.button(random_message)
    st.write("No button is moving around!")  
    st.balloons()

# Note: Adjust the URL of the image to your preference.
