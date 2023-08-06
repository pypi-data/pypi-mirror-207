#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from copy import deepcopy
from typing import List, Union
from sqlmodel import Session, select, lateral
import datetime
from .base_sql_data_handler import BaseSQLDataHandler
from ..schemas import OmbotEvent, EventInput, EventObject
from ..log_handler import logging

try:
    logging.handlers
except:
    logging.init_logger('ombot', 'ombot')


class EventDataHandler(BaseSQLDataHandler):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def get_data(self,
                 ombot_id: int,
                 event_name: str = None,
                 number: Union[int, str] = "all",
                 get_keys: List[str] = None
                 ) -> List[OmbotEvent]:
        """
        在事件库中查询ombot_id的关注事件信息。
        :param ombot_id: ombot_id 获取ombot_id的事件信息。
        :param number: 默认为'all' 获取全部事件信息，若指定number数量，则获取最新的number条事件信息。
        :param get_keys: List[str]，获取事件的关键字，默认查询["id", "event", "source"]
        :return: 返回查询到的事件信息。如未查询到结果返回:[]
        :return:
        """
        if get_keys is None:
            get_keys = ["id", "event_name", "event", "source"]

        with Session(self.engine) as session:
            if get_keys:
                if "bot_id" not in get_keys:
                    get_keys.append("bot_id")
                if "id" not in get_keys:
                    get_keys.append("id")
                select_statement = "OmbotEvent." + ", OmbotEvent.".join([key for key in get_keys])
                if event_name:
                    statement = select(*eval(select_statement))\
                                .where(OmbotEvent.bot_id == ombot_id)\
                                .where(OmbotEvent.event_name == event_name)\
                                .where(OmbotEvent.deleted == self.NO_DELETED)
                else:
                    statement = select(*eval(select_statement))\
                                .where(OmbotEvent.bot_id == ombot_id)\
                                .where(OmbotEvent.deleted == self.NO_DELETED)
            else:
                statement = select(OmbotEvent).where(OmbotEvent.bot_id == ombot_id).where(
                    OmbotEvent.deleted == self.NO_DELETED)

            query_results = session.exec(statement).all()
            if not query_results:
                return []
            if not isinstance(query_results[0], OmbotEvent):
                results = []
                for one_result in query_results:
                    results.append(OmbotEvent(**{key: val for key, val in zip(get_keys, one_result)}))
            else:
                results = query_results
            if isinstance(number, int):
                results = sorted(results, key=lambda OmbotEvent: OmbotEvent.id)[-number:]
            logging.info("查询到ombot【{}】的【{}】条事件信息。".format(ombot_id, len(results)))
            results = self.str2obj(results)
        return results

    def add_data(self, events: List[EventInput]) -> None:
        """
        为ombot_id添加事件信息。
        :param events: 包含ombot_id和event属性的EventInput实例
        :return: None
        """

        events = self.obj2str(events)
        with Session(self.engine) as session:
            for event, event_name in events:
                dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                temp_event = OmbotEvent(bot_id=event.ombot_id,
                                        create_time=dt,
                                        event_name=event_name,
                                        event=event.event,
                                        source=event.source)
                session.add(temp_event)
                logging.info("添加ombot【{}】的【{}】信息成功。".format(event.ombot_id, event_name))
            session.commit()

    def delete_data(self, ombot_id, event_names: List[str]) -> None:
        with Session(self.engine) as session:
            for event_name in event_names:
                statement = select(OmbotEvent).where(OmbotEvent.bot_id == ombot_id).where(
                    OmbotEvent.event_name == event_name).where(OmbotEvent.deleted == self.NO_DELETED)
                query_results = session.exec(statement).first()
                if query_results:
                    query_results.deleted = self.DELETED
                    logging.info("事件库中ombot【{}】的【{}】信息已成功删除。".format(ombot_id, event_name))
                else:
                    logging.warning("事件库中没有ombot【{}】的【{}】信息，无法删除。".format(ombot_id, event_name))
            session.commit()

    def str2obj(self, datas):
        results = []
        for data in datas:
            temp_result = deepcopy(data)
            event_result = json.loads(data.event)
            event_obj = EventObject(**dict(event_result))
            temp_result.event = event_obj

            results.append(temp_result)
        return results

    def obj2str(self, datas):
        results = []
        for data in datas:
            temp_result = deepcopy(data)
            temp_event_name = data.event.event_name
            result = json.dumps(dict(data.event), ensure_ascii=False)
            temp_result.event = result

            results.append((temp_result, temp_event_name))
        return results
