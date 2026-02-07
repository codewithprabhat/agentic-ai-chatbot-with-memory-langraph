import streamlit as st
from src.langraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")