from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# These are environment variable *NAMES*, not the actual keys
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")