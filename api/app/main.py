from fastapi import FastAPI, Request
from mangum import Mangum
from . import settings
from .summarizers.routers import router as summarizer_router


app = FastAPI(debug=settings.DEBUG)


@app.get("/")
async def root():
    return {
        "status": 200,
        "body": {
            "message": "Welcome to CurEdu APIs !"
        }
    }


@app.post("/test")
async def test(request: Request):
    data = await request.json()
    return {
        "data": {
            "message": "Welcome to CurEdu Query !",
            "data": data
        }
    }


app.include_router(summarizer_router)


handler = Mangum(app)
