from app.rag.vector_store import (
    collection
)


def retrieve_context(
    query,
    k=5
):

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    return results