#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from collections import defaultdict
from copy import deepcopy
from typing import List, Union
from sqlmodel import Session, select
import datetime
from .base_sql_data_handler import BaseSQLDataHandler
from ..schemas import MemoryInput, OmbotMemory, DetObject
from ..log_handler import logging

try:
    logging.handlers
except:
    logging.init_logger('ombot', 'ombot')


class MemoryDataHandler(BaseSQLDataHandler):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.add_memory_count = defaultdict(int)

    def get_data(self,
                 ombot_id: int,
                 number: Union[int, str] = "all",
                 get_keys: List[str] = None) -> List[OmbotMemory]:
        """
        在记忆库中查询ombot_id的记忆信息。
        :param ombot_id: ombot_id 获取ombot_id的记忆信息。
        :param number: 默认为'all' 获取全部记忆信息，若指定number数量，则获取最新的number条记忆信息。
        :param get_keys: List[str]，获取记忆的关键字，默认查询["id", "memory", "od_result", "abnormal_description", "caption",
                        "region_caption", "image_time"]
        :return: 返回查询到的记忆信息。如未查询到结果返回:[]
        """
        if get_keys is None:
            get_keys = ["id", "memory", "od_result", "od_result_summary", "anomalous_summary","anomalous", "caption", "caption_summary",
                        "region_caption_summary", "region_caption", "image_time"]

        with Session(self.engine) as session:
            if get_keys:
                if "bot_id" not in get_keys:
                    get_keys.append("bot_id")
                if "id" not in get_keys:
                    get_keys.append("id")
                select_statement = "OmbotMemory." + ", OmbotMemory.".join([key for key in get_keys])
                statement = select(*eval(select_statement)).where(OmbotMemory.bot_id == ombot_id).where(
                    OmbotMemory.deleted == self.NO_DELETED)
            else:
                statement = select(OmbotMemory).where(OmbotMemory.bot_id == ombot_id).where(
                    OmbotMemory.deleted == self.NO_DELETED)
            query_results = session.exec(statement).all()

            if not query_results:
                return []

            if not isinstance(query_results[0], OmbotMemory):
                results = []
                for one_result in query_results:
                    results.append(OmbotMemory(**{key: val for key, val in zip(get_keys, one_result)}))
            else:
                results = query_results

            if isinstance(number, int):
                results = sorted(results, key=lambda OmbotMemory: OmbotMemory.id)[-number:]

            results = self.str2obj(results)
            logging.info("查询到ombot【{}】的【{}】条记忆。".format(ombot_id, len(results)))
        return results

    def add_data(self, memorys: List[MemoryInput]) -> None:
        memorys = memorys if isinstance(memorys, list) else [memorys]
        memorys = self.obj2str(memorys)
        with Session(self.engine) as session:
            for memory in memorys:
                dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                temp_memory = OmbotMemory(bot_id=memory.ombot_id,
                                          create_time=dt,
                                          memory=memory.memory,
                                          od_result=memory.od_result,
                                          od_result_summary=memory.od_result_summary,
                                          anomalous=memory.anomalous,
                                          anomalous_summary=memory.anomalous_summary,
                                          caption=memory.caption,
                                          caption_summary=memory.caption_summary,
                                          region_caption=memory.region_caption,
                                          region_caption_summary=memory.region_caption_summary,
                                          image_time=memory.image_time
                                          )
                session.add(temp_memory)
                self.add_memory_count[memory.ombot_id] += 1
                logging.info("添加ombot【{}】的【{}】memory信息成功。".format(memory.ombot_id, memory.memory))
            session.commit()


    def delete_data(self, ombot_id, memory_ids) -> None:

        with Session(self.engine) as session:
            for memory_id in memory_ids:
                statement = select(OmbotMemory).where(OmbotMemory.bot_id == ombot_id).where(
                    OmbotMemory.id == memory_id).where(OmbotMemory.deleted == self.NO_DELETED)
                query_results = session.exec(statement).first()
                if query_results:
                    query_results.deleted = self.DELETED
                    logging.info("记忆库中ombot【{}】的{}信息已成功删除。".format(ombot_id, memory_id))
                else:
                    logging.warning("记忆库中没有ombot【{}】的【{}】信息，无法删除。".format(ombot_id, memory_id))
            session.commit()

    def str2obj(self, datas):
        results = []
        for data in datas:
            temp_result = deepcopy(data)
            if data.od_result:
                od_results = json.loads(data.od_result)
                od_obj = [DetObject(**dict(json.loads(od_result))) for od_result in od_results]
                temp_result.od_result = od_obj
            if data.region_caption:
                region_caption_results = json.loads(data.region_caption)
                region_obj = [DetObject(**dict(json.loads(region_caption_result))) for region_caption_result in
                              region_caption_results]
                temp_result.region_caption = region_obj
            if data.caption:
                caption_results = json.loads(data.caption)
                caption_res = [caption_result for caption_result in caption_results]
                temp_result.caption = caption_res
            if data.anomalous:
                anomalous_results = json.loads(data.anomalous)
                anomalous_res = [anomalous_result for anomalous_result in anomalous_results]
                temp_result.anomalous = anomalous_res
            results.append(temp_result)
        return results

    def obj2str(self, datas):
        results = []
        for data in datas:
            temp_result = deepcopy(data)
            if data.od_result:
                od_result = json.dumps(
                    [json.dumps(dict(od_result), ensure_ascii=False) for od_result in data.od_result],
                    ensure_ascii=False)
                temp_result.od_result = od_result
            if data.region_caption:
                region_caption = json.dumps(
                    [json.dumps(dict(region_caption), ensure_ascii=False) for region_caption in data.region_caption],
                    ensure_ascii=False)
                temp_result.region_caption = region_caption
            if data.caption:
                caption_results = json.dumps(data.caption)
                temp_result.caption = caption_results
            if data.anomalous:
                anomalous_results = json.dumps(data.anomalous)
                temp_result.anomalous = anomalous_results
            results.append(temp_result)
        return results


if __name__ == '__main__':
    rdh = MemoryDataHandler(1)
    input = [MemoryInput(ombot_id=id, event=char) for id, char in
             [(1, "memory", "od_result"), (2, "good"), (2, "bad"), (2, "bad1"), (2, "bad2"), (2, "bad3")]]
    rdh.add_data(input)
    # rdh.delete_data(input)
    print(rdh.get_data(2, number=2))
