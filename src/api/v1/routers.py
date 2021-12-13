from fastapi import APIRouter
from .endpoints import hello

router = APIRouter()
router.include_router(hello.router, tags=["Hello"])
