import streamlit as st

st.title("Even or Odd Checker")


number = st.number_input("Enter a number", step=1, format="%d")


if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{int(number)} is Even")
    else:
        st.info(f"{int(number)} is Odd")