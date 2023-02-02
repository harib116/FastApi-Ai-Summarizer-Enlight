from fastapi import APIRouter
from .imodels import SummarizerModel
from ..models.pkl_manager import get_model_obj

router = APIRouter(prefix="/summarizer")


@router.get("/")
async def root():
    return {"message": "API for text summarizer."}


@router.post("/summarize")
async def get_summary_view(summarizer: SummarizerModel):
    text = summarizer.text
    summarizer = get_model_obj("bert_summarizer")
    summary = summarizer(text)
    return {
        "data": {
            "text": text,
            "summary": summary,
            "lengths": {
                "text": len(text),
                "summary": len(summary),
            }
    }}
