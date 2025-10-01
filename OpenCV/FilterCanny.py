import cv2
img = cv2.imread("E:\GitGO\PYTHON\GitPyLearningREPO\OpenCV\CVimgs\E106676R.jpg")
width,height = 400,400
imgResize = cv2.resize(img,(width,height))
imgCanny = cv2.Canny(imgResize,80,80) #decrease the no. to get more lines
cv2.imshow("Img Canny",imgCanny)
cv2.waitKey(0)