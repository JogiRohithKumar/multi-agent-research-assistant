from app.memory.session_memory import research_sessions


def save_session(
    thread_id,
    state
):
    research_sessions[thread_id] = state


def load_session(
    thread_id
):
    return research_sessions.get(
        thread_id
    )