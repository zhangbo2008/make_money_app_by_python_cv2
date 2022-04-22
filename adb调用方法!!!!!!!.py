import os
#===========调用系统方法的争取方法!!!!!!!!!=========这个popen可以获取打印信息!!!!!!
#比system厉害. findstr就是grep命令在win10里面的变化.

#===========重要例子. 获取当前应用的包名~!!!!!!!!!!!!!
a=os.popen('adb shell dumpsys window |findstr  mCurrent')
a=a.read()
print(a)
# a=os.system('adb shall am force-stop com.jm.video')
# print(a)adb shell am force-stop  cn.com.conversant.swiftsync.android
# com.nuohu.dwkhly/com.auto98.gameshell.activity.AppActivity

# a=os.popen('adb shell am force-stop  com.nuohu.dwkhly')# 关闭
a=os.popen('adb shell am start   -W -n  com.auto98.gameshell/com.auto98.gameshell.activity.AppActivity')