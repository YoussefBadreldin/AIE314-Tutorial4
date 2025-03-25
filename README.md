# AIE314-Tutorial4: AI Support & Research Assistant

Two production-ready AI applications built with LangChain:
-  **Enterprise Support System** - AI customer support agent
-  **Academic Research Assistant** - Paper search and summarization

##  Quick Start

### Prerequisites
- Python 3.8+
- Git
- PowerShell/Terminal

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/AIE314-Tutorial4.git
cd AIE314-Tutorial4

# Set up Enterprise Support
cd enterprise-support
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt

# Set up Research Assistant (in new terminal)
cd ../research-assistant
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt

### Enterprise Support System
Features
Instant answers from product docs

Ticket creation system

Order status checks

Conversation memory

Usage Examples

# Ask product question
curl -X POST http://localhost:8000/support \
  -H "Content-Type: application/json" \
  -d '{"query":"How do I reset Product X?"}'

# Create support ticket
curl -X POST http://localhost:8000/support \
  -H "Content-Type: application/json" \
  -d '{"query":"Create ticket for broken screen (Order #12345)"}'

### Academic Research Assistant
Features
Search ArXiv/PubMed papers

Generate Markdown/LaTeX reports

Automatic citations

Paper summarization

Usage Examples

  # Search papers
curl -X POST http://localhost:8001/search \
  -H "Content-Type: application/json" \
  -d '{"query":"quantum computing","source":"arxiv"}'

# Generate report
curl -X POST http://localhost:8001/report \
  -H "Content-Type: application/json" \
  -d '{"format":"markdown"}'