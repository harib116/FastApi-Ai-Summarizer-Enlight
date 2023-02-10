from fastapi import APIRouter, Request
from app.search.search import Search
from app.search.validators import SearchInput


router = APIRouter()

@router.get("/")
async def search():
    return {"message": "Welcome to search API"}


@router.post("/", status_code=201)
async def search(query: SearchInput):
    search = Search()
    data = await search(query.query, sources=["wikipedia"], textract=True)
    return {"message": "Welcome to search API", "data": data}