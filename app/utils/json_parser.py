# app/utils/json_parser.py

import json
import re

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