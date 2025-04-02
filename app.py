import streamlit as st
import time

# Define the response generator
def response_generator(text, typing_speed=0.1):
    for word in text.split():
        yield word + " "
        time.sleep(typing_speed)  # Simulate typing delay

# Streamlit layout
st.title("Streamlit Chat Message with Typing Effect")

# Initialize a chat message with the sender
with st.chat_message("assistant"):
    # Use the response generator to stream words one by one
    for word in response_generator("Hello! This is a typing animation in a chat message.", typing_speed=0.2):
        st.chat_message("assistant").write(word)
