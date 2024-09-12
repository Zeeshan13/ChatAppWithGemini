import streamlit as st

def set_background():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://www.bing.com/th?id=OHR.GrandPrismaticEN-US2923792701_1920x1080.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
