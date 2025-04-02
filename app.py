import streamlit as st
import time

# Define the response generator
def response_generator(text, typing_speed=0.1):
    for word in text.split():
        yield word + " "
        time.sleep(typing_speed)  # Simulate typing delay

# Streamlit layout
st.title("Streamlit Chat Message with Typing Effect")

# Create an empty placeholder for the chat message
message_placeholder = st.empty()

# Initialize a chat message with the sender
with st.chat_message("assistant"):
    # Use the response generator to stream words one by one
    full_message = ""
    for word in response_generator("Hello! This is a typing animation in a chat message.", typing_speed=0.2):
        full_message += word
        message_placeholder.markdown(f"<div>{full_message}</div>", unsafe_allow_html=True)  # Update chat message
