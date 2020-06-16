from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import test_api

def create_app():
    """create app"""
    app = FastAPI()

    app.include_router(
        test_api.router,
        prefix="/test_api",
        tags=["test_api"],
        responses={404: {"description": "not found"}},
    )

    return app

app = create_app()

@app.get('/')
async def site_root():
    return {"message": "Hello, WORLD!"}

