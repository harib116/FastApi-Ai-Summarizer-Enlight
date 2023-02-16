from pydantic import BaseModel, Field


class SummarizerInterface(BaseModel):
    text: str = Field(...)
    ratio: float = Field(default=0.2)

