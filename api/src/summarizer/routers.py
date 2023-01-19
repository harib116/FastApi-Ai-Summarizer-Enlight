from fastapi import APIRouter
from .functions import get_summary
from .imodels import SummarizerModel


router = APIRouter(prefix="/summarizer")


@router.get("/")
async def root():
    return {"message": "API for text summarizer."}


@router.post("/summarize")
async def get_summary_view(summarizer: SummarizerModel):
    text = summarizer.text
    return {
        "data": {
            "summary": await get_summary(text)
    }}
