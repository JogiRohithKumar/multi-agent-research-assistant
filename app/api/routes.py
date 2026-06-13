from fastapi import APIRouter
from fastapi import Depends

from app.graph.research_graph import (
    research_graph
)

from app.api.schemas import (
    ResearchRequest
)

from app.auth.auth import (
    verify_api_key
)

router = APIRouter()


@router.post("/research")
def run_research(
    request: ResearchRequest,
    auth=Depends(verify_api_key)
):

    config = {
        "configurable": {
            "thread_id": request.query
        }
    }

    result = research_graph.invoke(
        {
            "query": request.query,
            "thread_id": request.query
        },
        config=config
    )

    return result