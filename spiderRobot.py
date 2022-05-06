import json
import requests
import datetime

def getDingMes(content, expected_resin_recovery_time):

    now = datetime.datetime.today()
    time = str(now)[:-10]
    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=c5f1d9f67fead26c676c834522bd5b6971f24a5d0672a2d183e66f364f8d294f"  # hook
    HEADERS = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    print("运行钉钉程序")
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
                   	+ content +
					"![screenshot](http://photogz.photo.store.qq.com/psc?/V537n5HO2zWdr33fusFf2NdplO0A5lnG/05RlWl8gsTOH*Z17MtCBzJ9UBApIksNgD8gRbOZNuhAZGMX.*QwUErM0UMWN4my1KMq*nS0.0pP6gZDODhUYsQ!!/m&amp;bo=MgAlADIAJQARADc!&rf=viewer_311)"
                    "\n---\n"
                    "<font  color=#008000>Full Time: " + expected_resin_recovery_time[:-10] + "</font>"
                    "\n---\n"
                    ##"> ![screenshot](http://photogz.photo.store.qq.com/psc?/V537n5HO2zWdr33fusFf2NdplO0A5lnG/05RlWl8gsTOH*Z17MtCBzIW13L33N0V4W0K5xCv6xQBJnkrrJNZtavcdzMoIOQ2NT.m19K.jMTSQvrlmtrE2QQ!!/m&amp;bo=PAAsADwALAARADc!&rf=viewer_311)"
                      "<font>Tip_Time: " + time + "</font>"
        },
        "at": {
            "atMobiles": [
                "150XXXXXXXX"
            ],
            "isAtAll": False
        }
    }
    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)


def getDingMes2(content, expected_resin_recovery_time):
    content = "111"
    expected_resin_recovery_time = "12311111"
    now = datetime.datetime.today()
    time = str(now)[:-10]
    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=c5f1d9f67fead26c676c834522bd5b6971f24a5d0672a2d183e66f364f8d294f"  # hook
    HEADERS = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    print("运行钉钉程序")
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
                    "<font color=#008000>" + content + "</font><font>/160</font>"
                    "![screenshot](http://photogz.photo.store.qq.com/psc?/V537n5HO2zWdr33fusFf2NdplO0A5lnG/05RlWl8gsTOH*Z17MtCBzJ9UBApIksNgD8gRbOZNuhAZGMX.*QwUErM0UMWN4my1KMq*nS0.0pP6gZDODhUYsQ!!/m&amp;bo=MgAlADIAJQARADc!&rf=viewer_311)"
                    "\n---\n"
                    "<font>Recovery_Time：" + expected_resin_recovery_time + "</font>"
                     "\n---\n"
                    ##"> ![screenshot](http://photogz.photo.store.qq.com/psc?/V537n5HO2zWdr33fusFf2NdplO0A5lnG/05RlWl8gsTOH*Z17MtCBzIW13L33N0V4W0K5xCv6xQBJnkrrJNZtavcdzMoIOQ2NT.m19K.jMTSQvrlmtrE2QQ!!/m&amp;bo=PAAsADwALAARADc!&rf=viewer_311)"
                     "<font size=3>Tip_Time: " + time + "<font>"
        },
        "at": {
            "atMobiles": [
                "150XXXXXXXX"
            ],
            "isAtAll": False
        }
    }
    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)
