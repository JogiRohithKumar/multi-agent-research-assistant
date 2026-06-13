from fastapi import APIRouter

from app.utils.stream_logger import (
    get_stream_events
)

router = APIRouter()


@router.get("/stream")
def stream_events():

    events = get_stream_events()

    print("STREAM API CALLED")
    print(events)

    return {
        "events": events
    }