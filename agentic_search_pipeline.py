import os
import json
import argparse
import pandas as pd
from datetime import datetime

# You can install required packages via:
# pip install openai requests
from openai import OpenAI
import requests

# Set your API keys as environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your-openai-api-key")
# Using Tavily for Agentic Web Search, or could use Serper/Google Custom Search
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "your-tavily-api-key")

client = OpenAI(api_key=OPENAI_API_KEY)

def web_search(query):
    """
    Search the web for information using Tavily API.
    """
    try:
        url = "https://api.tavily.com/search"
        payload = {
            "api_key": TAVILY_API_KEY,
            "query": query,
            "search_depth": "advanced",
            "include_answer": True,
            "max_results": 4
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        results = response.json()
        
        # Combine snippets from the search
        snippets = []
        if "answer" in results and results["answer"]:
            snippets.append(results["answer"])
        for res in results.get("results", []):
            snippets.append(f"[{res['url']}]: {res['content']}")
        return "\n\n".join(snippets)
    except Exception as e:
        print(f"Search failed: {e}")
        return "Search failed or API key not configured."

def get_subsidiary_dates(parent_comp, sub_comp):
    """
    Agentic flow:
    1. Perform a targeted web search for the acquisition/incorporation.
    2. Feed search results to an LLM to extract TimeIn, TimeOut, and Source.
    """
    query = f"When did {sub_comp} become a subsidiary of {parent_comp}? When was it divested or sold?"
    print(f"[*] Searching web: {query}")
    
    context = web_search(query)
    
    system_prompt = '''You are a financial research assistant. Given the search context, identify the timeline of a subsidiary relationship.
There are 3 ways it could be formed: Internal (registered), External (acquired), Restructuring (expanded).
Extract:
1. TimeIn: Year or Date it became a subsidiary.
2. TimeOut: Year or Date it was divested/sold (if applicable, else "N/A").
3. Source: Main source of this information (e.g., "SEC filings via SEC.gov", "News article from Bloomberg").

If the exact date is not in the text, make your best guess or state "Unknown".
Please return valid JSON ONLY with the keys: TimeIn, TimeOut, MainSource, Notes.
'''

    user_prompt = f"Parent Company: {parent_comp}\nSubsidiary: {sub_comp}\n\nSearch Context:\n{context}"
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"LLM extraction failed: {e}")
        return {"TimeIn": "Error", "TimeOut": "Error", "MainSource": "Error", "Notes": str(e)}

def process_batch(input_csv, output_csv, limit=5):
    df = pd.read_csv(input_csv)
    
    # Optional: Take a random sample or top `limit` rows
    df_sample = df.head(limit).copy()
    
    times_in = []
    times_out = []
    sources = []
    
    for idx, row in df_sample.iterrows():
        parent = row['COMP_NAME']
        sub = row['SUB_NAME']
        print(f"\nProcessing {idx+1}/{limit}: {sub} (Parent: {parent})")
        
        res = get_subsidiary_dates(parent, sub)
        times_in.append(res.get("TimeIn", "N/A"))
        times_out.append(res.get("TimeOut", "N/A"))
        sources.append(res.get("MainSource", "N/A"))
        
    df_sample['TimeIn'] = times_in
    df_sample['TimeOut'] = times_out
    df_sample['MainSource'] = sources
    
    df_sample.to_csv(output_csv, index=False)
    print(f"\nSaved results to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=5, help="Number of rows to process")
    args = parser.parse_args()
    
    print("Starting Agentic Extraction Pipeline...")
    process_batch("subs_sample.csv", "subs_processed.csv", limit=args.batch)
