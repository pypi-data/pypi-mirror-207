from fastapi import APIRouter

from https.routes import detector
from https.routes import heartbeat

router = APIRouter()
router.include_router(heartbeat.router, tags=["health"], prefix="/v1/health")
router.include_router(detector.router, tags=["detect"], prefix="/v1/process")


