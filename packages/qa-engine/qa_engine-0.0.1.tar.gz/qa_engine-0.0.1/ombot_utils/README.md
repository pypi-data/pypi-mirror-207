# ombot_utils

OMBot项目的通用工具包，提供项目通用的处理模块，包括
- 数据结构（`schemas`）
- 日志处理（`log_handler`）
- 回调处理（`callback_handler`）
- 错误处理（`error_handler`）
- 数据处理（`data_handler`） 
******

## 1. 数据结构（`schemas`）  
数据结构模块定义了程序运行中所有使用的数据交互结构，保证各模块之间的接入接口规范。  

### 1.1. 介绍   
常用的数据结构包括：
- ChatRecords：聊天记录，包括一次聊天交互过程中的所有上下文记录。包含 `get_recent` 方法，返回最近的聊天记录。可以把对象当做聊天记录（Message）的列表进行取长度，循环，索引取值赋值的操作。
- Message：聊天信息。
- DetObject：识别目标，图片类信息经过处理后，有可能返回的识别结果。
- Reply：回复消息的结构。
### 1.2. 可选参数（`OPT`）  
可选参数用于定义数据结构中的字段可选参数值，保证字段的有效性。  
OPT 类可以用于参数取值，避免对可选值的记忆。
```
from ombot_utils import schemas

reply = schemas.Reply(
    code=200,
    took=10,
    bot_id=records.bot_id,
    session_id=records.session_id,
    dialog_id='111',
    status=schemas.OPT.CHAT_STATUS.END_ANSWER,
    message=message,
)
```

## 2 日志处理（`log_handler`）  
日志处理模块用于替换Python的默认日志处理。logging 模块 import 后需要进行一次**初始化**，之后可以直接使用，方法与Python的logging模块相同。
```
from ombot_utils import logging
logging.init_logger('ombot', 'ombot')

logging.info('Logging something')
```

## 3 回调处理（`callback_handler`）
回调模块包含三个方法，**setup** 方法用来设置回调参数，**call** 方法用来回调正确识别的结果， **error** 方法用来回调处理失败的信息。
```
from ombot_utils import callback
from ombot_utils.schemas import OPT

callback.setup(chat_records)

callback.call(reply, OPT.CHAT_STATUS.END_ANSWER)
callback.error('Error information')
```

## 4 错误处理（`error_handler`）
使用错误处理类 `VQLError` 进行错误处理。
最简单的用法是使用错误代码抛出错误：
```
from ombot_utils import VQLError
raise VQLError(500)
```
可以使用自定义的错误信息代替内置的错误信息  
**注意：错误信息可能会被显示在用户界面上，因此请使用简单明了的描述语言**
```
from ombot_utils import VQLError
raise VQLError(500, msg='自定义错误信息')
```
同时，可以使用'detail'字段回传报错的详细错误信息。这部分信息会出现在系统日志中，用于错误排查。
```
from ombot_utils import VQLError
import traceback

raise VQLError(500, detail=traceback.format_exc())
```

## 5 数据处理
使用数据处理工具可实现获取、删除、添加数据库操作，数据库包括事件库、记忆库、角色库。  
### 5.1 设置数据库信息环境变量
```Shell
MYSQL_DB='ombot_test'  # 数据库名
MYSQL_USER='root'  # 数据库账号
MYSQL_PASSWD='123123'  # 数据库登陆密码
MYSQL_HOST='10.8.21.36'  # 数据库地址
MYSQL_PORT='3306'  # 端口
```
### 5.2事件库(EventDataHandler)
```python
from  ombot_utils import EventDataHandler
from ombot_utils.schemas import EventInput, EventObject

# 事件列表events
event_dicts = {
    "摔倒的人": {"weight": 0.10, "detailed_events": ["摔倒的人"], "status": "observed", "action": "warn",
             "solver_event": "摔倒的人被扶起"},
    "饮料打翻": {"weight": 0.10, "detailed_events": ["饮料打翻"], "status": "no observation", "action": "warn",
             "solver_event": "打扫打翻的饮料"}}
event_objects = [EventObject(event_name=event_name, **dict(event_val)) for event_name, event_val in event_dicts.items()]
events = [EventInput(ombot_id=2, event=event) for event in event_objects]


# 初始化事件处理器
eventdh = EventDataHandler()

# 添加数据
eventdh.add_data(events)
# 查询数据
result = eventdh.get_data(ombot_id=2, number=5)
# 删除数据
eventdh.delete_data(ombot_id=2, event_names=["摔倒的人", "饮料打翻"])
```
添加数据：  
  - 方法：add_data(events)
  - 输入：  
    events：list[EventInput]，必选，EventInput中`ombot_id`和`event`是必选属性。
  - 输出：  
    None  
    
