# 一些cv2 实用技术!!!!!!!!!!
#1.https://mp.weixin.qq.com/s?__biz=MzU4OTYzNjE2OQ==&mid=2247485356&idx=1&sn=38d72793bf6b88499665a9a41d348472&chksm=fdcb308acabcb99c528b677d811cf98f9a3ae467529be84054da9a121408c1b23e1b7dd4caeb&scene=21#wechat_redirect




#========1.模板匹配

#最快速的匹配.

#函数传入2个图片,返回all中匹配little的结果矩阵.
def pipei(all,little,threshold):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread(all, 0)
    img2 = img.copy()
    template = cv2.imread(little, 0)

    # img=img.astype('float32')
    # template=template.astype('float32')
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF_NORMED']
    for meth in methods:
        img = img2.copy()
        # eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
        # 模板匹配
        res = cv2.matchTemplate(img, template, method)

        # loc = np.where(res >= threshold)
        # print(loc, "loc")

        # # Draw a rectangle around the matched region.#=========画出黄色区域
        # print("找到多少个",len(list(zip(*loc[::-1]))))
        # for pt in zip(*loc[::-1]):
        #     cv2.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        # cv2.imwrite('fordebug.png',img2)







#http://www.opencv.org.cn/opencvdoc/2.3.2/html/modules/imgproc/doc/object_detection.html?highlight=template#cv2.matchTemplate  对应的官方文档.
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # min_val=abs(min_val/(w*h))
        if max_val>=threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # print("匹配成功,匹配值是",max_val,top_left + bottom_right)
            if 0:#这块debug用,正是时候关闭即可.
                cv2.rectangle(img2, top_left, bottom_right, (0, 255, 255), 2)
                cv2.imwrite('fordebug.png', img2)
            return top_left + bottom_right
        else:
            # print("匹配失败,匹配值是",max_val)
            return None






#==============明显的可以避免了背景色的干扰!!!!!!!!!!!!!!!!
#函数传入2个图片,返回all中匹配little的结果矩阵.
def pipei_after_erzhihua(all,little,threshold):
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread(all, 0)
    img2 = img.copy()
    img2=cv2.threshold(img2, 200, 255, cv2.THRESH_BINARY )[1]# 200 ,255表示大于200的都变成255. 小于200的都变成黑色也就是0.
    template = cv2.imread(little, 0)
    template=cv2.threshold(template, 200, 255, cv2.THRESH_BINARY )[1]
    # cv2.imwrite('bug222222.png',img2)
    # cv2.imwrite('bug1111111111.png',template)
    # cv2.waitKey()


    # img=img.astype('float32')
    # template=template.astype('float32')
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF_NORMED']
    for meth in methods:
        img = img2.copy()
        # eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
        # 模板匹配
        res = cv2.matchTemplate(img, template, method)

        # loc = np.where(res >= threshold)
        # print(loc, "loc")

        # # Draw a rectangle around the matched region.#=========画出黄色区域
        # print("找到多少个",len(list(zip(*loc[::-1]))))
        # for pt in zip(*loc[::-1]):
        #     cv2.rectangle(img2, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        # cv2.imwrite('fordebug.png',img2)







#http://www.opencv.org.cn/opencvdoc/2.3.2/html/modules/imgproc/doc/object_detection.html?highlight=template#cv2.matchTemplate  对应的官方文档.
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # min_val=abs(min_val/(w*h))
        if max_val>=threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # print("匹配成功,匹配值是",max_val,top_left + bottom_right)
            if 1:#这块debug用,正是时候关闭即可.
                cv2.rectangle(img2, top_left, bottom_right, (0, 255, 255), 2)
                cv2.imwrite('fordebug.png', img2)
            return top_left + bottom_right
        else:
            # print("匹配失败,匹配值是",max_val)
            return None









if 0:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = cv2.imread('image.jpg', 0)
    img2 = img.copy()
    template = cv2.imread('image_head.png', 0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
        # eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
        # 模板匹配
        res = cv2.matchTemplate(img, template, method)
        # 寻找最值
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 使用不同的比较方法，对结果的解释不同

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()







#边缘检测的代码
if 0:
    import cv2
    import numpy as np

    # 读取原图像
    img = cv2.imread('1.png', 0)

    # 显示原图像
    cv2.namedWindow('img', 0)
    cv2.resizeWindow('img', 400, 600)
    cv2.imshow('img', img)

    # 高斯模糊
    img_rgb = cv2.GaussianBlur(img, (5, 5), 0)
    canny_img = cv2.Canny(img_rgb, 1, 10)

    # 显示边缘检测图像
    cv2.namedWindow('canny', 0)
    cv2.resizeWindow('canny', 400, 600)
    cv2.imshow('canny', canny_img)
    cv2.waitKey()

    # 输出边缘检测图像的高和宽
    H, W = canny_img.shape
    print(H, W)






if 0:
    #test
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt

    img = np.array([[1,2,3,4],[1,2,3,4]])
    img=cv2.imwrite('tmp.png',img)
    img=cv2.imread('tmp.png')
    img2 = img.copy()
    template = np.array([[2,3],[2,3]])
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_SQDIFF']
    for meth in methods:
        img = img2.copy()
        # eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
        # 模板匹配
        res = cv2.matchTemplate(img, template, method)
        # http://www.opencv.org.cn/opencvdoc/2.3.2/html/modules/imgproc/doc/object_detection.html?highlight=template#cv2.matchTemplate  对应的官方文档.
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        min_val = abs(min_val / (w * h))
        if min_val <= threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            print("匹配成功,匹配值是", min_val, top_left + bottom_right)

        else:
            print("匹配失败,匹配值是", min_val)
            None