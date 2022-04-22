
#=全民农家乐游戏!!!!!!!!!!!
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

    print("下面开始点击红包")
    import os
    #========================上来获取图片

    flag=1
    while flag==1:
        os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
        # 把模拟器里面的文件或文件夹传到电脑上
        os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.
        aaa=utils.pipei('screencap.png','hongbao.png',0.8)#==========这里面有一个飞着的红包.是干扰项.所以我们要限制aaa的位置.
        if aaa :
            point=(aaa[0]+aaa[2])/2,(aaa[1]+aaa[3])/2
            if 960<point[0]<1030 and 1200<point[1]<1300:#必须点到那个死红包我们才算.
                print(f"点击坐标{point}")

                a=os.system('adb shell input tap '+str(int(point[0]))+' '+str(int(point[1])))#点击指令
                flag=0
        import time
        time.sleep(sleeptime)#每2秒尝试一次





    #====================下面同理开始点击 开这个图片

    import time

    print("下面开始点击领取红包,#也是每2秒尝试一次")

    import time


    flag=1
    while flag==1:
        import os
        #========================上来获取图片
        os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
        # 把模拟器里面的文件或文件夹传到电脑上
        os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.
        aaa=utils.pipei('screencap.png','lingquhongbao.png',0.8)
        if aaa:
            point=(aaa[0]+aaa[2])/2,(aaa[1]+aaa[3])/2-450
            flag = 0
            print(f"点击坐标{point}")

            a=os.system('adb shell input tap '+str(int(point[0]))+' '+str(int(point[1])))#点击指令
        import time
        time.sleep(sleeptime)#每2秒尝试一次



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

        import utils#因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.
        aaa=utils.pipei_after_erzhihua('screencap.png','close_button2.png',0.8)
        bbb=utils.pipei_after_erzhihua('screencap.png','chazi3.png',0.8)

        #============有时候叉子需要点2次.
        if aaa:
            point=(aaa[0]+aaa[2])/2,(aaa[1]+aaa[3])/2

            print(f"点击坐标{point}")
            a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令





        elif bbb:
            point=(bbb[0]+bbb[2])/2,(bbb[1]+bbb[3])/2

            print(f"点击坐标{point}")
            a = os.system('adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))  # 点击指令
            import time






        time.sleep(sleeptime)#每2秒尝试一次
        #=============check一下确实没有叉子了.再flag=0
        if aaa or bbb:#如果点击了一次,那么再查一次,确实没有了再退出循环.  =======这个地方逻辑挺复杂, 游戏就是这么设计的, 有时候叉子不止点一次!!!!!!!!!!!!!!!!!!!!挺牛逼的这么写.
            import os
            #========================上来获取图片
            os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
            # 把模拟器里面的文件或文件夹传到电脑上
            os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.

            import utils#因为叉子图片是黑白色基本,所以二值化可以提升准确率, 其他的不是黑白所以不要用.
            aaa=utils.pipei_after_erzhihua('screencap.png','close_button2.png',0.8)
            bbb=utils.pipei_after_erzhihua('screencap.png','chazi3.png',0.8)
            if not aaa and not bbb:
                flag=0
        time.sleep(sleeptime)  # 每2秒尝试一次














    #===============点击恭喜获得红包

    print("开始点击恭喜获得红包")
    import os
    #========================上来获取图片
    os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    # 把模拟器里面的文件或文件夹传到电脑上
    os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.

    import utils
    aaa=utils.pipei('screencap.png','gongxihuodehongbao.png',0.8)
    if aaa:#===============这里面我们找静态不变的,然后后面修正一个720像素即可.
        point=(aaa[0]+aaa[2])/2,(aaa[1]+aaa[3])/2+720
    print(f"点击坐标{point}")
    a=os.system('adb shell input tap '+str(int(point[0]))+' '+str(int(point[1])))#点击指令
    import time
    time.sleep(sleeptime)




    print("等待下次循环!!!!!!!!!!!!!!!")



while 1:#=============无限玩下去,测bug!!!!!!!!!!!!!
    play()





