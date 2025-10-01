import cv2

img = cv2.imread(r"E:\GitGO\PYTHON\GitPyLearningREPO\OpenCV\CVimgs\street.jpg")
print("Original Shape:",img.shape)
width, height = 600,500

imgResize = cv2.resize(img,(width,height))
print("Resized Shape:", imgResize.shape)
cv2.imshow("ResizedImg" , imgResize)
cv2.waitKey(0)