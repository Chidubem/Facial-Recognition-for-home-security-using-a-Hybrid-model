import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.title("About This App")
st.markdown("""
**Face Recognition App** built with Streamlit.

- Developed using `face_recognition`, `OpenCV`, and `Streamlit`
- Allows image or webcam-based facial verification
- Adjustable tolerance settings
- Dataset management for enrolled users
""")