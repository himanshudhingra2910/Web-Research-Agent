from app.search_tool import perform_search
from app.scraper import extract_content
from app.analyzer import analyze_content

def web_research_agent(user_query):
    print(f"Processing query: {user_query}")
    links = perform_search(user_query)

    contents = []
    for link in links:
        text = extract_content(link)
        contents.append(text)

    combined_text = "\n\n".join(contents[:3])
    prompt = f"Based on the following data, summarize the answer to the question: '{user_query}'\n\n{combined_text}"

    return analyze_content(prompt)
