from ..schemas import ChatRecords, FrameRequest
from ..data_handler import MemoryDataHandler, EventDataHandler, CharacterDataHandler
from ..callback_handler.callback import Callback
from typing import Union


class BaseEngine:
    def __init__(self) -> None:
        self.memory_handler = MemoryDataHandler()
        self.event_handler = EventDataHandler()
        self.charecter_handler = CharacterDataHandler()

    def _triger():
        pass


class BaseShuntEngine(BaseEngine):
    def _call(self, bot_id: str, chat_records: ChatRecords):
        raise NotImplementedError('The _call function must be implemented')

    def run(self, bot_id: str, chat_records: ChatRecords):
        result = self._call(bot_id, chat_records)
        return result


class BaseDecisionEngine(BaseEngine):
    def _call_chat(
        self,
        bot_id: str,
        callback: Callback,
        chat_records: Union[ChatRecords, None] = None,
    ):
        raise NotImplementedError('The _call function must be implemented')

    def _call_task(self, bot_id: str, callback: Callback):
        raise NotImplementedError('The _call function must be implemented')

    def _call_init_character(self, bot_id: str, callback: Callback):
        raise NotImplementedError('The _call function must be implemented')

    def run_chat(self, bot_id: str, chat_records: ChatRecords):
        callback = Callback(
            endpoint=chat_records.callback,
            bot_id=chat_records.bot_id,
            session_id=chat_records.session_id,
        )
        result = self._call_chat(bot_id=bot_id, chat_records=chat_records, callback=callback)
        return result

    def run_task(self, bot_id: str, callback_url: str):
        callback = Callback(endpoint=callback_url, bot_id=bot_id, session_id=bot_id)
        result = self._call_task(bot_id=bot_id, callback=callback)
        return result

    def run_init_character(self, bot_id: str, callback_url: str):
        callback = Callback(endpoint=callback_url, bot_id=bot_id, session_id=bot_id)
        result = self._call_init_character(bot_id, callback=callback)
        return result


class BaseQAEngine(BaseEngine):
    def _call(self, bot_id: str, chat_records: ChatRecords, callback: Callback):
        raise NotImplementedError('The _call function must be implemented')

    def run(self, bot_id: str, chat_records: ChatRecords):
        callback = Callback(
            endpoint=chat_records.callback,
            bot_id=chat_records.bot_id,
            session_id=chat_records.session_id,
        )
        result = self._call(
            bot_id=chat_records.bot_id, chat_records=chat_records, callback=callback
        )
        return result


class BaseMemoryEngine(BaseEngine):
    def _call(self, bot_id: str, images: FrameRequest):
        raise NotImplementedError('The _call function must be implemented')

    def run(self, bot_id: str, images: FrameRequest):
        result = self._call(bot_id, images)
        return result
