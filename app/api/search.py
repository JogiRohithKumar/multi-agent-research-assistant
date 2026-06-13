from fastapi import APIRouter # type: ignore
from app.agents.search_agent import search_papers

router = APIRouter()

@router.get("/search")
def search(query: str):

    papers = search_papers(query)

    return {
        "query": query,
        "papers": papers
    }