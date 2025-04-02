import streamlit as st
def chat_stream(prompt):
    response = f'You said, "{prompt}" ...interesting.'


    for char in response:
        yield char
        time.sleep(.02)

st.write_stream(chat_stream())
