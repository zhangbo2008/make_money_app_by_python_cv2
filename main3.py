import time
#=换个游戏.这个叫.yeyedexiaonongyuan.#还是这个游戏,这次我们换一个玩法. main2的玩法每天有次数限制.
# 下面这个玩法,点击小狗上面的红包.然后看完视频,点开心收下. 这回红包的触发难度很大, 是一个动图.

#=========解释一下为什么不 写一个点击跳过的.因为有一些广告特别坑,虽然写一个跳过,但是你一点他就开始说跳过就没法拿红包了.骗人的跳过.所以最稳的方法还是等他一直走完.
import time
# time.sleep(50*60)


sleeptime=1

def play():
    #项目说明:
    # 使用的手机是荣耀v40.
    #

    import utils
    # aaa=utils.pipei('1.png','2.png',1)#第三个是阈值,大于这个阈值的话表示搜索失败,不存在template图片.
    # print(aaa) # 返回的坐标表示的是图片的匹配之后的 xmin, ymin, xmax, ymax坐标框.









    import os
    # a=os.system('adb shell ls')
    # print(a)

    # a=os.system('adb shell input swipe 800 300 200 300')#滑动指令输入的2个xy坐标
    # a=os.system('adb shell input tap 800 300 ')#点击指令
    # print(a)





    # #========================上来获取图片
    # os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    # # 把模拟器里面的文件或文件夹传到电脑上
    # os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.




    #找到close_button的坐标:
    #注意cv2无法读取中文 # ===========注意截取的小图一定要跟原图同比例, 放缩后的图不行. 最好方法是用画图软件打开,然后再截屏这样没有放缩的.=========注意每一步的保存图片都记做fordebug.png#====================!!!!!!!!!!!!!!!!!!!!!!!!!!!切记切记!!!!!!!!!!!!!!!!因为这个模式比较傻!!!!!!!!!!




    #=========下面写一个死循环.
    # 第一个需求是找到屏幕红包的地方然后点击他的中心位置.
    # 第二个需求是找到屏幕开的位置然后点他中心位置.
    #然后点×关闭   ==========这3个一直循环即可.

    import cv2
    #===============第一个找红包位置.

    print("下面点击小狗脑袋上的红包,每2秒扫描一次")
    import os
    #========================上来获取图片
    flag=1
    while flag:
        os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')

        os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项
        import utils  # 因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.
        aaa = utils.pipei('screencap.png', 'xiaogouhongbao.png', 0.8)
        bbb = utils.pipei('screencap.png', 'xiaogouhongbao2.png', 0.8)
        ccc = utils.pipei('screencap.png', 'xiaogouhongbao3.png', 0.8)
        if aaa or bbb or ccc:
            tmp=[aaa, bbb,ccc]
            for i in tmp:
                #找到第一个不是None的,作为我们输出坐标
                if i!=None:
                    point = (i[0] + i[2]) / 2, (i[1] + i[3]) / 2
                    if 830<point[1]<930:
                        a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
                        flag=0
        import time
        time.sleep(sleeptime)


    print("下面我们点击打开看看")#直接写死即可.

    a = os.system('adb shell input tap ' + str(int(566)) + ' ' + str(int(1350)))  # 点击指令

    #
    #
    # #====================下面同理开始点击 开这个图片
    #
    # import time
    #
    # print("下面开始点击领取红包,#也是每2秒尝试一次")
    #
    # import time
    #
    #
    # flag=1
    # while flag==1:
    #     import os
    #     #========================上来获取图片
    #     os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    #     # 把模拟器里面的文件或文件夹传到电脑上
    #     os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.
    #     aaa=utils.pipei('screencap.png','lingquhongbao.png',0.8)
    #     if aaa:
    #         point=(aaa[0]+aaa[2])/2,(aaa[1]+aaa[3])/2-450
    #         flag = 0
    #         print(f"点击坐标{point}")
    #
    #         a=os.system('adb shell input tap '+str(int(point[0]))+' '+str(int(point[1])))#点击指令
    #     import time
    #     time.sleep(1)#每2秒尝试一次
    #
    #
    #
    #==========下面最难的就是按这个叉子!!!!!!!!!!
    #===========先这么用. 可以从阈值和图片预处理继续做优化.1

    import time
    time.sleep(20)

    flag=1
    while flag==1:
        print("下面开始尝试点击叉子.")

        import os
        #========================上来获取图片
        os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
        # 把模拟器里面的文件或文件夹传到电脑上
        os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.

        import utils#因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.#==========如果背景色是纯色的话,不二值化比较好.
        aaa=utils.pipei_after_erzhihua('screencap.png','close_button2.png',0.8)
        aaa2=utils.pipei('screencap.png','close_button2.png',0.8)
        bbb=utils.pipei_after_erzhihua('screencap.png','chazi3.png',0.8)
        bbb2=utils.pipei('screencap.png','chazi3.png',0.8)

        #============有时候叉子需要点2次.
        tmp=[aaa,aaa2,bbb,bbb2]
        for  kkk in tmp:
            if kkk:
                point = (kkk[0] + kkk[2]) / 2, (kkk[1] + kkk[3]) / 2
                print(f"点击坐标{point}")
                a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令






        time.sleep(sleeptime)#每2秒尝试一次
        time.sleep(sleeptime)#每2秒尝试一次#========一定要sleep足够时间,不然总是继续截屏那个旧图片!!!!!!!!!!!!
        #=============check一下确实没有叉子了.再flag=0
        if tmp!=[None]*4:#如果点击了一次,那么再查一次,确实没有了再退出循环.  =======这个地方逻辑挺复杂, 游戏就是这么设计的, 有时候叉子不止点一次!!!!!!!!!!!!!!!!!!!!挺牛逼的这么写.
            print("进入叉子结束循环的判断")
            import os
            #========================上来获取图片
            os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
            # 把模拟器里面的文件或文件夹传到电脑上
            os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.

            import utils#因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.
            aaa = utils.pipei_after_erzhihua('screencap.png', 'close_button2.png', 0.8)
            aaa2 = utils.pipei('screencap.png', 'close_button2.png', 0.8)
            bbb = utils.pipei_after_erzhihua('screencap.png', 'chazi3.png', 0.8)
            bbb2 = utils.pipei('screencap.png', 'chazi3.png', 0.8)
            tmp = [aaa, aaa2, bbb, bbb2]
            if tmp==[None]*4:
                print("已经没有叉子了,结束循环")
                flag=0
        time.sleep(sleeptime)  # 每2秒尝试一次
        time.sleep(sleeptime)  # 每2秒尝试一次

    time.sleep(4)  # 每2秒尝试一次





    #=================在这个之前有时候还会给你蹦一个广告.草了
    #=========看看是否出现bugclose这个.出现了关了它!!!!!!!!!如果找不到就直接跳过这层逻辑判断.
    print("进行bugclose的匹配")
    import os
    # ========================上来获取图片
    os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    # 把模拟器里面的文件或文件夹传到电脑上
    os.system('adb pull /sdcard/screencap.png screencap.png')  # 这时手机的屏幕就保存到了项目的根目录下.

    import utils  # 因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.
    aaa = utils.pipei_after_erzhihua('screencap.png', 'bugclose.png', 0.8)
    bbb = utils.pipei('screencap.png', 'bugclose.png', 0.8)

    # ============有时候叉子需要点2次.
    if aaa:
        point = (aaa[0] + aaa[2]) / 2, (aaa[1] + aaa[3]) / 2

        print(f"点击坐标{point}")
        a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
    elif bbb:
        point = (bbb[0] + bbb[2]) / 2, (bbb[1] + bbb[3]) / 2

        print(f"点击坐标{point}")
        a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
        import time
    time.sleep(sleeptime)  # 每2秒尝试一次









    print("下面我们点击开心收下")#直接写死即可.#========这游戏刷这个页面超级慢,多等一会儿.

    a = os.system('adb shell input tap ' + str(int(526)) + ' ' + str(int(1672)))  # 点击指令
    time.sleep(sleeptime)  # 每2秒尝试一次#慢一点,页面刷的有时候慢.
    time.sleep(sleeptime)  # 每2秒尝试一次#慢一点,页面刷的有时候慢.


