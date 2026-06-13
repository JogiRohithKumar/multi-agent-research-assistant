import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(
api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
"gemini-2.5-flash"
)

def rewrite_query(query: str):

    prompt = f"""

    Convert the research topic into a concise academic search query.
    If paper is NOT in dataset, explicitly say:
    "Not found in retrieved papers"
    Do NOT use external knowledge
    Rules:

    Add important synonyms
    Add related keywords
    Keep under 15 words
    Return only the search query

    Topic:
    {query}
    """

    response = model.generate_content(
        prompt
    )

    return response.text.strip()