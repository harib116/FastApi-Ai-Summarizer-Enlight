from pydantic import BaseModel, validator


class SearchInput(BaseModel):
    query:str
    sources:str = "wikipedia"
    
    @validator('query')
    @classmethod
    def check_query_null(cls, value):
        if value == '':
            raise ValueError("Query can't be null")
        return value
    
    @validator('sources')
    @classmethod
    def check_source_type(cls, value):
        value = str.lower(value)
        if value not in ("wikipedia", "twitter"):
            raise ValueError("Currently supported source types are wikipedia and twitter(soon).")
        return value
