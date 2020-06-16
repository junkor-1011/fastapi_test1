"""
APIRouter static test.
"""

from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles


def create_router():
    """create router"""
    _router = APIRouter()

    _router.mount("/dir",
                  StaticFiles(directory="app/test_static/dir", html=True),
                  name="static_test",)
    return _router


router = create_router()


# @router.get("/test_static/get")
@router.get("/get")
async def hello():
    """hello(tmp)"""
    return {"message": "hello from APIRouter"}
