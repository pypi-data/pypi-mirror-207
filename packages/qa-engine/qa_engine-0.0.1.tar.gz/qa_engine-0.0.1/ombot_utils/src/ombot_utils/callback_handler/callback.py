import requests
from ..schemas import ChatRecords, Reply, Message, OPT
from uuid import uuid4
from time import time
from ..log_handler import logging
from ..error_handler.error import VQLError
import os
from distutils.util import strtobool


class Callback:
    def __init__(self, endpoint, bot_id, session_id) -> None:
        '''
        Setup the args. This function must be called before callback.
        :param query: The received query.
        '''
        self.endpoint = endpoint
        self.bot_id =bot_id
        self.session_id = session_id
        self.dialog_id = str(uuid4())
        self.start_time = time()

    def call(self, message: Message, status:str):
        '''
        :param message: The message needed callback.
        :param status: The reply status. Choose from 'incomplete', 'end_block', 'end_answer'.
        '''
        body = Reply(
            code=200,
            error_info="",
            took=int((time() - self.start_time) * 1000),
            bot_id=self.bot_id,
            session_id=self.session_id,
            dialog_id=self.dialog_id,
            status=status,
            message=message,
        )
        logging.debug(body.json(ensure_ascii=False, indent=2))

        self.start_time = time()
        if status != 'incomplete':
            self.dialog_id = str(uuid4())

        self.do_request(body)

    def error(self, error_info:str=''):
        message = Message(
            role=OPT.ROLE.ASSISTANT,
            message_type=OPT.MESSAGE_TYPE.TEXT,
            src_type=OPT.SRC_TYPE.TEXT,
        )
        body = Reply(
            code=500,
            error_info=error_info,
            took=int((time() - self.start_time) * 1000),
            bot_id=self.bot_id,
            session_id=self.session_id,
            dialog_id=self.dialog_id,
            status=OPT.CHAT_STATUS.END_ANSWER,
            message=message,
        )
        logging.debug(body.json(ensure_ascii=False, indent=2))

        self.do_request(body)
        
    def do_request(self, body):
        if not strtobool(os.environ.get('IS_DEBUG', 'false')):
            res = requests.post(url=self.endpoint, json=body.dict())
            if res.status_code > 299:
                detail = "callback error [{}]".format(res.json())
                logging.error(detail)
                raise VQLError(570, detail=detail)