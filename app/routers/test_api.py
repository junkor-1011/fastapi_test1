"""
test api
"""

import shutil
# import pathlib
from pathlib import Path
from typing import (
    Optional,
    List,
)

# from fastapi import APIRouter, HTTPException, Query, Path
from fastapi import (
    APIRouter,
    Query,
    Path,
    File,
    UploadFile,
)


# router = APIRouter()
def create_router():
    """create router"""
    _router = APIRouter()
    return _router


router = create_router()


@router.get("/")
async def get_test1(
    string: str = Query(None, min_length=2, max_length=5, regex=r'[a-c]+.'),
    integer: int = Query(..., gt=1, le=3),
    alias_query: str = Query('default', alias='alias-query'),
):
    return {
        "string": string,
        "integer": integer,
        "alias-query": alias_query,
    }


@router.get("/validation/{path}")
async def validation(
    string: str = Query(None, min_length=2, max_length=5, regex=r'[a-c]+.'),
    integer: int = Query(..., gt=1, le=3),
    alias_query: str = Query('default', alias='alias-query'),
    path: int = Path(10),
):
    return {
        "string": string,
        "integer": integer,
        "alias-query": alias_query,
        "path": path,
    }


# @router.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        # "file_size": len(file),   # NG
    }


@router.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


# @router.post("/savefiles")
# async def save_file(
#     upload_file: UploadFile = File(...),
#     destination: Path = "",
# ):
#     with destination.open("wb") as buffer:
#         shutil.copyfileobj(upload_file.file, buffer)
#     return {
#         "filenames": upload_file.filename,
#         "destination": str(destination),
#     }
