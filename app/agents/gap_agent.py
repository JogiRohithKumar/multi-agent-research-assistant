import json
import re

import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_json(text):

    text = text.strip()

    if text.startswith("```json"):
        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

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


def analyze_gaps(summaries):

    summaries = summaries[:10]

    summaries_text = ""

    for summary in summaries:

        findings = "\n".join(
            summary.get(
                "key_findings",
                []
            )
        )

        summaries_text += f"""
Title:
{summary.get("title", "")}

Summary:
{summary.get("summary", "")}

Key Findings:
{findings}

----------------------------------------
"""

    prompt = f"""
You are a senior research gap analysis expert.

Analyze all papers.

Return ONLY valid JSON.

{{
    "research_gaps": [],
    "missing_areas": [],
    "future_directions": [],
    "unanswered_questions": []
}}

Research Papers:

{summaries_text}
"""

    try:

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 2048
            }
        )

        return extract_json(
            response.text
        )

    except Exception as e:

        return {
            "research_gaps": [],
            "missing_areas": [],
            "future_directions": [],
            "unanswered_questions": [],
            "error": str(e)
        }