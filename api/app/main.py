from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from os import getenv
from .summarizers.routers import router as summarizer_router
from .search.routers import router as search_router

app = FastAPI(debug=getenv("DEBUG", False))

@app.get("/live/")
async def live():
    return "Chathitilla.."

app.include_router(summarizer_router, tags=["summarizer"])
app.include_router(search_router, prefix="/search", tags=["search"])

app.mount("/", StaticFiles(directory="ui", html=True), name="ui")

handler = Mangum(app)
