from langchain.schema import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from schema import Answer_format,Overallstate
from langgraph.graph import StateGraph, START, END

from statefuncs import *


os.environ["GOOGLE_API_KEY"] =os.getenv("GOOGLE_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.2)


section_builder = StateGraph(Overallstate)

section_builder.add_node("context_retriever", context_retriever)
section_builder.add_node("First_explainer", First_explainer)
section_builder.add_node("second_explainer", second_explainer)
section_builder.add_edge(START, "context_retriever")
section_builder.add_edge("context_retriever", "First_explainer")
section_builder.add_edge("First_explainer", "second_explainer")
section_builder.add_edge("second_explainer", END)
section_builder_subagent = section_builder.compile()

