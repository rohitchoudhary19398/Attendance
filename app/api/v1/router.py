from fastapi import APIRouter

from app.api.v1.endpoints import att_records, auth

api_router = APIRouter()
api_router.include_router(att_records.router, prefix="/records", tags=["records"])
api_router.include_router(auth.router, prefix="/auth", tags=["user"])
