"""# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from section_builder_subagent import invoke_agent

app = FastAPI()

class QueryInput(BaseModel):
    query: str
    Relevent_context: str = ""

@app.post("/ask")
async def ask_question(data: QueryInput):
    output = invoke_agent(data.query, data.Relevent_context)
    return {"response": output}
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

from config import settings
from section_builder_subagent import invoke_agent

app = FastAPI(title=settings.PROJECT_NAME)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pydantic input model
class QueryInput(BaseModel):
    query: str
    Relevent_context: str = ""

@app.post("/ask")
async def ask_question(data: QueryInput):
    try:
        output = invoke_agent(data.query, data.Relevent_context)
        return {"response": output}
    except Exception as e:
        logger.error(f"Error while processing request: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong while processing the query.")


@app.get("/health")
def health_check():
    return {"status": "ok"}
