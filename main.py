from app.agent import web_research_agent

def save_to_examples(query, result):
    with open("examples.md", "a") as f:
        f.write(f"\n\nQuery: \"{query}\"\n\n")
        f.write(f"Research Summary:\n{result.strip()}\n\n")

if __name__ == "__main__":
    query = input("Enter your research query: ")
    result = web_research_agent(query)

    print("\n--- Research Summary ---\n")
    print(result)

    save_to_examples(query, result)
    
