import streamlit as st
import random

st.title("Guess the Number")

mode = st.selectbox("Choose a mode:", ["Easy", "Medium", "Hard"])

if mode == "Easy":
    min_val, max_val = 1, 10
elif mode == "Medium":
    min_val, max_val = 1, 50
else:
    min_val, max_val = 1, 100

number_to_guess = int (st.text_input("Enter the number to guess:", type="default"))

guess = st.number_input(f"Guess a number between {min_val} and {max_val}:", min_value=min_val, max_value=max_val)

if st.button("Submit"):
    if guess < number_to_guess:
        st.write("Too low!")
    elif guess > number_to_guess:
        st.write("Too high!")
    else:
        st.write("Congratulations! You found the number.")

st.write(f"Mode: {mode} ({min_val}-{max_val})")

