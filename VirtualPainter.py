import os
import cv2
import numpy as np
import time
import mediapipe as mp
import HandTrackingModule as htm
from sympy import symbols, Eq, solve
import math
from math import *
from sympy import *

##################
brushThickness=5
eraserThickness=150
#################

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList=[]
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
header=overlayList[0]

drawColor =(255,0,255)

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector =htm.handDetector(detectionCon=0.85)
xp,yp=0,0
imgCanvas = np.zeros((720,1280,3),np.uint8)

while True:
    #1. import image
    success,img =cap.read()
    #img = cv2.flip(img, 1)

    #2. Find Hand landmarks
    img =detector.findHands(img)
    lmList = detector.findPosition(img , draw=False)

    if len(lmList)!=0:
        #print(lmList)

        #tip of index and middle finger
        x1,y1= lmList[8][1:]
        x2,y2=lmList[12][1:]
        x3,y3=lmList[16][1:]



     #3.Check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)
        #4. if selection mode -two fingers are up
        if fingers[1] and fingers[2]:

            print("Selection Mode")
            #checking for the click
            if y1<125:
                if 250<x1<450:
                    header = overlayList[0]
                    drawColor=(255,0,255)
                    #brushThickness=5
                elif 550<x1<700:
                    header =overlayList[1]
                    drawColor = (255, 0, 0)
                    #brushThickness=20
                elif 750 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                    #brushThickness=50

                elif  1050 < x1 < 1250:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
                elif x1<125:
                    header=overlayList[4]
                    brushThickness= 100-int(x1)
               # elif 130<x1<230:



            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
        if fingers[1] and fingers[2] and fingers[3]:
            #########################
            #cv2.circle(img, (x1, y1), 25, (100, 20, 100),1)
            g, f, c = symbols('g,f,c')
            eq1 = Eq((x1 * 2*g + 2*(800-y1)* f + c), (-1*(pow(x1,2)+pow(y1,2))))
            eq2 = Eq((x2 *2* g + 2*(800-y2) * f + c), (-1 * (pow(x2, 2) + pow(y2, 2))))
            eq3 = Eq((x3 *2* g + 2*(800-y3) * f + c), (-1 * (pow(x3, 2) + pow(y3, 2))))

            a=(solve((eq1, eq2, eq3),(g,f,c)))
            g1=a[g]
            f1=a[f]
            c1=a[c]




            #radius= int (math.sqrt(pow(g1,2)+pow(f1,2)+c1))
            radius=x3-x1
            print(radius)
            rx=int((-1*g1))
            ry=int((f1))
            print(rx , x1)
            print(ry,y1)
            cv2.circle(img, (x2, y2), radius, drawColor, 2)
            if fingers[4]:
                cv2.circle(imgCanvas, (x2, y2), radius, drawColor, 2)
            ############################



        #5. if Drawing mode- Index finger is up
        if fingers[1] and fingers[2]==False:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            print("Drawing Mode")
            if xp ==0 and yp ==0:
                xp, yp = x1, y1

            if drawColor == (0,0,0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)


            else:
                cv2.line(img, (xp,yp), (x1,y1) , drawColor , brushThickness)
                cv2.line(imgCanvas, (xp,yp), (x1,y1) , drawColor , brushThickness)

        xp,yp=x1,y1



    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray,50,255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)




    #setting the header image
    img[0:125,0:1280] = header

    cv2.imshow("Image",img)
    cv2.imshow("Canvas",imgCanvas)
    #cv2.imshow("Inverse",imgInv)
    cv2.waitKey(1)









