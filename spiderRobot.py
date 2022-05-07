import json
import requests
import datetime
import base64

##树脂提醒
def getDingMes(content, expected_resin_recovery_time):
    now = datetime.datetime.today()
    time = str(now)[:-10]
    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=c5f1d9f67fead26c676c834522bd5b6971f24a5d0672a2d183e66f364f8d294f"  # hook
    HEADERS = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    print("运行应急食品")
    # massage是要推送的文字消息
    ##content = "##"  # 写要发的通知内容
    # stringBody = {
    #
    # 	"msgtype": "text",
    # 	"text": {
    # 		"content": content
    # 	},
    # 	"at": {
    # 		"isAtAll": False##1改为False尝试 true T大写
    # 	}
    # }
    stringBody = {
        "msgtype": "markdown",
        "markdown": {
            "title": "美味派蒙的Tips",
            "text": "**美味派蒙的Tips**\n"
                   	"\n---\n"
                   	+ ""+content +""+
					"![screenshot](http://photogz.photo.store.qq.com/psc?/V537n5HO2zWdr33fusFf2NdplO0A5lnG/05RlWl8gsTOH*Z17MtCBzJ9UBApIksNgD8gRbOZNuhAZGMX.*QwUErM0UMWN4my1KMq*nS0.0pP6gZDODhUYsQ!!/m&amp;bo=MgAlADIAJQARADc!&rf=viewer_311)\n"
                    "\n  **<font  color=#008000>Full Time: " + expected_resin_recovery_time[:-10] + "</font>**  \n"
                    "\n---\n"
                    " <font>Tip_Time: " + time + "</font> "
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)

    #图片转换
def getPngByte(pngPath):
    with open(pngPath,'rb') as f:
        pngByte = base64.b64encode(f.read())
    pngStr = pngByte.decode('ascii')
    return pngStr


##委托提醒
def getDingMes2(finished_task_num, total_task_num,is_extra_task_reward_received, current_expedition_num, expeditions_finish_num):
    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=d54f170402d81ef7a6e1e10c1d9b14f75e22e18558b13e6e33ebb7484739a918"  # hook
    HEADERS = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    print("运行凯瑟琳")

    #未完成委托字体会变红提醒
    not_finish ="**<font>已完成/未完成委托:</font>** "+"**<font color=#ff0000>"+str(finished_task_num)+"</font>**"+" **<font>/"+str(total_task_num)+"</font>** "+"**<font color=#ff0000>(未完成)\n</font>**"
    finished = "**<font>已完成/未完成委托:</font>** "+"**<font  color=#008000>"+str(finished_task_num)+"</font>**"+" **<font>/"+str(total_task_num)+"</font>** "+"**<font  color=#008000>(已完成)\n</font>**"
    #未领取委托奖励会变红
    rewardnt = " **<font color=#ff0000>-------------未领取每日委托奖励-------------</font>** "
    rewarded = " **<font  color=#008000>-------------已领取每日委托奖励-------------</font>** \n"
    #派遣探索
    expedition = "<font>派遣探索：</font>"+str(expeditions_finish_num)+"已完成<font>"+"</font>"+"<font> / </font>"+"<font>"+str(current_expedition_num)+"</font>"
    if(finished_task_num!=total_task_num):
        content=not_finish
    else:
        content=finished
    if(is_extra_task_reward_received==True):
        reward = rewarded
    else:
        reward = rewardnt
    stringBody = {
        "msgtype": "markdown",
        "markdown": {
            "title": "委托提醒",
            "text":" **<font>工作还不如睡觉,睡醒再做委托吧~</font>** \n"
                   "\n-\n"
                    "![screenshot](http://r.photo.store.qq.com/psc?/V537n5HO2zWdr33fusFf2NdplO0A5lnG/05RlWl8gsTOH*Z17MtCBzIMgvNWXO0eFMdXMHvPhobuUUtKxj5fpJyEEhhY2zI6yWU1XnNzMVGspwa5o*izQLg!!/o&ek=1&kp=1&pt=0&bo=qwJ*AasCfwERADc!&tl=1&tm=1651842000&dis_t=1651845038&dis_k=8799907bcce5e490d400f77d8963e1d9&sce=0-12-12&rf=viewer_311)"
                    +content+"\n\n"
                    +reward+
                    "\n---\n"
                   + expedition


        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)



##洞天宝钱
def getDingMes3(current_home_coin,max_home_coin,expected_home_coin_recovery_time):
    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=0e9dc95022bf8384b6fd9ee5241a1ed7a00f8effd187393f28e6a6e80e91d276"  # hook
    HEADERS = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    ##当前洞天宝钱
    if(current_home_coin>=max_home_coin*0.9): #超过90%报警,字体变红
        color = "#ff0000"
    else:
        color = "#008000"

    current = " **<font color="+color+">"+str(current_home_coin)+" /</font>** "
    ##满洞天宝钱
    max = "**<font>"+str(max_home_coin)+"</font>** "
    ##预计恢复满时刻
    time = str(expected_home_coin_recovery_time)[:-10]

    ##宝钱产量/溢出:  预计恢复时间:
    num = " **<font>宝钱产量/最大宝钱量:</font>** " + current + max
    recovery = " **<font>回  满  时  间 :</font>** " + " **<font color="+color+">"+ time + "</font>** "
    print("运行阿圆")

    stringBody = {
        "msgtype": "markdown",
        "markdown": {
            "title": "洞天宝钱",
            "text":" **<font>销虹霁雨真君</font>** \n"
            "\n---\n"
            +num+"\n"
            "\n---\n"
            +recovery
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }

    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)
