#!/usr/bin/env python
"""
This would be the point of entry of running application.
This script would act as a wrapper and load necessary env files and other configs.
"""
import os
import uvicorn
from dotenv import load_dotenv, dotenv_values
from pathlib import Path

# Change work directory
os.chdir(Path(__file__).parent)
# Load .env variables
load_dotenv('.env')


if __name__ == "__main__":
    # Run uvicorn server
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, workers=2) # reload=True
