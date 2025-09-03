
import streamlit as st
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength

st.title("🔐 Password Strength Checker")
st.write("Enter your password to check its strength:")

password = st.text_input("Password", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")

    if strength != "Very Strong":
        st.write("**Tips to improve your password:**")
        if len(password) < 8:
            st.write("- Make it at least 8 characters long.")
        if re.search(r"\d", password) is None:
            st.write("- Add at least one number.")
        if re.search(r"[A-Z]", password) is None:
            st.write("- Add at least one uppercase letter.")
        if re.search(r"[a-z]", password) is None:
            st.write("- Add at least one lowercase letter.")
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None:
            st.write("- Add at least one special character (!@#$%^&* etc).")