#=======开心手下之后,还有一波京东广告的gank,关闭它!!!!!!!!

#=================在这个之前有时候还会给你蹦一个广告.草了
    #=========看看是否出现bugclose这个.出现了关了它!!!!!!!!!如果找不到就直接跳过这层逻辑判断.
    print("进行bugclose的匹配")
    import os
    # ========================上来获取图片
    os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    # 把模拟器里面的文件或文件夹传到电脑上
    os.system('adb pull /sdcard/screencap.png screencap.png')  # 这时手机的屏幕就保存到了项目的根目录下.

    import utils  # 因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.
    aaa = utils.pipei_after_erzhihua('screencap.png', 'bugclose.png', 0.8)
    bbb = utils.pipei('screencap.png', 'bugclose.png', 0.8)

    # ============有时候叉子需要点2次.
    if aaa:
        point = (aaa[0] + aaa[2]) / 2, (aaa[1] + aaa[3]) / 2

        print(f"点击坐标{point}")
        a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
    elif bbb:
        point = (bbb[0] + bbb[2]) / 2, (bbb[1] + bbb[3]) / 2

        print(f"点击坐标{point}")
        a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
        import time
    time.sleep(sleeptime)  # 每2秒尝试一次
while 1:#=============无限玩下去,测bug!!!!!!!!!!!!!
    play()





