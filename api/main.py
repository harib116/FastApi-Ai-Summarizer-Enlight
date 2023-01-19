from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
def root():
    return {
        "status": 200,
        "body": {
            "message": "Welcome to CurEdu API !"
        }
    }


@app.post("/query")
def root():
    return {
        "status": 200,
        "body": {
            "message": "Welcome to CurEdu API !"
        }
    }


handler = Mangum(app)