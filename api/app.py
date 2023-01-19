from fastapi import FastAPI, Request
from mangum import Mangum
from api.src.summarizer.routers import router as summarizer_router


app = FastAPI()


@app.get("/")
async def root():
    return {
       "message": "Welcome to CurEdu API !"
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