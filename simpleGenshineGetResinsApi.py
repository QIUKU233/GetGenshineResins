import requests
import random
import time
import hashlib ##md5()使用
import json
import simpleGenshineHandle

import spiderRobot


##这里设置个人信息
GenshinID = "110457304" ##-------------非UID，是米游社id:306029388 uid:110457304
cookie = "UM_distinctid=17f8db4b32d8c-0ffa3c150a1e99-56171d51-144000-17f8db4b32e3f; _MHYUUID=f1f89b39-ec7c-4836-8b52-90f14f38ee1e; mi18nLang=zh-cn; _ga=GA1.2.2011675086.1647349906; _ga_R8CG4VZ69C=GS1.1.1650699888.1.1.1650700148.0; _gid=GA1.2.11261065.1651675101; ltoken=weTSg29wvNtzhUmHrv50TRrBfDzIoUsIYtFaDuRd; ltuid=306029388; cookie_token=forIn80XSm10pKPNTATgNEekQIjRs2DS5QT1PI37; account_id=306029388; CNZZDATA1275023096=85683300-1647344570-%7C1651682064"

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

def main():
    ##获取树脂
    req = getResins()
         ##处理返回信息
    current_resin,max_resin,expected_resin_recovery_time= simpleGenshineHandle.handleReq(req)
   # if(int(current_resin)>=120):
        ##向钉钉发送消息
    c0 = "旅行者:"+GenshinID+"\n---\n"
    c1 = "当前："
    content=c0+c1+"<font color=#008000>"+str(current_resin)+"</font><font>/160</font>"
    print(content)
    spiderRobot.getDingMes(content,expected_resin_recovery_time)
 #   else:
   #     print("树脂回复还没准备满")
main()