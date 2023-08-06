import json
import logging
import time
import traceback


import redis
from fastapi import APIRouter
from https.schemas.payload import ChatBody
from https.schemas.response import Response
from rq import Connection, Queue, cancel_job
from rq.job import Job
from starlette.requests import Request
from qa_engine import QAEngine
from ombot_utils.schemas import ChatRecords
from config.config import EnvVars

router = APIRouter()
logging.basicConfig(
    format="============ %(asctime)s [%(pathname)s:%(lineno)d] ============ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)


@router.post("/chat", response_model=Response, name="Start evaluate")
async def run(request: Request, body: ChatBody = None) -> Response:
    logging.info("收到请求{}".format(body.json(ensure_ascii=False)))
    s_time = time.time()
    try:
        engine = request.app.state.engine
        resp = engine.process(
            bot_id=body.bot_id, data=body.data, events=body.kwargs.events
        )
        logging.info("处理成功，结果为{}".format(resp))
        res = Response(
            took=int((time.time() - s_time) * 1000),
            msg="success",
            code=200,
            result=resp,
        )

    except Exception as e:
        logging.error(traceback.format_exc())
        res = Response(
            took=int((time.time() - s_time) * 1000), msg="failed", code=500, result={}
        )
    return res
