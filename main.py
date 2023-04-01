# main.py
import streamlit as st
import requests

key_prompt = "prompt"
if key_prompt not in st.session_state:
    st.session_state[key_prompt] = "I saw her standing there"

key_lylic = "lylic"
if key_lylic not in st.session_state:
    st.session_state[key_lylic] = "[Lylics will be generated below]"


def send_prompt():
    prompt = st.session_state[key_prompt]
    r = requests.post("http://127.0.0.1:8000/generate_lylic", 
                    headers = {'Content-Type': 'application/json'},
                    json = {'lylic_prompt': prompt})
    st.session_state[key_lylic] = r.json()['lylic']


def main():
    st.text_input("Prompt", key=key_prompt) # (A)

    st.button("Generate", on_click=send_prompt) # (C)
    st.write(st.session_state[key_lylic])

if __name__ == "__main__":
    main()