import streamlit as st
from src.langraph_agentic_ai.graph import graph_builder
from src.langraph_agentic_ai.ui.streamlit_ui.load_ui import LoadStreamlitUI
from src.langraph_agentic_ai.LLMS.groq_llm import GroqLLM
from src.langraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langraph_agentic_ai.ui.streamlit_ui.display_result import DisplayResultStreamlitUI

def load_langgraph_agenticai_app():
    ui = LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_input)
            model = obj_llm_config.get_groq_llm()
            if not model:
                st.error("Error: Failed to load the model.")
                return

            use_case = user_input["selected_usecase"]
            print("Use Case: ", use_case)
            if not use_case:
                st.error("Error: Failed to load the use case.")
                return

            graph_builder = GraphBuilder(model, use_case)
            try:
                graph = graph_builder.setup_graph()
                DisplayResultStreamlitUI(use_case, graph, user_message).display_result()
            except Exception as e:
                st.error(f"Error: Graph set up failed- {e}")
                return
               
        except Exception as e:
            st.error(f"Error: {e}")
            return