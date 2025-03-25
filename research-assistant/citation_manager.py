from pydantic import BaseModel
from typing import List

class ResearchPaper(BaseModel):
    title: str
    authors: List[str]
    source: str  # "arxiv" or "pubmed"
    url: str
    summary: str

class CitationManager:
    def __init__(self):
        self.papers = []
    
    def add_paper(self, paper: ResearchPaper):
        self.papers.append(paper)
    
    def generate_citations(self, format="APA"):
        return [f"{p.authors[0]} et al. ({p.year}). {p.title}. {p.source.upper()}." for p in self.papers]