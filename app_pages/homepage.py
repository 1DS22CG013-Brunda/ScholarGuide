import streamlit as st
import base64
import os

# Background image loader function
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Show function for homepage
def show():
    # Add background image from assets folder
    add_bg_from_local("assets/bg.jpg")  # make sure this path is correct

    # Add styled header and paragraph
    st.markdown(
        """
        <style>
            .overlay {
                background-color: rgba(255, 255, 255, 0.75);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                margin-top: 2rem;
            }

            .overlay h1 {
                font-size: 3.5rem;
                font-weight: 800;
                color: #1f2937;
                margin-bottom: 0.5rem;
            }

            .overlay p {
                font-size: 1.25rem;
                font-style: italic;
                color: #374151;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
        </style>

        <div class='overlay'>
            <h1>Scholarship Eligibility Checker 🎓
     </h1>
            <p>"🚀Find scholarships personalized for your background and goals💡"</p>
        </div>
        """,
        unsafe_allow_html=True
    )
