import streamlit as st
from app_pages import homepage, form_page, output_page

# Set page configuration
st.set_page_config(layout="wide", page_title="Scholarship Checker")

# Default page in session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Navigation with session-based selection
page = st.sidebar.radio(
    "Go to", 
    ("Home", "Form", "Output"), 
    index=["Home", "Form", "Output"].index(st.session_state.page)
)

# Save user selection back to session state
st.session_state.page = page

# Render Pages
if page == "Home":
    homepage.show()
elif page == "Form":
    form_page.show()
elif page == "Output":
    output_page.show()
