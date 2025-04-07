from schema import Answer_format,Overallstate
from pipecone_index import vectorstoretest
from langchain.schema import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
import os


os.environ["GOOGLE_API_KEY"] =os.getenv("GOOGLE_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.2)


First_Retriever="""
You are an expert in signals and systems you were given a task to explain your student question given the context and the question help your student to understand

Context:
{context}


Question:
{question}
"""


Second_Retriever="""
You are an expert in control systems you were given a task to explain your student question given the context and the question help your student to understand

Context:
{context}


Question:
{question}
"""





def context_retriever(Overallstate):
  query=Overallstate.query
  relevent_data=vectorstoretest.similarity_search(  
    query,  
    k=5  
)
  cont=[i.page_content for i in relevent_data]
  context="\n".join(cont)
  return {"Relevent_context":context}



def First_explainer(Overallstate):
  query=Overallstate.query
  context=Overallstate.Relevent_context

  structured_llm = llm.with_structured_output(Answer_format)
  system_instructions_query = First_Retriever.format(
      context=context,
      question=query
  )


  results = structured_llm.invoke([
      SystemMessage(content=system_instructions_query),
      HumanMessage(content='Please help me with my question')
  ])

  return {"answer_1":results.answer}


def second_explainer(Overallstate):
  query=Overallstate.query
  context=Overallstate.Relevent_context

  structured_llm = llm.with_structured_output(Answer_format)
  system_instructions_query = Second_Retriever.format(
      context=context,
      question=query
  )

  results = structured_llm.invoke([
      SystemMessage(content=system_instructions_query),
      HumanMessage(content='Please help me with my question')
  ])
  return {"answer_2":results.answer}


