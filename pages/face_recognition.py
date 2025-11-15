import streamlit as st
import cv2
import face_recognition as frg
import yaml
import pandas as pd
import os
from datetime import datetime
from utils.utils import recognize, build_dataset

# ================= Config =================
cfg = yaml.load(open('config.yaml','r'), Loader=yaml.FullLoader)
PICTURE_PROMPT = cfg['INFO']['PICTURE_PROMPT']
WEBCAM_PROMPT = cfg['INFO']['WEBCAM_PROMPT']

st.title("🧠 Facial Recognition System")

# Sidebar
menu = ["Picture", "Webcam"]
choice = st.sidebar.selectbox("Input type", menu)
TOLERANCE = st.sidebar.slider("Tolerance", 0.0, 1.0, 0.44, 0.01)

st.sidebar.title("Student Information")
name_container = st.sidebar.empty()
id_container = st.sidebar.empty()
name_container.info('Name: Unknown')
id_container.success('ID: Unknown')

# ================= History Setup =================
HISTORY_FILE = "recognition_history.csv"
if "history" not in st.session_state:
    if os.path.exists(HISTORY_FILE):
        try:
            df = pd.read_csv(HISTORY_FILE)
            st.session_state.history = df.to_dict("records") if not df.empty else []
        except Exception:
            st.session_state.history = []
    else:
        st.session_state.history = []

def log_recognition(user, confidence, result, frame=None):
    """Log recognition attempts into history and save unknown snapshots"""
    snapshot_path = None
    if user == "Unknown" and frame is not None:
        os.makedirs("snapshots", exist_ok=True)
        snapshot_path = f"snapshots/unknown_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(snapshot_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    record = {
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "User": user,
        "Confidence (%)": round(confidence * 100, 2),
        "Result": result,
        "Snapshot": snapshot_path
    }
    st.session_state.history.append(record)
    pd.DataFrame(st.session_state.history).to_csv(HISTORY_FILE, index=False)

# ================= Picture Upload =================
if choice == "Picture":
    st.subheader("Upload Image(s)")
    st.write(PICTURE_PROMPT)
    uploaded_images = st.file_uploader("Upload", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)

    if uploaded_images:
        for image in uploaded_images:
            image = frg.load_image_file(image)
            image, name, id = recognize(image, TOLERANCE)

            # Show in sidebar
            name_container.info(f"Name: {name}")
            id_container.success(f"ID: {id}")

            # Show recognized image
            st.image(image)

            # ✅ Log recognition result
            confidence = 0.95
            result = "Access Granted" if name != "Unknown" else "Access Denied"
            log_recognition(name, confidence, result, frame=image)

    else:
        st.info("Please upload an image")

# ================= Webcam =================
elif choice == "Webcam":
    st.subheader("Webcam Capture")
    st.write(WEBCAM_PROMPT)
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    FRAME_WINDOW = st.image([])

    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to capture frame.")
            break

        image, name, id = recognize(frame, TOLERANCE)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Show in sidebar
        name_container.info(f"Name: {name}")
        id_container.success(f"ID: {id}")

        # Display webcam feed
        FRAME_WINDOW.image(image_rgb)

        # ✅ Log recognition result
        confidence = 0.90
        result = "Access Granted" if name != "Unknown" else "Access Denied"
        log_recognition(name, confidence, result, frame=image_rgb)

# ================= Developer Tools =================
with st.sidebar.form(key='my_form'):
    st.subheader("Developer Tools")
    submit_button = st.form_submit_button(label='REBUILD DATASET')
    if submit_button:
        with st.spinner("Rebuilding dataset..."):
            build_dataset()
        st.success("Dataset has been rebuilt.")
