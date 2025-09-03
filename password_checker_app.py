import streamlit as st
import re
import os

# -----------------------------
# Load common passwords
# -----------------------------
# Make sure common_passwords.txt is in the same folder as this app
common_file = "common_passwords.txt"

if os.path.exists(common_file):
    with open(common_file, "r") as f:
        common_passwords = [line.strip() for line in f.readlines()]
else:
    common_passwords = []
    st.error(f"Error: {common_file} not found in the folder!")

# -----------------------------
# App title
# -----------------------------
st.title("Password Strength Checker")

# -----------------------------
# Password input
# -----------------------------
password = st.text_input("Enter your password to check its strength", type="password")

if password:
    # Check if password is common first
    if password in common_passwords:
        st.warning("This password is very common and unsafe! Please choose a different one.")
    else:
        # Initialize strength score
        strength = 0

        # Criteria checks
        if len(password) >= 8:
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[a-z]", password):
            strength += 1
        if re.search(r"[0-9]", password):
            strength += 1
        if re.search(r"[^A-Za-z0-9]", password):
            strength += 1

        # Determine strength
        if strength <= 2:
            st.error("Weak")
        elif strength == 3 or strength == 4:
            st.warning("Moderate")
        else:
            st.success("Very Strong")

        # Optional suggestions
        st.write("Tips to make your password stronger:")
        if len(password) < 8:
            st.write("- Use at least 8 characters")
        if not re.search(r"[A-Z]", password):
            st.write("- Include at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            st.write("- Include at least one lowercase letter")
        if not re.search(r"[0-9]", password):
            st.write("- Include at least one number")
        if not re.search(r"[^A-Za-z0-9]", password):
            st.write("- Include at least one special character")
