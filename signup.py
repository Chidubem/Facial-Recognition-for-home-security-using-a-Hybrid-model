import streamlit as st

def signup_page():
    st.subheader("Sign Up")

    new_username = st.text_input("Choose a username")
    new_password = st.text_input("Choose a password", type="password")

    if st.button("Sign Up", use_container_width=True):
        if new_username and new_password:
            if "users" not in st.session_state:
                st.session_state["users"] = {"admin": "admin123"}

            if new_username in st.session_state["users"]:
                st.error("Username already exists. Please choose another.")
            else:
                st.session_state["users"][new_username] = new_password
                st.success("Account created successfully! Please log in.")
        else:
            st.error("Please enter both username and password.")

    st.caption("Already have an account? Use the **Login** tab.")
