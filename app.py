import streamlit as st
from login import login_page
from signup import signup_page

st.set_page_config(page_title="Face Recognition", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    # Hide sidebar completely
    hide_sidebar_style = """
        <style>
            [data-testid="stSidebar"] {display: none;}
            [data-testid="stSidebarNav"] {display: none;}
            [data-testid="stHeader"] {visibility: hidden;}
            .block-container {max-width: 400px; margin: auto; padding-top: 10%;} 
            div.stTabs [role="tablist"] {
                justify-content: center;
            }
            div[data-baseweb="tab"] {
                font-size: 16px;
                padding: 10px 20px;
            }
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)

    # Tabs for Login and Sign Up inside a centered container
    tab1, tab2 = st.tabs(["📝 Sign Up", "🔐 Login"])

    with tab1:
        signup_page()

    with tab2:
        login_page()

else:
    st.sidebar.success("Logged in ✅")
    st.switch_page("pages/Home.py")
