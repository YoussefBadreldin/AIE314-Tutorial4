from research_tools import search_arxiv, search_pubmed
from citation_manager import CitationManager, ResearchPaper
from summarizer import summarize_text

class AcademicResearchAssistant:
    def __init__(self):
        self.citation_manager = CitationManager()
    
    def search(self, query, source="arxiv"):
        if source == "arxiv":
            docs = search_arxiv(query)
        elif source == "pubmed":
            docs = search_pubmed(query)
        
        for doc in docs:
            paper = ResearchPaper(
                title=doc.metadata.get("title", "Untitled"),
                authors=doc.metadata.get("authors", []),
                source=source,
                url=doc.metadata.get("url", "#"),
                summary=doc.page_content[:500] + "..."
            )
            self.citation_manager.add_paper(paper)
        
        return docs
    
    def generate_report(self, format="markdown"):
        summaries = [paper.summary for paper in self.citation_manager.papers]
        summarized = summarize_text(summaries)
        
        if format == "markdown":
            return f"# Research Report\n\n## Summary\n{summarized}"
        elif format == "latex":
            return f"\\section{{Summary}}\n{summarized}"