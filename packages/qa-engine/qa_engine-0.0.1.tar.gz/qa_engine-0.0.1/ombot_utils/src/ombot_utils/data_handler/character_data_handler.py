#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Union
from sqlmodel import Session, select
import datetime
from .base_sql_data_handler import BaseSQLDataHandler
from ..schemas import CharacterInput, OmbotCharacter
from ..log_handler import logging

try:
    logging.handlers
except:
    logging.init_logger('ombot', 'ombot')


class CharacterDataHandler(BaseSQLDataHandler):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def get_data(self,
                 ombot_id: int,
                 number: Union[int, str] = "all",
                 get_keys: List[str] = None) \
            -> List[OmbotCharacter]:
        """
        在角色库中查询ombot_id的角色信息。
        :param ombot_id: ombot_id 获取ombot_id的角色信息。
        :param number: 默认为'all' 获取全部角色信息，若指定number数量，则获取最新的number条角色信息。
        :param get_keys: List[str]，获取角色的关键字，默认查询["id", "character"]
        :return: 返回查询到的角色信息。如未查询到结果返回:[]
        """

        if get_keys is None:
            get_keys = ["id", "character", "traits", "status"]

        with Session(self.engine) as session:
            if get_keys:
                if "bot_id" not in get_keys:
                    get_keys.append("bot_id")
                if "id" not in get_keys:
                    get_keys.append("id")
                select_statement = "OmbotCharacter." + ", OmbotCharacter.".join([key for key in get_keys])
                statement = select(*eval(select_statement)).where(OmbotCharacter.bot_id == ombot_id).where(
                    OmbotCharacter.deleted == self.NO_DELETED)
            else:
                statement = select(OmbotCharacter).where(OmbotCharacter.bot_id == ombot_id).where(
                    OmbotCharacter.deleted == self.NO_DELETED)

            query_results = session.exec(statement).all()
            if not query_results:
                return []
            if not isinstance(query_results[0], OmbotCharacter):
                results = []
                for one_result in query_results:
                    results.append(OmbotCharacter(**{key: val for key, val in zip(get_keys, one_result)}))
            else:
                results = query_results
            if isinstance(number, int):
                results = sorted(results, key=lambda OmbotCharacter: OmbotCharacter.id)[-number:]
            logging.info("查询到ombot【{}】的【{}】条消息。".format(ombot_id, len(results)))
        return results

    def add_data(self, characters: List[CharacterInput]) -> None:
        """
        为ombot_id添加角色信息。
        :param characters: 包含ombot_id和character属性的CharacterInput实例
        :return: None
        """
        with Session(self.engine) as session:
            characters = characters if isinstance(characters, list) else [characters]
            for character in characters:
                dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                temp_character = OmbotCharacter(bot_id=character.ombot_id,
                                                create_time=dt,
                                                character=character.character,
                                                traits=character.traits,
                                                status=character.status)
                session.add(temp_character)
                logging.info("添加ombot【{}】的【{}】信息成功。".format(character.ombot_id, character.character))
            session.commit()

    def delete_data(self, characters: List[CharacterInput]) -> None:
        """
        删除ombot_id的角色信息。
        :param characters: 包含ombot_id和character属性的CharacterInput实例
        :return: None
        """
        with Session(self.engine) as session:
            for character in characters:
                statement = select(OmbotCharacter).where(OmbotCharacter.bot_id == character.ombot_id).where(
                    OmbotCharacter.character == character.character).where(OmbotCharacter.deleted == self.NO_DELETED)
                query_results = session.exec(statement).first()
                if query_results:
                    query_results.deleted = self.DELETED
                    logging.info("角色库中ombot【{}】的【{}】信息已成功删除。".format(character.ombot_id, character.character))
                else:
                    logging.warning("角色库中没有ombot【{}】的【{}】信息，无法删除。".format(character.ombot_id, character.character))
            session.commit()
