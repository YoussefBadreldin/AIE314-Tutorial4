from fastapi import FastAPI
from main import AcademicResearchAssistant

app = FastAPI()
research_assistant = AcademicResearchAssistant()

@app.post("/search")
async def search_articles(query: str, source: str = "arxiv"):
    return research_assistant.search(query, source)

@app.post("/report")
async def generate_report(format: str = "markdown"):
    return research_assistant.generate_report(format)