def generate_report(query, summaries, citations, intelligence):

    verification = intelligence.get("verification", {})
    gaps = intelligence.get("gaps", {})

    report = []

    # HEADER
    report.append(f"# Research Report\n")
    report.append(f"**Query:** {query}\n")

    # EXECUTIVE SUMMARY
    report.append("## Executive Summary\n")
    report.append(
        f"This analysis is based on {len(summaries)} research papers.\n"
    )

    # COMMON FINDINGS
    report.append("## Common Findings\n")
    for item in verification.get("common_findings", []):
        report.append(f"- {item}")
    report.append("")

    # CONFLICTING FINDINGS
    report.append("## Conflicting Findings\n")
    for item in verification.get("conflicting_findings", []):
        report.append(f"- {item}")
    report.append("")

    # EVIDENCE
    report.append("## Evidence Strength\n")
    report.append(verification.get("evidence_strength", "N/A"))
    report.append("")

    report.append("## Confidence Score\n")
    report.append(str(verification.get("confidence_score", 0)))
    report.append("")

    # GAPS
    report.append("## Research Gaps\n")
    for item in gaps.get("research_gaps", []):
        report.append(f"- {item}")
    report.append("")

    # MISSING AREAS
    report.append("## Missing Areas\n")
    for item in gaps.get("missing_areas", []):
        report.append(f"- {item}")
    report.append("")

    # FUTURE DIRECTIONS
    report.append("## Future Directions\n")
    for item in gaps.get("future_directions", []):
        report.append(f"- {item}")
    report.append("")

    # UNANSWERED QUESTIONS
    report.append("## Unanswered Questions\n")
    for item in gaps.get("unanswered_questions", []):
        report.append(f"- {item}")
    report.append("")

    # REFERENCES
    report.append("## References\n")
    for i, c in enumerate(citations, 1):
        report.append(f"{i}. {c.get('apa', '')}")

    return "\n".join(report)