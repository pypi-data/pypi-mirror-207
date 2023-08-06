from ombot_utils import EventDataHandler
from ombot_utils.schemas import EventInput, EventObject

# 事件列表events
event_dicts = {
    "摔倒的人": {"weight": 0.10, "detailed_events": ["摔倒的人"], "status": "observed", "action": "warn",
             "solver_event": "摔倒的人被扶起"},
    "饮料打翻": {"weight": 0.10, "detailed_events": ["饮料打翻"], "status": "no observation", "action": "warn",
             "solver_event": "打扫打翻的饮料"},
    "购物车失控": {"weight": 0.10, "detailed_events": ["购物车失控", "购物车撞人", "购物车撞到货架", "购物车撞到柜台", "购物车撞到墙壁"],
              "status": "no observation", "action": "warn", "solver_event": "购物车停下来"},
    "货架倒塌": {"weight": 0.10, "detailed_events": ["货架倒下", "货物散落在地上"], "status": "no observation", "action": "warn",
             "solver_event": "清理倒塌的货架"},
    "孩子走失": {"weight": 0.10, "detailed_events": ["孩子不见了", "孩子离开了", "孩子走丢了", "孩子失踪了"], "status": "no observation",
             "action": "warn", "solver_event": "寻找走失的孩子"},
    "火灾": {"weight": 0.10, "detailed_events": ["火灾", "火场"], "status": "no observation", "action": "warn",
           "solver_event": "扑灭火源"},
    "盗窃行为": {"weight": 0.10, "detailed_events": ["盗窃者", "偷东西的人", "入室行窃者", "小偷", "窃贼"], "status": "no observation",
             "action": "warn", "solver_event": "无"},
    "地面湿滑": {"weight": 0.1, "detailed_events": ["地面湿滑", "地面有水", "地面有液体"], "status": "no observation", "action": "warn",
             "solver_event": "清理地面上的液体"}
}

event_objects = [EventObject(event_name=event_name, **dict(event_val)) for event_name, event_val in event_dicts.items()]
events = [EventInput(ombot_id="2", event=event) for event in event_objects]

# 初始化事件处理器
eventdh = EventDataHandler()

# 添加数据
eventdh.add_data(events)
# 查询数据
result = eventdh.get_data(ombot_id=2, event_name="摔倒的人",number=5)
print(result)
# 删除数据
eventdh.delete_data(ombot_id=2, event_names=["摔倒的人", "饮料打翻", "购物车失控", "货架倒塌", "孩子走失", "火灾", "盗窃行为", "地面湿滑"])

from ombot_utils import MemoryDataHandler
from ombot_utils.schemas import MemoryInput, DetObject


# 记忆列表memorys
od_result = [DetObject(bbox=[2.,3.,3.,3.],label="a",conf=0.6),DetObject(bbox=[2.,3.,3.,3.],label="a",conf=0.6)]


memorys = [MemoryInput(ombot_id=ombot_id, memory=memory, od_result= od_result, region_caption=od_result, image_time=im_time) for ombot_id, memory,im_time in
            [(1, "一瓶矿泉水洒了","2023:04:20 00:00:00"),
            (2, "小偷偷了一盒三明治，未付钱","2023:04:20 00:00:05"), (2, "厨房燃气灶未关火","2023:04:20 00:00:10"), (2, "小孩哇哇大哭","2023:04:20 00:00:15"), (2, "摔倒在地上","2023:04:20 00:00:20"), (2, "跳起来的人","2023:04:20 00:00:25")]]
# 初始化记忆处理器
memorydh = MemoryDataHandler()

# 添加数据
memorydh.add_data(memorys)
# 查询数据
result = memorydh.get_data(ombot_id=2, number=5)
# 删除数据
memorydh.delete_data(ombot_id=2,memory_ids=[1,2,3,4,5])


from ombot_utils import CharacterDataHandler
from ombot_utils.schemas import CharacterInput

# 角色characters
characters = [CharacterInput(ombot_id=id, character=char, traits=traits, status=status) for id, char, traits, status in
             [(1, "小明","开朗活泼","厨房"), (2, "小丽","细心","卧室")]]

# 初始化角色处理器
characterdh = CharacterDataHandler()

# 添加数据
characterdh.add_data(characters)
# 查询数据
result = characterdh.get_data(1, number=5)
print(result)
# 删除数据
characterdh.delete_data(characters)

