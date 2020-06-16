"""
app main
"""

from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import test_api
from .test_static import router as router_static   # TMP


def create_app():
    """create app"""
    _app = FastAPI()

    _app.include_router(
        test_api.router,
        prefix="/test_api",
        tags=["test_api"],
        responses={404: {"description": "not found"}},
    )
    _app.include_router(
        router_static,
        # prefix="/test_static",
        tags=["test_static"],
    )

    return _app


app = create_app()


@app.get('/')
async def site_root():
    """hello-world(TMP)"""
    return {"message": "Hello, WORLD!"}
