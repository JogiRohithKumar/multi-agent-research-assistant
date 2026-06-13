def generate_apa_citation(paper):

    authors = ", ".join(
        paper["authors"]
    )

    year = paper["published"][:4]

    return (
        f"{authors} ({year}). "
        f"{paper['title']}. "
        f"Retrieved from {paper['paper_url']}"
    )


def generate_ieee_citation(paper):

    authors = ", ".join(
        paper["authors"]
    )

    year = paper["published"][:4]

    return (
        f"{authors}, "
        f'"{paper["title"]}," '
        f"arXiv, {year}. "
        f"[Online]. Available: {paper['paper_url']}"
    )


def generate_mla_citation(paper):

    authors = ", ".join(
        paper["authors"]
    )

    year = paper["published"][:4]

    return (
        f'{authors}. "{paper["title"]}." '
        f"arXiv, {year}, "
        f"{paper['paper_url']}."
    )


def generate_bibtex_citation(paper):

    first_author = (
        paper["authors"][0]
        .split()[-1]
        .lower()
    )

    year = paper["published"][:4]

    key = f"{first_author}{year}"

    return f"""
@article{{{key},
  title={{ {paper["title"]} }},
  author={{ {" and ".join(paper["authors"])} }},
  year={{ {year} }},
  url={{ {paper["paper_url"]} }}
}}
""".strip()


def generate_citations(papers):

    citations = []

    for paper in papers:

        citations.append({
            "title": paper["title"],
            "apa": generate_apa_citation(paper),
            "ieee": generate_ieee_citation(paper),
            "mla": generate_mla_citation(paper),
            "bibtex": generate_bibtex_citation(paper)
        })

    return citations