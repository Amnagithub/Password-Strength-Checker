import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker by Amna", page_icon="🛅")
st.title("🛅 Password Strength Checker")
st.markdown("""### Welcome To the Ultimate Password Strength Checker! 🖐️
#### 🛅 This app checks the strength of your password. Enter your password in the text box below and  enter the button to check its strength and create a 💪 Strong Password""")

password=st.text_input("Enter your password here",type="password")

feedback = []

score = 0

if password :
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")
    if re.search(r"[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase characters.")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Password must contain at least one digit.")
    if re.search(r"[!@#$%^&*?/]", password):
            score += 1
    else:
        feedback.append("❌ Password must contain at least one special character(!@#$%^&*?/).")
    if score == 4:
        feedback.append("✅ Your Password is strong.🎉")
    elif score == 3:
        feedback.append("🟡 Your Password is weak.It coulde be stronger.")
    else:
        feedback.append("🔴 Your Password is very weak.Please make it stronger.")
    if feedback:
        st.markdown("### Improvement Suggestion:")
        for i in feedback:
            st.write(i)
else:
    st.info("Please enter a password to check its strength.")