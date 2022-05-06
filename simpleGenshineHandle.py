import json
import datetime


def handleReq(req):
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



