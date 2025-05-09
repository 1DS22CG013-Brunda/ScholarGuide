import streamlit as st

def show():
    st.title("📤 Eligible Scholarships")

    # Get the response from the session state
    if 'response' in st.session_state:
        # Display the response from Gemma 3
        st.write("🔍 Your matched scholarships:")
        st.write(st.session_state.response)
    else:
        st.write("No response available. Please submit the form to get results.")
