import google.generativeai as genai
from app.config import GEMINI_API_KEY
from app.utils.json_parser import extract_json
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_supervisor_decision(query: str):

    prompt = f"""
You are a supervisor agent controlling a research pipeline.

Return ONLY valid JSON.

Decide if the query is valid for academic research.

Rules:
- If query is vague or non-research → invalid
- If query may fail search → retry with improved query
- If good → continue

Return format:

{{
  "status": "valid | invalid | retry",
  "reason": "",
  "modified_query": "",
  "route": "continue | stop | retry_search"
}}

Query:
{query}
"""

    response = model.generate_content(prompt)

    print("\n===== SUPERVISOR RAW RESPONSE =====\n")
    print(response.text)
    print("\n==================================\n")

    return extract_json(response.text)