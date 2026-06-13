stream_events = []


def stream_log(message: str):

    print(f"[STREAM] {message}")

    stream_events.append(message)

    print("EVENTS:", stream_events)


def get_stream_events():

    return stream_events


def clear_stream_events():

    stream_events.clear()