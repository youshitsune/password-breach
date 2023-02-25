import streamlit as st
import pwnedpasswords as pp

st.write("# Password breach checker")
password = st.text_input("Type in your password:")
st.write("Are you concered about security of this application? Check source code [here](https://github.com/youshitsune/password-breach).")
if password:
    response = pp.check(password)
    if response == 0:
        st.success("Password hasn't been breached!!!", icon="✅")
    elif response > 0:
        st.error("Password has been breached!!!", icon="🚨")