查询数据:
  - 方法: get_data(ombot_id=2, number=5，get_keys=None)
  - 输入：
    - ombot_id：int，必选，
    - number：int，可选，输出最近的查询数量，默认输出全部结果。
    - get_keys：list[str，可选，查询关键，默认：["id", "event", "source"] 
  - 输出：  
    list[OmbotEvent]
    
删除数据：匹配输入EventInput中的`ombot_id`和`event`进行删除。
  - 方法：delete_data(events)
  - 输入：  
    events：list[EventInput]，必选，EventInput中`ombot_id`和`event`是必选属性。
  - 输出：  
    None  
  

### 5.3 记忆库(MemoryDataHandler)
```python
from  ombot_utils import MemoryDataHandler
from ombot_utils.schemas import MemoryInput

# 记忆列表memorys
memorys = [MemoryInput(ombot_id=ombot_id, memory=memory,image_time=im_time) for ombot_id, memory,im_time in
            [(1, "一瓶矿泉水洒了","2023:04:20 00:00:00"), 
            (2, "小偷偷了一盒三明治，未付钱","2023:04:20 00:00:05"), (2, "厨房燃气灶未关火","2023:04:20 00:00:10"), (2, "小孩哇哇大哭","2023:04:20 00:00:15"), (2, "摔倒在地上","2023:04:20 00:00:20"), (2, "跳起来的人","2023:04:20 00:00:25")]]
# 初始化记忆处理器
memorydh = MemoryDataHandler()

# 添加数据
memorydh.add_data(memorys)
# 查询数据
result = memorydh.get_data(ombot_id=2, number=5)
# 删除数据
memorydh.delete_data(ombot_id=2,memary_ids=[6])
```
添加数据：  
  - 方法：add_data(memorys)
  - 输入：  
    events：list[MemoryInput]，必选，MemoryInput`ombot_id`、`memory`、`image_time`是必选属性。
  - 输出：  
    None  
    
查询数据:
  - 方法: get_data(ombot_id=2, number=5，get_keys=None)
  - 输入：
    - ombot_id：int，必选，
    - number：int，可选，输出最近的查询数量，默认输出全部结果。
    - get_keys：list[str，可选，查询关键，默认：["id", "memory", "od_result_summary", "anomalous_summary", "caption_summary",
                        "region_caption_summary", "image_time"]
  - 输出：  
    list[OmbotMemory]
    
删除数据：匹配输入中的`ombot_id`和`ids`进行删除。
  - 方法：delete_data(ombot_id, ids)
  - 输入： 
    - ombot_id：int，必选， 
    - ids：list[int]，必选，记忆库中的唯一id列表。
  - 输出：  
    None  
  


### 5.4 角色库(CharacterDataHandler)
```python
from ombot_utils import CharacterDataHandler
from ombot_utils.schemas import CharacterInput

# 角色characters
characters = [CharacterInput(ombot_id=id, character=char) for id, char in
             [(1, "小明，开朗活泼"), (2, "小丽，细心"), (2, "认真"), (2, "仔细"), (2, "粗心"), (2, "贪玩")]]

# # 初始化角色处理器
characterdh = CharacterDataHandler()

# 添加数据
characterdh.add_data(characters)
# 查询数据
result = characterdh.get_data(2, number=5)
# 删除数据
characterdh.delete_data(characters)
```
添加数据：  
  - 方法：add_data(characters)
  - 输入：  
    events：list[CharacterInput]，必选，CharacterInput`ombot_id`和`character`是必选属性。
  - 输出：  
    None  
    
查询数据:
  - 方法: get_data(ombot_id=2, number=5，get_keys=None)
  - 输入：
    - ombot_id：int，必选，
    - number：int，可选，输出最近的查询数量，默认输出全部结果。
    - get_keys：list[str，可选，查询关键，默认：["id", "character"]
  - 输出：  
    list[OmbotCharacter]
    
删除数据：匹配输入CharacterInput中的`ombot_id`和`character`进行删除。
  - 方法：delete_data(characters)
  - 输入：  
    characters：list[CharacterInput]，必选，CharacterInput`ombot_id`和`character`是必选属性。
  - 输出：  
    None  
## 调试模式（Debug mode）
设置环境变量 ```IS_DEBUG=True``` 可以开启debug模式，在该模式下有几点和正常模式不同：
- 回调将不进行接口调用，仅日志显示回调数据。
- 日志将不保存文件，仅作显示。
- 错误将主动显示detail

## 注意
- 直接从代码安装时需要pip>=22.0。可以使用 `python -m pip install pip==22.2.2` 来升级pip。
- python=3.9，data_handler 查询数据库sqlmodel需要python3.9以上。