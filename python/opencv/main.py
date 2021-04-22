import cv2

img_path = "file.jpg"

img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 将彩色图片转换成为灰度图

# 使用高斯滤波函数对灰度图进行模糊化操作，参数ksize表示高斯核的大小，sigmaX和sigmaY分别表示高斯核在 X 和 Y 方向上的标准差（设为0表示根据ksize自行计算）。可以通过调整ksize来呈现不同的模糊效果。
blur = cv2.GaussianBlur(gray, ksize=(101, 101), sigmaX=0, sigmaY=0)

# 一幅素描作品诞生啦
res = cv2.divide(gray, blur, scale=255)

# 保存素描作品
cv2.imwrite('new.jpg', res)
