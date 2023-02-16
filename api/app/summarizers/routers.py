from fastapi import APIRouter
from .imodels import SummarizerInterface
from ..models.pkl_manager import get_model_obj

# FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
import warnings
warnings.filterwarnings("ignore")

router = APIRouter(prefix="/summarizer")


@router.get("/")
async def root():
    return {"message": "API for text summarizer."}


@router.post("/summarize/")
async def get_summary_view(summarizer_data: SummarizerInterface):
    body = summarizer_data.text
    summarizer = get_model_obj("bert_summarizer")
    summary = summarizer(body, ratio=summarizer_data.ratio)
    return {
        "data": {
            "body": body,
            "ratio": summarizer_data.ratio,
            "summary": summary,
            "lengths": {
                "text": len(body),
                "summary": len(summary),
            }
    }}
