import cv2
import numpy as np

print("Package Imported")

#image capture

img = cv2.imread("Resourses/roma.png")
kernel = np.ones((5,5),np.uint8)

print (img.shape)

imgResize = cv2.resize(img,(300,200))

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
imgCropped = img[100:200,120:180]

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Dialation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)
# cv2.imshow("Resize",imgResize)
# cv2.imshow("Cropped",imgCropped)
# cv2.imshow("Image",img)


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

imgStack = stackImages(0.5, ([imgGray, imgBlur, img], [imgCanny, imgDialation, imgEroded], [imgResize, imgCropped, img ]))

cv2.imshow("ImageStack", imgStack)


cv2.waitKey(5000)

#video capture

#cap = cv2.VideoCapture("Resourses/esp.mp4")

#while True:
#    success, img = cap.read()
#    cv2.imshow("Video",img)
#    if cv2.waitKey(1) & 0xFF ==ord('q'):    #frame delay 1
#        break

#vwebcamcapture

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,1024)
cap.set(10,100)

while True:
    success, imgV = cap.read()
    imgCannyV = cv2.Canny(imgV,100,100)
    cv2.imshow("Video",imgV)
    cv2.imshow("Canny",imgCannyV)
    if cv2.waitKey(1) & 0xFF ==ord('q'):    #frame delay 1
        break