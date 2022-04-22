import os
point=550,1669
def aaa(a):
    while 1:
        print(1)
        a = os.system(
                            'adb shell input tap ' + str(int(point[0])) + ' ' + str(int(point[1])))
import time
def bbb(a):
    while 1:
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
                time.sleep(2)  # 每2秒尝试一次
                time.sleep(2)  #






        time.sleep(2)#每2秒尝试一次
        time.sleep(2)#


from multiprocessing import Pool,Process

def f(x):
    return x*x

if __name__ == '__main__':
    p = Process(target=aaa, args=('bob',))
    q = Process(target=bbb, args=('bob',))
    p.start()
    q.start()
    p.join()
    q.join()