from pydantic import BaseModel, Field, validator
from app.sources.models import SourceType

class SearchInterface(BaseModel):
    search: str = Field(...)
    source: SourceType = Field(...)
    
    @validator('search')
    @classmethod
    def check_null_string(cls, value):
        if bool(value):
           return value
        else:
            raise ValueError("Search string must not be null")
