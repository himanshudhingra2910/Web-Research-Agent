# 🧠 Web Research Agent

An intelligent, real-time research assistant that searches the web, extracts key insights, and summarizes responses using Azure GPT-4o and SerpAPI.

Built for the **Masonry AI Agent Developer Assignment**.

---

## 🚀 Features

- 🔎 Real-time web search with SerpAPI
- 🕸️ Web scraping with BeautifulSoup
- 🤖 Content analysis using Azure OpenAI GPT-4o
- 🧠 Query understanding and synthesis
- ⚙️ Clean CLI + FastAPI backend
- 🧪 Tested with `pytest`
- 📦 Conda-based environment (`environment.yml`)

---

## 🧠 Architecture Overview

        ┌─────────────┐
        │ User Query  │
        └─────┬───────┘
              ▼
    ┌──────────────────┐
    │  SerpAPI Search  │
    └─────┬────────────┘
          ▼
┌───────────────────────┐
│  Web Scraper (HTML)   │
└─────┬─────────────────┘
      ▼
┌──────────────────────────────┐
│ Azure GPT-4o (Summarization)│
└─────┬────────────────────────┘
      ▼
┌──────────────────────────────┐
│  Structured Summary Output   │
└──────────────────────────────┘

---

## 📦 Tech Stack

| Tool      | Purpose                             |
|-----------|-------------------------------------|
| **FastAPI**  | Web API for structured queries     |
| **BeautifulSoup** | HTML parsing from web pages     |
| **Azure GPT-4o** | Intelligent summarization       |
| **SerpAPI**     | Real-time Google search results |
| **Python + Conda** | Reproducible environment        |

---

## 🛠️ Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/web-research-agent.git
cd web-research-agent
2. 🧪 Create Environment
Using Conda (recommended):
conda env create -f environment.yml
conda activate web-agent
3. 🔐 Setup Environment Variables
Create a .env file based on .env.example:
AZURE_OPENAI_API_KEY=your_azure_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_DEPLOYMENT_NAME=gpt-4o
SERPAPI_API_KEY=your_serpapi_key
4. 💻 Run CLI Agent
python main.py
You’ll be prompted to enter a query. The agent will search, scrape, and summarize.
5. 🌐 Run FastAPI Web Server
uvicorn api:app --reload
Open http://127.0.0.1:8000/docs to test via Swagger.
6. ✅ Run Tests
pytest tests/
📁 File Structure

web-research-agent/
├── app/                # Core agent logic
│   ├── agent.py
│   ├── analyzer.py
│   ├── scraper.py
│   ├── search_tool.py
├── config/             # .env loader
│   └── settings.py
├── api.py              # FastAPI endpoint
├── main.py             # CLI interface
├── tests/              # Pytest file
├── environment.yml     # Conda env
├── .env.example        # API key template
├── .gitignore
└── README.md
📹 Loom Demo + Submission

Link to Loom (to be added)
🤝 Author

Himanshu Dhingra
AI Developer Intern at R Systems
himanshudhingra2910@gmail.com
GitHub
