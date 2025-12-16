pip install streamlit

streamlit run first_app.py

# Import convention
>>> import streamlit as st

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = st.chat_input('Please enter the key: ')
key = st.chat_input(key)
new_message = ''

message = st.chat_input('Please enter a message: ')

for character in message:
	position = alphabet.find(character)

	new_position = (position + key) % 26

	new_character = alphabet[new_position]

	new_message += new_character
st.write(new_message)
