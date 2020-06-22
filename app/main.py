"""
app main
"""

import pathlib

# from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# from .routers import test_api
from .routers import (
    test_api,
    subpage,
)
# from .test_static import router as router_static   # TMP

# const
PATH_STATIC = str(pathlib.Path(__file__).resolve().parent / "static")


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
        subpage.router,
        prefix="/subpage",
        tags=["subpage"],
        responses={404: {"description": "not found"}},
    )
    # _app.include_router(
    #     router_static,
    #     prefix="/test_static",
    #     tags=["test_static"],
    # )

    # static
    _app.mount(
        "/static",
        StaticFiles(directory=PATH_STATIC, html=False),
        name="static",
    )

    return _app


app = create_app()


@app.get('/')
async def site_root():
    """hello-world(TMP)"""
    return {"message": "Hello, WORLD!"}
