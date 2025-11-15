
import streamlit as st

# Page config
st.set_page_config(page_title="Home Security System", page_icon="🏠")

# Welcome section
st.title("Welcome to Your Facial Recognition Home Security System")
st.markdown("""
This system uses advanced facial recognition technology to keep your home safe.  
Get real-time alerts via email whenever an unknown face is detected.  

Easily select the camera you want to monitor and activate the system below.  
Our goal is to provide a user-friendly and reliable security solution for every home.
""")

st.markdown("---")  # horizontal line

# Camera selection and activation controls
camera_options = ["Front Door Camera", "Backyard Camera", "Garage Camera", "Living Room Camera"]
selected_camera = st.selectbox("Select the Camera to Monitor:", camera_options)

if st.button("Activate Monitoring"):
    st.success(f"Monitoring started on: {selected_camera}")
    # Here, call your facial recognition and email alert functions
else:
    st.info("Select a camera and click 'Activate Monitoring' to begin.")

# Footer or additional info (optional)
st.markdown("---")
st.caption("© 2025 Home Security System | Powered by Facial Recognition and Email Alerts")
