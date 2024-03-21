from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse, JSONResponse
from router.users import router as user_routes

metadata = [
    {
        "name": "web",
        "description": "Web endpoints"
    },
    {
        "name": "users",
        "description": "User handle endpoints"
    }
]

app = FastAPI(openapi_tags=metadata, openapi_prefix="/api/v1")

@app.get('/',
            tags=["web"],
            description="Shows an HTML welcome")
def greet():
    with open("public/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)


app.include_router(user_routes, tags=["users"])