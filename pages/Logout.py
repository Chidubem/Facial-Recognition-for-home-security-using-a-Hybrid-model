import streamlit as st

st.set_page_config(page_title="Logout", layout="wide")

st.title("🚪 Logout")

if st.button("Click here to logout", use_container_width=True):
    # Clear session state
    st.session_state["logged_in"] = False

    # Optional: reset users dict if needed
    if "users" not in st.session_state:
        st.session_state["users"] = {"admin": "admin123"}

    st.success("You have been logged out!")

    # Redirect back to login/signup screen
    st.switch_page("app.py")
