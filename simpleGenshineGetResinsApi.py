import datetime

import requests
import random
import time
import hashlib ##md5()使用
import json
import simpleGenshineHandle

import spiderRobot


##这里设置个人信息
GenshinID = "" ##-------------原神UID
cookie = "" ##-------------cookie

##这里设置mhy信息
salt = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"
dailyNoteURL = "https://api-takumi.mihoyo.com/game_record/app/genshin/api/dailyNote?server=cn_gf01&role_id=" + GenshinID
mhyVersion = "2.27.2"##"2.11.1"
client_type = "5"


##使用此方法合成请求头
def getResinsRequest():
    Header = {

        'Accept': "application/json, text/plain, */*",
        ##'DS': DSGet("role_id=" + GenshinID + "&server=cn_gf01"),
        'DS': DSGet(f"role_id="+GenshinID+"&server=cn_gf01"),
        'Origin': "https://webstatic.mihoyo.com",
        ##这个变量在code.setting里
        'x-rpc-app_version': mhyVersion,
        ##'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Unspecified Device) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 miHoYoBBS/2.2.0',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
        ##client_type在code.setting里
        'x-rpc-client_type': client_type,
        'Referer': "https://webstatic.mihoyo.com/app/community-game-records/index.html?v=6",
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'X-Requested-With': 'com.mihoyo.hyperion',

        "Cookie": "UM_distinctid=17f8db4b32d8c-0ffa3c150a1e99-56171d51-144000-17f8db4b32e3f; _MHYUUID=f1f89b39-ec7c-4836-8b52-90f14f38ee1e; mi18nLang=zh-cn; _ga=GA1.2.2011675086.1647349906; _ga_R8CG4VZ69C=GS1.1.1650699888.1.1.1650700148.0; _gid=GA1.2.11261065.1651675101; ltoken=weTSg29wvNtzhUmHrv50TRrBfDzIoUsIYtFaDuRd; ltuid=306029388; cookie_token=forIn80XSm10pKPNTATgNEekQIjRs2DS5QT1PI37; account_id=306029388; CNZZDATA1275023096=85683300-1647344570-%7C1651682064"##cookie
    }
    ##test
    print("dailyNoteURL:"+dailyNoteURL)
    print("cookie:"+cookie)
    print("DS:"+DSGet("role_id=" + GenshinID + "&server=cn_gf01"))
    return Header

##尝试使用此方法向米游社接口访问
def getResins():
    Header=getResinsRequest()
    req = requests.get(dailyNoteURL, headers=Header)
    data = json.loads(req.text)
    # if(data[data]==0):
    #     print("获取失败")
    return req

##以下两个函数应该是mhy的算法
def DSGet(query: str):
    n = salt
    i = str(int(time.time()))
    r = str(random.randint(100001, 200000))
    b = ""
    q = query
    c = md5("salt=" + n + "&t=" + i + "&r=" + r + "&b=" + b + "&q=" + q)
    return i + "," + r + "," + c
def md5(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()
##运行
##req=getResins()
##处理返回信息
##current_resin,max_resin,expected_resin_recovery_time=simpleGenshineHandle.handleReq(req)

#此函数控制某个机器人是否发消息
def main(Res,Que,Coi,req):
    ##----树脂板块
    if(Res==True):
      getResinNow(req)
    ##-------获取委托
    if (Res == True):
      getQuestNow(req)
    ##------------阿圆洞天宝钱
    if (Res == True):
      getCoinNow(req)

##向钉钉发送消息(树脂板块)
def getResinNow(req):
    current_resin,max_resin,expected_resin_recovery_time= simpleGenshineHandle.handleReq1(req)
    c0 = "  旅行者:  " + GenshinID + " \n---\n"
    c1 = "**当前：**"
    # resin>=140时让字体变红
    if (current_resin < 140):
        content = c1 + " **<font color=#008000>" + str(current_resin) + "</font>** " + " **<font>/160</font>** "
    elif (current_resin >= 140):
        content = c1 + " **<font color=#ff0000>" + str(current_resin) + "</font>** " + " **<font>/160</font>** "

    spiderRobot.getDingMes(content, expected_resin_recovery_time)


##-------获取委托
def getCoinNow(req):
         #如果没有做委托则提醒
    finished_task_num, total_task_num,is_extra_task_reward_received, current_expedition_num, expeditions_finish_num = simpleGenshineHandle.handleReq2(req)
    spiderRobot.getDingMes2(finished_task_num, total_task_num,is_extra_task_reward_received, current_expedition_num, expeditions_finish_num)

##------------阿圆洞天宝钱
def getQuestNow(req):
    current_home_coin,max_home_coin,expected_home_coin_recovery_time = simpleGenshineHandle.handleReq3(req)
    spiderRobot.getDingMes3(current_home_coin,max_home_coin,expected_home_coin_recovery_time)

#运行此方法即可
#ACTION控制的情况有：（委托奖励领取不运行委托）（宝钱不到1980宝钱不运行宝钱），树脂大于140时运行，宝钱大于2200*0.9=1980时运行，17点委托没做或者委托奖励没领取时时运行
#由于体力8分钟回复一点 排除晚上00--8：00运行时间 8:00 11:00 14:00 17:00 20:00 23:00
def action():
    #获取当前时间
    SYSTEM_TIME = datetime.datetime.now()
    hour1 = str(SYSTEM_TIME)[11]
    hour2 = str(SYSTEM_TIME)[12]
    min1 = str(SYSTEM_TIME)[14]
    min2 = str(SYSTEM_TIME)[15]

    #08:00的第一次运行
    req = getResins()
    data = json.loads(req.text)
    data = data['data']
    current_resin = data['current_resin']
    is_extra_task_reward_received = data['is_extra_task_reward_received']
    current_home_coin = data['current_home_coin']
    max_home_coin = data['max_home_coin']

    #8点and 23点的提醒
    if (int(hour1)*10 + int(hour2) >= 8):
        if (current_resin >= 120 and is_extra_task_reward_received == False and current_home_coin >= max_home_coin * 0.7):
            main(True, True, True,req)
        elif (current_resin >= 120 and is_extra_task_reward_received == False and current_home_coin <= max_home_coin * 0.7):
            main(t, True, False,req)
        elif (current_resin >= 120 and is_extra_task_reward_received == True and current_home_coin >= max_home_coin * 0.7):
            main(True, False, True,req)
        elif (current_resin >= 120 and is_extra_task_reward_received == True and current_home_coin <= max_home_coin * 0.7):
            main(True, False,False,req)
        elif (current_resin <= 120 and is_extra_task_reward_received == False and current_home_coin >= max_home_coin * 0.7):
            main(False,True,True,req)
        elif (current_resin <= 120 and is_extra_task_reward_received == False and current_home_coin<=max_home_coin*0.7):
            main(False, True, False,req)
        elif (current_resin <= 120 and is_extra_task_reward_received == True and current_home_coin <= max_home_coin * 0.7):
            main(False,False,False,req)
        elif (current_resin <= 120 and is_extra_task_reward_received == True and current_home_coin >= max_home_coin * 0.7):
            main(False,False,True,req)

    #此后每间隔半个小时运行一次，每次计算资源数量


action()
