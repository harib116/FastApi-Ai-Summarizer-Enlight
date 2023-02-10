from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from mangum import Mangum
from . import settings
from .summarizers.routers import router as summarizer_router
from .search.routers import router as search_router


app = FastAPI(debug=settings.DEBUG)

# @app.get("/")
# async def root():
#     return {
#         "status": 200,
#         "body": {
#             "message": "Welcome to CurEdu APIs !"
#         }
#     }


@app.post("/test/")
async def test(request: Request):
    data = await request.json()
    print(data)
    return {
        "data": {
            "message": "Welcome to CurEdu API! The data you just entered are",
            "inputs": data
        }
    }


app.include_router(summarizer_router, tags=["summarizer"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.mount("/", StaticFiles(directory="web", html=True), name="web")


handler = Mangum(app)


# TODO
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", port=8000, access_log="info")
