#  Web Research Agent

An intelligent, real-time research assistant that searches the web, extracts key insights, and summarizes responses using Azure GPT-4o and SerpAPI.

Built for the **Masonry AI Agent Developer Assignment**.

---

##  Features

- 🔎 Real-time web search with SerpAPI
- 🕸️ Web scraping with BeautifulSoup
- 🤖 Content analysis using Azure OpenAI GPT-4o
- 🧠 Query understanding and synthesis
- ⚙️ Clean CLI + FastAPI backend
- 🧪 Tested with `pytest`
- 📦 Conda-based environment (`environment.yml`)

---

###  Execution Flow

1. User submits a research query via CLI or POST API.  
2. `search_tool.py` fetches relevant links using SerpAPI.  
3. `scraper.py` extracts text content from those URLs.  
4. `analyzer.py` sends the text and query to Azure GPT-4o for summarization.  
5. `agent.py` returns the structured summary.

"If using FastAPI, result is returned in JSON format with status and content."

---

##  Tech Stack

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
```
### 2. 🧪 Create Environment
Using Conda (recommended):
```bash
conda env create -f environment.yml
conda activate web-agent
```
3. 🔐 Setup Environment Variables
Create a .env file based on .env.example:
```bash
AZURE_OPENAI_API_KEY=your_azure_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
AZURE_DEPLOYMENT_NAME=gpt-4o
SERPAPI_API_KEY=your_serpapi_key
```
4. 💻 Run CLI Agent
```bash
python main.py
```
You’ll be prompted to enter a query. The agent will search, scrape, and summarize.

5. 🌐 Run FastAPI Web Server
```bash
uvicorn api:app --reload
Open http://127.0.0.1:8000/docs to test via Swagger.
```
6. ✅ Run Tests
```bash
pytest tests/
```
### 📁 File Structure

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

### Demo Video
https://drive.google.com/file/d/1ta_koSpsOATKX_YKJvP6-UwY19K8Bnbk/view?usp=sharing

### Author

  `Himanshu Dhingra🚀`<br>
  `AI Developer Intern at R Systems`<br>
  `himanshudhingra2910@gmail.com`<br>
  `GitHub`<br>
