import streamlit as st

def login_page():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        if "users" not in st.session_state:
            st.session_state["users"] = {"admin": "admin123"}

        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.session_state["logged_in"] = True
            st.success("Login successful!")

            # ✅ Immediately redirect to About page
            st.switch_page("pages/Home.py")

        else:
            st.error("Invalid username or password")

    st.caption("Don't have an account? Use the **Sign Up** tab.")
