import streamlit as st
import pandas as pd
import os

st.title("📜 Recognition History")

HISTORY_FILE = "recognition_history.csv"

# Load history safely
if "history" not in st.session_state:
    if os.path.exists(HISTORY_FILE):
        try:
            df = pd.read_csv(HISTORY_FILE)
            st.session_state.history = df.to_dict("records") if not df.empty else []
        except Exception:
            st.session_state.history = []
    else:
        st.session_state.history = []

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df.drop(columns=["Snapshot"], errors="ignore"), use_container_width=True)

    # Show snapshots of unknowns in dropdown format
    st.subheader("📸 Unknown Faces Detected")
    for record in st.session_state.history:
        snapshot_path = record.get("Snapshot", "")

        if isinstance(snapshot_path, str) and snapshot_path.strip() != "" and os.path.exists(snapshot_path):
            with st.expander(f"Unknown detected at {record['Time']}"):
                st.image(snapshot_path, caption=f"Unknown at {record['Time']}", width=250)

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download History as CSV", csv, "recognition_history.csv", "text/csv")

    # Clear history
    if st.button("🧹 Clear History"):
        st.session_state.history = []
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        st.success("History cleared!")
else:
    st.info("No recognition history available yet.")
