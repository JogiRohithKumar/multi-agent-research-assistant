from typing import Dict

research_sessions: Dict[str, dict] = {}


def save_session(
    thread_id: str,
    data: dict
):
    research_sessions[thread_id] = data


def get_session(
    thread_id: str
):
    return research_sessions.get(thread_id)


def delete_session(
    thread_id: str
):
    research_sessions.pop(
        thread_id,
        None
    )