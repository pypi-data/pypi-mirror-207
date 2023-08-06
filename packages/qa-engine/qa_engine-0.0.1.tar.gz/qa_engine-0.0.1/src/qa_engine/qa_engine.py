import json

from langchain.prompts import PromptTemplate
from qa_engine.utils.chatgpt import ChatGPT
from langchain.chains import LLMChain
from qa_engine.prompt.prompt import QA_PROMPT, EXTRACT_EVENT_PROMPT, CHAT_PROMPT
from ombot_utils.log_handler import logging
from ombot_utils.schemas import ChatRecords
from ombot_utils.base.engine import BaseQAEngine
from ombot_utils import Callback, schemas
import re
import os

logging.init_logger('ombot', 'ombot')
os.environ.setdefault('IS_DEBUG', 'true')

class QAEngine(BaseQAEngine):
    def __init__(self):
        super().__init__()
        self.llm = ChatGPT()


    def gen_prompt(self, memory, problem):
        input = {"memory": memory, "problem": problem}
        output = self.chain.run(input)
        print(output)

    def extract_event(self, problem: str, events: str) -> str:
        """
        :param problem: 用户提出的问题
        :param events:  记忆库中的所有事件
        :return: 若提出问题中的事件和记忆库中事件匹配，则返回记忆库中的事件，若不匹配，则返回
        """
        prompt = PromptTemplate(
            template=EXTRACT_EVENT_PROMPT, input_variables=["problem", "events"]
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        input = {"problem": problem, "events": events}
        answer = chain.run(input)
        if re.search(r"输出：", answer):
            _, output = re.split(r"输出：", answer)
        # print(output)
        return output

    def question_answer(self, problem: str, memory: str) -> str:
        """
        :param problem:
        :param memory:
        :return:
        """
        prompt = PromptTemplate(
            template=QA_PROMPT, input_variables=["memory", "problem"]
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        input = {"problem": problem, "memory": memory}
        answer = chain.run(input)
        if re.search(r"输出：", answer):
            _, output = re.split(r"输出：", answer)
        return output

    def regular_chat(self, text: str) -> str:
        prompt = PromptTemplate(
            template=CHAT_PROMPT, input_variables=["problem"]
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        input = {"problem": text}
        answer = chain.run(input)
        # if answer.startswith("，"):
        #     answer = answer[1:]
        if re.search(r"回答：", answer):
            _, output = re.split(r"回答：", answer)
        return output

    def is_problem(self, problem: str, events: list):
        # problem = chat_records.get_recent(role_include=["user"])[0].content
        logging.info("获取最近的问题：【{}】".format(problem))
        events = str(events).replace("\'", "")
        logging.info("获取最近的事件库：【{}】".format(events))
        # 抽取问题中的事件
        event = self.extract_event(problem=problem, events=events)
        event = event.split("，")[0]
        logging.info("抽取问题中的事件：【{}】".format(event))
        if event != "不存在":
            return True, event, problem
        else:
            return False, event, problem

    def get_od_result(self, bot_id: str, event: str) -> list:
        memory_res = self.memory_handler.get_data(ombot_id=bot_id)
        od_result = []
        for img in memory_res:
            if img.od_result:
                img_res = []
                for bbox in img.od_result:
                    if event == bbox.label:
                        # bbox.json(ensure_ascii=False)
                        img_res.append(bbox.dict())
                if img_res:
                    od_result.append({"object": img_res, "id": img.image_time})
        return od_result


    def callback(self, callback, res):
        # callback = Callback(bot_id=bot_id, session_id=bot_id, endpoint=chat_records.callback)
        message = {
            "role": "assistant",
            "message_type": "text",
            "src_type": "text",
            "content": res,
            "objects": []
        }
        message = schemas.Message(**message)
        callback.call(message, schemas.OPT.CHAT_STATUS.END_ANSWER)

    # def _call(self, bot_id: str, chat_records: ChatRecords, callback: Callback):
    #     # 判断问题是否为专业问题
    #     flag, event, problem = self.is_problem(bot_id, chat_records)
    #     # 若为专业问题
    #     if flag:
    #         # 根据事件过滤记忆库
    #         od_result_summarys = self.get_od_result_summary(bot_id, event)
    #         logging.info("过滤后的记忆库为：【{}】".format(od_result_summarys))
    #         # 进行问答
    #         res = self.question_answer(problem=problem, memory="。".join(od_result_summarys))
    #         logging.info("最终回答结果为：【{}】".format(res))
    #         self.callback(callback, res)
    #     # 若为闲聊问题
    #     else:
    #         res = self.regular_chat(problem)
    #         logging.info("最终回答结果为：【{}】".format(res))
    #         self.callback(callback, res)

    def process(self, bot_id: str, data: str, events: list):
        flag, event, problem = self.is_problem(data, events)
        # 若为专业问题
        if flag:
            # 根据事件过滤记忆库
            result = self.get_od_result(bot_id, event)
            logging.info("过滤后的记忆库为：【{}】".format(result))
            if result:
                result = {"is_found": True, "od_result": result}
            else:
                result = {"is_found": False, "od_result": []}
        # 若为闲聊问题
        else:
            result = {"is_found": False, "od_result": []}
        return result





if __name__ == '__main__':
    qa = QAEngine()

    records = {
        "bot_id": "2",
        "session_id": "string",
        "callback": "string",
        "messages": [
            {
                "role": "user",
                "message_type": "text",
                "src_type": "text",
                "content": "窗帘绳子过长",
                "objects": [],
            }
        ]
    }
    records = ChatRecords(**records)


    qa.process(bot_id="2", chat_records=records)

