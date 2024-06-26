from fastapi import APIRouter

from .health import health_router

monitoring_router = APIRouter()
monitoring_router.include_router(health_router, tags=["系统健康度检查"])

__all__ = ["monitoring_router"]
