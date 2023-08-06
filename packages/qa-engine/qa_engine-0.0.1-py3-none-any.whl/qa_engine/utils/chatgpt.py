from langchain.llms.base import LLM

from typing import Optional, List
import requests
from qa_engine.config.config import EnvVars
from langchain.llms.utils import enforce_stop_tokens
import time

class ChatGPT(LLM):
    max_token: int = 4000
    temperature: float = 0.1
    top_p = 0.9
    history = []
    tokenizer: object = None
    model: object = None
    history_len: int = 10

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "ChatGPT"

    def _call(self,
              prompt: str,
              stop: Optional[List[str]] = None) -> str:

        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0
        }
        # print_text('=======prompt=======\n'+prompt, "blue")
        # print(len(prompt))
        for i in range(5):
            try:
                res = requests.post(url=EnvVars.CHATGPT_URL, json=body).json()
                response = res['choices'][0]['message']['content']
                break
            except:
                if i == 4:
                    raise "gpt cannot connect!"
                print("gpt cannot connect! Try it after 2s.")
                time.sleep(2)

        if stop is not None:
            response = enforce_stop_tokens(response, stop)
        self.history = self.history+[[None, response]]
        return response