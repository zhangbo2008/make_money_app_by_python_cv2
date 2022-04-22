import utils,os
def click_close_button(littlepngs=['bugclose.png', 'bugclose2.png', 'bugclose3.png', 'bugclose4.png', 'bugclose5.png'],
                       sleeptime=1):
    print("下面关闭bug_close")
    os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')

    os.system('adb pull /sdcard/screencap.png screencap.png')  # 这时手机的屏幕就保存到了项
    tmp = []
    for kkk in littlepngs:
        tmp.append(utils.pipei('screencap.png', kkk, 0.8))
        tmp.append(utils.pipei_after_erzhihua('screencap.png', kkk, 0.8))

    for i in tmp:
        # 找到第一个不是None的,作为我们输出坐标
        if i != None:
            point = (i[0] + i[2]) / 2, (i[1] + i[3]) / 2

            a = os.system(
                'adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))
    import time
    time.sleep(sleeptime)
click_close_button()