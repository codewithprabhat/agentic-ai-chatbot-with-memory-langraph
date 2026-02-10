from langgraph.graph import StateGraph, START, END
from src.langraph_agentic_ai.state.state import State
from src.langraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langraph_agentic_ai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langraph_agentic_ai.tools.search_tool import get_tools, create_search_tool
from langgraph.prebuilt import tools_condition



class GraphBuilder:
    def __init__(self, model, use_case):
        self.model = model
        self.graph_builder = StateGraph(State)
        self.use_case = use_case
    
    def basic_chatbot_graph(self):
        """
            Builds a basic chatbot graph using LangGraph.
            This method initializes a chatbot node using the `BasicChatbotNode` class 
            and integrates it into the graph. The chatbot node is set as both the 
            entry and exit point of the graph.
        """

        chatbot_node = BasicChatbotNode(self.model)
        self.graph_builder.add_node("chatbot", chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_graph(self):
        """
            Builds an advanced chatbot graph with tool integration.
            This method creates a chatbot graph that includes both a chatbot node 
            and a tool node. It defines tools, initializes the chatbot with tool 
            capabilities, and sets up conditional and direct edges between nodes. 
            The chatbot node is set as the entry point.
        """

        tools = get_tools()
        tool_node = create_search_tool(tools)

        self.chatbot_with_tool_node = ChatbotWithToolNode(self.model)
        chatbot_node = self.chatbot_with_tool_node.create_chatbot(tools)


        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)
       

    def setup_graph(self):
        """
        Sets up the graph for the selected use case.
        """
        if self.use_case == "Basic Chatbot":
            self.basic_chatbot_graph()
        elif self.use_case == "Chatbot With Web":
            self.chatbot_with_tools_graph()
        
        return self.graph_builder.compile()