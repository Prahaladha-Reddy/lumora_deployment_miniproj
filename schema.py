
from pydantic import BaseModel, Field
class Answer_format(BaseModel):
  answer:str=Field(description="Answer to the student question")

class Overallstate(BaseModel):
  query:str=Field(description="Student question here")
  Relevent_context:str=Field(description="Relevent context for the student question")
  answer_1:str
  answer_2:str