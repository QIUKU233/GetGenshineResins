# getGenshineResins

##### 	前言：新人的第一个github，请多多指教！" ^-^ " Genshine get resins IN **python**只是完成了预期的功能，在文件结构，代码优化方面只能说是凑合，毕竟（如果您的代码以一种奇怪的方式跑起来，那么请不要再动他了。深感不足，学有所成后会重构项目，现在权当记录一些好玩的事。

​	Hello, This is my first github, plz give me some advice, ill appreciate it very much ! !

##### 	正文：

功能和实现效果：

功能：利用获取的米游社cookie，github的Action定时功能，和钉钉开放的群机器人接口 ，实现定期执行获取当前游戏内树脂的数量，委托完成数量，委托奖励领取情况，派遣探索完成情况，当前洞天宝钱产生数量并且发送到钉钉。


实现效果：

操作步骤:

1、获取米游社cookie
---进入米游社官网原神板块（https://bbs.mihoyo.com/ys/）
---登录自己的账号
---按下F12进行中断
---把getcookie.text里的代码复制到控制台获取cookie
2、到 simpleGenshineGetResinsApi.py 里把自己的UID和cookie粘贴进去
3、到钉钉创建一个群（可以拉两个小伙伴创群然后再把他们踢了），创建自定义机器人
注意事项：
---登录成功后若登出则cookie会失效（浏览器可以关闭）



关于Action：
Action建立一个python工作流，可以达到自动运行而不需自己搭建服务器的目的，其中的间隔运行时间可以自行调整，需要注意的是schedule最少5min能执行一次，详细参见workflow中的xml文件。
