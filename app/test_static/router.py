"""
APIRouter static test.
"""

from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

router = APIRouter()

router.mount("/dir",
             StaticFiles(directory="app/test_static/dir", html=True),
             name="static_test",)


@router.get("/test_static/get")
async def hello():
    """hello(tmp)"""
    return {"message": "hello from APIRouter"}
