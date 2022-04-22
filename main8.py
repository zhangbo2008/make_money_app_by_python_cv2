# 动物狂欢乐园         做这个游戏的自动玩ai
# 继续优化这个程序,    做一个重置.玩多少次就重置游戏,防止游戏自己bug死.


import time
#=换个游戏.这个叫.yeyedexiaonongyuan.#还是这个游戏,这次我们换一个玩法. main2的玩法每天有次数限制.
# 下面这个玩法,点击小狗上面的红包.然后看完视频,点开心收下. 这回红包的触发难度很大, 是一个动图.

#=========解释一下为什么不 写一个点击跳过的.因为有一些广告特别坑,虽然写一个跳过,但是你一点他就开始说跳过就没法拿红包了.骗人的跳过.所以最稳的方法还是等他一直走完.
import time
# time.sleep(50*60)

timeUsing_per_action=30
sleeptime=1
import time
while 1:
    #项目说明:
    # 使用的手机是荣耀v40.
    #
    import os
    import utils
    # aaa=utils.pipei('1.png','2.png',1)#第三个是阈值,大于这个阈值的话表示搜索失败,不存在template图片.
    # print(aaa) # 返回的坐标表示的是图片的匹配之后的 xmin, ymin, xmax, ymax坐标框.




    # 图片中是否出现一些小图片, 用的变参
    def whether_exist(littlepngs,xishu=0.8,sleeptime=1):
        if type(littlepngs)!=tuple and  type(littlepngs)!=list:
            tmp=[]
            tmp.append(littlepngs)
            littlepngs=tmp
        print(littlepngs,99999999999999)
        os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')

        os.system('adb pull /sdcard/screencap.png screencap.png')  # 这时手机的屏幕就保存到了项
        tmp = []
        for kkk in littlepngs:
            tmp.append(utils.pipei('screencap.png', kkk, 0.8))
            tmp.append(utils.pipei_after_erzhihua('screencap.png', kkk, 0.8))
        print(tmp)

        return tmp!=[None]*len(tmp)


    # 死循环,在mainpng里面匹配littlepngs,直到匹配成功.匹配陈宫后点击他
    # litttlepngs是一个数组里面有很多个小图.
    def  while_pipeiall_and_click(littlepngs,xishu=0.8,sleeptime=1,):
        import time
        if type(littlepngs)!=tuple and  type(littlepngs)!=list:
            tmp=[]
            tmp.append(littlepngs)
            littlepngs=tmp
        flag = 1
        start=time.time()
        while flag:
            os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')

            os.system('adb pull /sdcard/screencap.png screencap.png')  # 这时手机的屏幕就保存到了项
            tmp=[]
            for kkk in littlepngs:
                tmp.append(utils.pipei('screencap.png', kkk, 0.8))
                tmp.append(utils.pipei_after_erzhihua('screencap.png', kkk, 0.8))


            # tmp2=[]
            # for i in tmp:
            #     if i not in tmp2:
            #         tmp2.append(i)
            # tmp=tmp2
            for i in tmp:
                    # 找到第一个不是None的,作为我们输出坐标
                    print("点击内容tmp",tmp)
                    if i != None:
                        point = (i[0] + i[2]) / 2, (i[1] + i[3]) / 2
                        import time
                        time.sleep(2)# 点击太快会bug
                        a = os.system(
                                'adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
                        flag = 0
                        break
            import time
            end=time.time()
            if end-start>timeUsing_per_action:
                break
            time.sleep(sleeptime)
#关闭随时搞心态的那些弹窗广告
    def click_close_button(littlepngs=['bugclose.png','bugclose2.png','bugclose3.png','bugclose4.png','bugclose5.png','bugclose6.png','close_button6.png'],sleeptime=0.2):
        while 1:
            print("下面关闭bug_close")

            import time
            start=time.time()
            # time.sleep(1)
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
                    print('叉子点击完毕',point)
                    return True
            import time
            time.sleep(sleeptime)
            if time.time() - start > timeUsing_per_action:
                break





#===========上来先答题:
    while_pipeiall_and_click(['shibie.png'])
    click_close_button()
    while_pipeiall_and_click(['shibie2.png'])