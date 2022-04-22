import os
#========================上来获取图片
os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
# 把模拟器里面的文件或文件夹传到电脑上
os.system('adb pull /sdcard/screencap.png screencap.png')#这时手机的屏幕就保存到了项目的根目录下.








