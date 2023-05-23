import cv2
#pip install opencv-python
imagepath = input("Enter Image name with extension: ")
#give the name of the file
image = cv2.imread(imagepath)

grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("sketch.png",sketch)
