from pydantic import BaseModel


class Paper(BaseModel):
    title: str
    authors: list[str]
    abstract: str
    published: str
    paper_url: str