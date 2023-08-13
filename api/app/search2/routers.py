from fastapi import APIRouter
from .interfaces import SearchInterface
from .search import Search


router = APIRouter()

@router.get("/")
async def root():
    return True

@router.post("/")
async def search(search: SearchInterface):
    _search = Search()
    _results = await _search(search)
    return _results
