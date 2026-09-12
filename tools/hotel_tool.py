# Import libraries
from tavily import TavilyClient 
from dotenv import load_dotenv 
import certifi 
import os 

# Load dotenv
load_dotenv()

# If there is path issue with SSL
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# Get API key for tavily 
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Create tavily client 
tavily_client = TavilyClient(
    api_key=TAVILY_API_KEY
)

# Create a hotel search tool function 
def search_hotels(query):
    """ Search top 5 hotels on the internet according to the user query"""
    response = tavily_client.search(
        query=query,
        max_results=5
    )
    
    result = []

    for i, r in enumerate(response["results"],1): 
        title = r.get("title","Unknown")
        url = r.get("url","")
        snippet = r.get("content","")

        if len(snippet)>300: 
            snippet = snippet[:300].rsplit(" ",1)[0] + "..."

        result.append(f"{i}. **{title}\n {url}\n {snippet}")

    return "\n\n".join(result)

