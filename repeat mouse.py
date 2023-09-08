# -*- coding: utf-8 -*-
try:
    import os
    import time
    import pyautogui
    import json
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1.5
    pyautogui.onScreen(60, 60)
except BaseException as error:
    print('发生错误:'+str(error))
    time.sleep(10)
s=0
d=0
cishu=1
cishu2=0
cishu3=1
cishu4=1
w=0
L0=[]
savelist =['L0']
def save_save():  # 保存存档
    global error
    try:
        savefile = open(os.getcwd()+r'/playersave.txt', mode='w+')
        globallist = globals()
        savedict = {}
        for val in savelist:
            savetempdict = {val: globallist[val]}
            savedict.update(savetempdict)
        savefile.write(json.dumps(savedict))
        savefile.close()
        print('存档完毕')
    except BaseException as error:
        print('发生错误:'+str(error))
def save_read(): 
    global error
    try:  
        savefile = open(os.getcwd()+r'/playersave.txt', mode='r+') 
        savereaddata = json.loads(savefile.read()) 
        for val in savereaddata:
            if str(type(savereaddata[val])) == "<class 'str'>":
                exec('global '+val+' ; '+val+"='"+str(savereaddata[val])+"'")
            else:
                exec('global '+val+' ; '+val+"="+str(savereaddata[val]))
            savefile.close()
        print('读档完毕')
    except IOError:
        print('没有存档文件')
    except BaseException as error:
        print('发生错误:'+str(error))
print('欢迎使用repeat mouse,该软件可为您解决重复枯燥的机械操作的烦恼，使用方法如下：')
print('正常使用：设置好后，鼠标在一个坐标上连续停留的时间若超过4s，则该坐标将记录在案。记录的坐标达到设置的一周期点击次数时，则该程序即将开始运行。')
print('存档：顾名思义，若您将频繁使用一个序列周期，可以提前设置保存。')
print('读档：执行保存的机械操作。')
mode=input('1.存档2.读档3.正常使用')
if mode=='1':
    n = int(input('一周期内点击次数:'))
    stay = int(input('每次点击间隔时间:'))
    repeat = int(input('重复执行次数:'))
    input('按回车开始记录')
    while cishu <= n:
        time.sleep(0.1)
        d = pyautogui.position()
        if d == s:
            cishu2 = cishu2+1
            if cishu2 > 39:
                cishu = cishu+1
                L0.append(d)
                cishu2 = 0
        else:
            cishu2 = 0
        s = d
    save_save()
elif mode=='2':
    save_read()
    n = int(input('一周期内点击次数:'))
    stay = int(input('每次点击间隔时间:'))
    repeat = int(input('重复执行次数:'))
    input('按回车确认开始执行预设脚本')
    while cishu3 <= repeat:
        cishu3 = cishu3+1
        while cishu4 <= n:
            cishu4 = cishu4+1
            xy = str(L0[w])
            x1, y1 = xy.split(',')
            x2, x3 = x1.split('[')
            y2, y3 = y1.split(']')
            x3 = int(x3)
            y2 = int(y2)
            w = w+1
            pyautogui.click(x=x3, y=y2, button='left', clicks=1, interval=stay)
    print('感谢您的使用，若您觉得本程序好用，可以分享给小伙伴们(*^▽^*)！作者的编程交流群：908144376')
    time.sleep(3600)
elif mode == '3':
    n=int(input('一周期内点击次数:'))
    stay = int(input('每次点击间隔时间:'))
    repeat = int(input('重复执行次数:'))
    input('按回车开始记录')
    while cishu<=n:
        time.sleep(0.1)
        d = pyautogui.position()
        if d==s:
            cishu2=cishu2+1
            if cishu2>39:
                cishu=cishu+1
                L0.append(d)
                cishu2=0
        else:
            cishu2=0
        s=d
    input('按回车确认开始执行预设脚本')
    while cishu3<=repeat:
        cishu3=cishu3+1
        while cishu4<=n:
            cishu4=cishu4+1
            xy=str(L0[w])
            x1, y1 = xy.split(',')
            x2,x3=x1.split('(')
            y2,y3=y1.split(')')
            x4,x5=x3.split('=')
            y4,y5=y2.split('=')
            x5=int(x5)
            y5=int(y5)
            w = w+1
            pyautogui.click(x=x5, y=y5, button='left', clicks=1, interval=stay)
    print('感谢您的使用，若您觉得本程序好用，可以分享给小伙伴们(*^▽^*)！作者的编程交流群：908144376')
    time.sleep(3600)
