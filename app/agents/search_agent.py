
import requests
import xml.etree.ElementTree as ET

from app.agents.query_rewriter import rewrite_query


def is_relevant(paper, query):

    text = (paper["title"] + " " + paper["abstract"]).lower()

    important = [
        "llm", "gpt", "transformer",
        "education", "learning",
        "language model"
    ]

    score = sum(1 for k in important if k in text)

    return score >= 2


def search_papers(query):
    optimized_query = rewrite_query(query)

    print(
        "\nOptimized Query:",
        optimized_query
    )

    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query=ti:{optimized_query}+OR+abs:{optimized_query}"
        "&start=0"
        "&max_results=15"
    )

    response = requests.get(
        url,
        timeout=30
    )

    root = ET.fromstring(
        response.content
    )

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    papers = []

    for entry in root.findall(
        "atom:entry",
        namespace
    ):
        authors = []

        for author in entry.findall(
            "atom:author",
            namespace
        ):
            authors.append(
                author.find(
                    "atom:name",
                    namespace
                ).text
            )

        papers.append(
            {
                "title": entry.find(
                    "atom:title",
                    namespace
                ).text.strip(),

                "authors": authors,

                "abstract": entry.find(
                    "atom:summary",
                    namespace
                ).text.strip(),

                "published": entry.find(
                    "atom:published",
                    namespace
                ).text,

                "paper_url": entry.find(
                    "atom:id",
                    namespace
                ).text
            }
        )

    filtered_papers = [
        paper
        for paper in papers
        if is_relevant(
            paper,
            optimized_query
        )
    ]

    print(
        f"Found {len(filtered_papers)} relevant papers"
    )

    return filtered_papers[:5]

