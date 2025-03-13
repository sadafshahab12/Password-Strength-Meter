import streamlit as st

st.set_page_config(page_title="Password Strength Meter", layout="wide")
st.title("Password Strength Meter")
st.write("Lock it down: Strength matters! 🔒💪")

COMMON_PASSWORD = ["password", "123456", "12345678", "1234", "qwerty", "admin", "letmein", "welcome"]
def check_password_strength(password):
    length = len(password)
    has_upper = any(
        char.isupper() for char in password
    )  # built-in string methods isupper()
    has_lower = any(
        char.islower() for char in password
    )  # built-in string methods islower()
    has_digit = any(
        char.isdigit() for char in password
    )  # built-in string methods isdigit()
    has_special = any(
        not char.isalnum() for char in password
    )  # built-in string methods isalnum()
    is_common = password.lower() in COMMON_PASSWORD

    # Based on the value of strength, it categorizes the password as Weak, Medium, or Strong.
    strength = 0
    feedback = []

    # first we check length
    if length >= 8:
        strength += 1
    else:
        feedback.append("Password should be atleast 8 characters long")

    # 2 : Now we check uppercase in password
    if has_upper:
        strength += 1
    else:
        feedback.append("Password should have at least one uppercase letter")
    # 3 : then we check lower case letter
    if has_lower:
        strength += 1
    else:
        feedback.append("Password should have at least one lowercase letter")

    # 4 : check digit in password
    if has_digit:
        strength += 1
    else:
        feedback.append("Password should have at least one digit")

    # 5 : check special character in password
    if has_special:
        strength += 1
    else:
        feedback.append("Password should have at least one special character")

    # now we will check strength level of password
    if strength == 5:
        return "Strong", "Your Password is Strong!"
    elif strength >= 3:
        return "Medium", "Your Password is medium! " + " ".join(feedback)
    else:
        return "Weak", "Your Password is weak!" + " ".join(feedback)


def main():
    
    password = st.text_input("Enter your password", type="password")
    if password:
        # check password strength
        strength, feedback = check_password_strength(password)

        # display strength and feedback
        if strength == "Strong":
            st.success(f"Strength: {strength}")
        elif strength == "Medium":
            st.warning(f"Strenth: {strength}")
        else:
            st.error(f"Strength : {strength}")
        st.write(feedback)


# now run the app
if __name__ == "__main__":
    main()

st.write("My Profile")

