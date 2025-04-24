from app.agent import web_research_agent

from app.agent import web_research_agent

def test_llama_3():
    result = web_research_agent("Current status of LLaMA 3 by Meta")
    assert any(word in result.lower() for word in ["llama", "meta", "model"])

def test_digital_id():
    result = web_research_agent("Top 3 countries using digital ID systems in 2024")
    assert "india" in result.lower() or "estonia" in result.lower()

def test_creativity():
    result = web_research_agent("Will AI replace human creativity?")
    assert "creativity" in result.lower() and "ai" in result.lower()

def test_quantum():
    result = web_research_agent("Latest breakthroughs in quantum computing 2024")
    assert "quantum" in result.lower() and ("ibm" in result.lower() or "google" in result.lower())
