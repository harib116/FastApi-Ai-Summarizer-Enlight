from pydantic import BaseModel


class SummarizerModel(BaseModel):
    text: str

