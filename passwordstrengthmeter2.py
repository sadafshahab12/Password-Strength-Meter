import streamlit as st
import re

# Custom CSS for styling
st.markdown(
    """
    <style>
    h1 {
        color: #FF4B4B; /* Change heading color */
        text-align: center;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #FF1C1C;
    }
    .feedback {
        color: #FF4B4B;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper and lower case
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0 - 9).")

    # Check special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Strength rating
    if score == 4:
        return "Strong Password!", feedback
    elif score == 3:
        return "Moderate Password - Consider adding more security features.", feedback
    else:
        return "Weak Password - Improve it using the suggestions above.", feedback


# App title
st.title("Password Strength Meter")

# Password input
password = st.text_input("Enter your password", type="password")

# Check password strength
if password:
    result, feedback = check_password_strength(password)
    st.subheader(result)
    for msg in feedback:
        st.markdown(f'<p class="feedback">{msg}</p>', unsafe_allow_html=True)
