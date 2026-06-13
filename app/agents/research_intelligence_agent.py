import json
import re
import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_json(text):

    text = text.strip()

    try:
        return json.loads(text)
    except Exception:
        pass

    # extract first valid JSON block safely
    matches = re.findall(r"\{[\s\S]*?\}", text)

    for m in matches:
        try:
            return json.loads(m)
        except:
            continue

    raise ValueError(f"Invalid JSON Response:\n{text}")


def generate_research_intelligence(query, summaries, citations):

    # limit input size (VERY IMPORTANT)
    summaries = summaries[:5]


    summaries_text = ""

    for s in summaries:
        findings = "\n".join(s.get("key_findings", [])[:3])

        summaries_text += f"""
Title: {s.get("title","")}
Summary: {s.get("summary","")}
Key Findings: {findings}
-----------------------------------
"""



    prompt = f"""
You are a senior research analyst.

Return ONLY valid JSON. No explanation. No markdown.

Keep output SMALL and STRICT.

Rules:
- max 5 items per list
- evidence_strength must be short (max 1 line)
- confidence_score between 0 and 1
- DO NOT generate long paragraphs

Return format:

{{
  "verification": {{
    "common_findings": [],
    "conflicting_findings": [],
    "evidence_strength": "",
    "confidence_score": 0.0
  }},
  "gaps": {{
    "research_gaps": [],
    "missing_areas": [],
    "future_directions": [],
    "unanswered_questions": []
  }},
  citations_text = "\n".join(
    c.get("apa", "") for c in citations[:5]
)
}}

Query:
{query}

Papers:
{summaries_text}

"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2,
            "max_output_tokens": 8192
        }
    )

    print("\n===== RAW GEMINI RESPONSE =====\n")
    print(response.text)
    print("\n==============================\n")

    return extract_json(response.text)