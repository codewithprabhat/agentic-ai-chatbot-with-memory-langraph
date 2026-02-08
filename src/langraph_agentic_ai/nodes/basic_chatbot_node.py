from src.langraph_agentic_ai.state import State


class BasicChatbotNode:
    """
        Basic Chatbot node implementation
    """
    def __init__(self, model):
        self.model = model

    def process(self, state: State):
        """
            Processes the input state and generates a chatbot response.
        """
        return {"messages": self.model.invoke(state["messages"])}
