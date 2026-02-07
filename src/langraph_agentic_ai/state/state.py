from typing import Annotated, List
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List, add_messages]