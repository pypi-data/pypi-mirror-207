from typing import Callable
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from qa_engine import QAEngine

import logging
logger = logging.getLogger(__name__)


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")

        app.state.engine = QAEngine()

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        app.state.engine = None
        app.state.monitor = None
    return shutdown


async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={'error': str(exc)},
    )

