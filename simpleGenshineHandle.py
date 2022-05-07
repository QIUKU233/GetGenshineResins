import json
import datetime

##树脂
def handleReq1(req):
    data = json.loads(req.text)
    data = data['data']
    # 当前原粹树脂值
    current_resin = data['current_resin']
    # 原粹树脂最大值
    max_resin = data['max_resin']
    # 原粹树脂补满剩余时间
    ##抄的方法，大概是返回补充满的时间
    resin_recovery_time = data['resin_recovery_time']
    resin_recovery_time_hours = str(datetime.timedelta(seconds=int(resin_recovery_time)))
    expected_resin_recovery_time = str(
        datetime.datetime.now() + datetime.timedelta(seconds=int(resin_recovery_time)))
    return current_resin,max_resin,expected_resin_recovery_time

##委托 && 派遣探索
def handleReq2(req):
    data = json.loads(req.text)
    data = data['data']
    # 完成委托数
    finished_task_num = data['finished_task_num']
    # 委托总数
    total_task_num = data['total_task_num']
    #委托奖励是否领取
    is_extra_task_reward_received = data['is_extra_task_reward_received']
    #当前派遣数
    current_expedition_num = data['current_expedition_num']
    str_data=str(data)
    #计算完成派遣数量
    expeditions_finish_num = current_expedition_num-str_data.count("Ongoing")
    return finished_task_num,total_task_num,is_extra_task_reward_received,current_expedition_num,expeditions_finish_num

##洞天宝钱
def handleReq3(req):
    data = json.loads(req.text)
    data = data['data']
    # 当前硬币数
    current_home_coin = data['current_home_coin']
    # 最大硬币数
    max_home_coin = data['max_home_coin']
    # 硬币补满所需时间
    ##抄的方法，大概是返回补充满的时间
    home_coin_recovery_time = data['home_coin_recovery_time']
    home_coin_recovery_time_hours = str(datetime.timedelta(seconds=int(home_coin_recovery_time)))
    expected_home_coin_recovery_time = str(
        datetime.datetime.now() + datetime.timedelta(seconds=int(home_coin_recovery_time)))
    return current_home_coin,max_home_coin,expected_home_coin_recovery_time


