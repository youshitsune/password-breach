import streamlit as st
import pwnedpasswords as pp
from time import sleep

st.write("# Password breach checker")
password = st.text_input("Type in your password:")
if password:
    response = pp.check(password)
    if response == 0:
        st.success("Password hasn't been breached!!!", icon="✅")
    elif response > 0:
        st.error("Password has been breached!!!", icon="🚨")

