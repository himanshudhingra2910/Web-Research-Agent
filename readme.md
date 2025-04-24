Masonry Web Research Agent

A fully autonomous AI research assistant that searches the web, extracts content, and synthesizes intelligent answers using Azure GPT-4o.

How It Works

Query Analysis: Understands the user's question

Search: Uses SerpAPI to find relevant web pages

Scraping: Extracts content using BeautifulSoup

Synthesis: Summarizes using Azure OpenAI's GPT-4o

Technologies Used

Component

Tool

AI Model

Azure OpenAI (GPT-4o)

Search

SerpAPI

Scraping

BeautifulSoup

Config

dotenv

Language

Python 3.10

Project Structure

web-research-agent/
├── app/
│   ├── agent.py         # Orchestrates the whole pipeline
│   ├── search_tool.py   # Uses SerpAPI to find results
│   ├── scraper.py       # Scrapes HTML text
│   ├── analyzer.py      # Calls GPT-4o
│   └── utils.py         # Future helper functions
├── config/settings.py   # Loads .env values
├── main.py              # Entry point
├── tests/test_agent.py  # Example test
├── .env.example         # Template for env vars
├── examples.md          # Sample queries and answers
└── README.md

Setup Instructions

Clone the repo:

git clone https://github.com/yourusername/web-research-agent
cd web-research-agent

Create .env file:

AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_DEPLOYMENT_NAME=gpt-4o-bro
SERPAPI_API_KEY=your-serpapi-key

Note: You need to create a .env file based on .env.example with your own API keys.

Install dependencies:

pip install -r requirements.txt

Run it:

python main.py

Agent Behavior: Decision Flow

Receives query

Generates Google search using SerpAPI

Picks top 5 links

Extracts readable content from them

Combines the content into a single prompt

Sends the prompt to GPT-4o for analysis

Returns summarized research response

Error Handling

Handles unreachable links with fallback messages

Skips empty or invalid pages

Uses try-except blocks to ensure graceful failures

Testing

# tests/test_agent.py
from app.agent import web_research_agent

def test_basic():
    result = web_research_agent("Benefits of mindfulness")
    assert "mindfulness" in result.lower()

Run tests with:

pytest tests/

💡 Prompt Engineering

We use a consistent prompt template:

"You are a helpful research assistant. Based on the following sources, summarize the answer to: [query]"

This ensures factual, clear, helpful responses.

Sample Queries (see examples.md)





Author

Himanshu Dhingra AI Developer Intern @ R Systems himanshudhingra2910@gmail.com

