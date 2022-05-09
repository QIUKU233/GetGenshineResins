# GenshineResins
新人的第一个github小程序，请多多指教！" ^-^ "
Genshine get resins IN **python**

#需要的额外模块:requests

#操作步骤:
1、获取cookie 
    进入米游社官网(https://bbs.mihoyo.com/ys/)--登录--F12中断--中断控制台里输入代码并回车
    
    ![image text]
    (https://github.com/QIUKU233/GenshineResins/blob/master/how_to_get_cookie.png?raw=true)

    
2、cookie粘贴到 simpleGenshineGetResinsApi.py 的 cookie ，GenshinID填自己的UID
3、运行simpleGenshineGetResinsApi.py
![Uploading (9BS%YA4S@O%_JA_JEN~}2K.png…]()


[获取cookie]
var cookie=document.cookie;var ask=confirm('Cookie:'+cookie+'\n\nDo you want to copy the cookie to the clipboard?');if(ask==true){copy(cookie);msg=cookie}else{msg='Cancel'}

