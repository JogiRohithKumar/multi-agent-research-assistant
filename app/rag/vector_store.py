import uuid
import chromadb

from app.rag.chunker import chunk_text

client = chromadb.PersistentClient(
    path="app/db/chroma"
)

collection = client.get_or_create_collection(
    name="research_papers"
)


def store_papers(papers):

    for paper in papers:

        text = paper.get(
            "abstract",
            ""
        )

        if not text:
            continue

        chunks = chunk_text(text)

        for chunk in chunks:

            collection.add(
                ids=[
                    str(uuid.uuid4())
                ],
                documents=[
                    chunk
                ],
                metadatas=[
                    {
                        "title": paper.get(
                            "title",
                            ""
                        )
                    }
                ]
            )