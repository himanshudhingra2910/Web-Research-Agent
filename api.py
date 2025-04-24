from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import web_research_agent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class SummaryResponse(BaseModel):
    query: str
    summary: dict
    status: str

@app.get("/")
def root():
    return {"message": "Web Research Agent is running 🚀"}

@app.post("/research", response_model=SummaryResponse)
def get_summary(request: QueryRequest):
    summary_text = web_research_agent(request.query)
    
    return {
        "query": request.query,
        "summary": {
            "header": "📄 Summary",
            "content": summary_text.strip()
        },
        "status": "✅ Completed"
    }
