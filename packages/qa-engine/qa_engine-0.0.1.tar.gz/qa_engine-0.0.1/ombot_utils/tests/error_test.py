from ombot_utils import VQLError
import os

os.environ.setdefault('IS_DEBUG', 'true')
from time import time

s = time()
os.environ.get('IS_DEBUG', 'false')
print((time() - s)*1000)
try:
    raise VQLError(500)
    raise VQLError(500, msg='测试错误处理')
    raise VQLError(500, detail='错误详细信息')
except Exception as error:
    print(error)
    print(error.detail)
