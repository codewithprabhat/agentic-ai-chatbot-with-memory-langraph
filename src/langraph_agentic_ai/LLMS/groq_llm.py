import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls: dict):
        self.user_controls = user_controls
    
    def get_groq_llm(self):
        try:
            groq_api_keys = self.user_controls["GROQ_API_KEY"]
            if not groq_api_keys:
                st.error("GROQ API key is not set")
                return None

            groq_model = self.user_controls["selected_groq_model"]
            if not groq_model:
                st.error("GROQ model is not set")
                return None

            llm = ChatGroq(api_key=groq_api_keys, model=groq_model)            
        except Exception as e:
            raise ValueError(f"Error Occured in GroqLLM: {e}")
            
        return llm