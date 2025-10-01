import cv2
img = cv2.imread("E:\GitGO\PYTHON\GitPyLearningREPO\OpenCV\CVimgs\E106676R.jpg",0)
width,height = 400,400
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)
cv2.imshow("GrayImg",imgResize)
cv2.waitKey(0)