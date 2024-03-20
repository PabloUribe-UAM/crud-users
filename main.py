from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field, validator, model_validator
from typing import Any, Optional, List


metadata = [
    {
        "name": "users",
        "description": "Users entity"
    }
]

app = FastAPI(openapi_tags=metadata)

@app.get('/hello',
            tags=["web"],
            description="Shows an HTML hello world")
def greet():
    return HTMLResponse("<h1>Hello World</h1>")