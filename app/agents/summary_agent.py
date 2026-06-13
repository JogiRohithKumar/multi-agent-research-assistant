import google.generativeai as genai
import json
import re

from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_json(text):

    text = text.strip()

    try:
        return json.loads(text)

    except Exception:
        pass

    match = re.search(
    r"\{[\s\S]*\}",
    text
)

    if match:

        return json.loads(
            match.group()
        )

    raise ValueError(
        "No valid JSON found"
    )


def summarize_papers(papers):

    papers_text = ""

    for i, paper in enumerate(papers, start=1):

        papers_text += f"""
Paper {i}

Title:
{paper["title"]}

Abstract:
{paper["abstract"]}

----------------------------------------
"""

    prompt = f"""
You are an expert research paper summarizer.

Analyze EACH paper separately.

Return ONLY valid JSON.

Format:

[
    {{
        "title": "paper title",
        "summary": "2-3 sentence summary",
        "key_findings": [
            "finding 1",
            "finding 2",
            "finding 3"
        ]
    }}
]

Research Papers:

{papers_text}
"""

    response = model.generate_content(prompt)

    response_text = response.text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    try:
        summaries = extract_json(response_text)
        return summaries

    except Exception:

        return [
            {
                "title": "Parsing Error",
                "summary": response_text,
                "key_findings": []
            }
        ]