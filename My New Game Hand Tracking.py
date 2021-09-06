import  cv2
import mediapipe as mp
import time
import HandTrackingModule as hm
import random as rn

def drawRanPoint(img):

    h, w, c = img.shape
    cx = rn.randint(50,w-50)
    cy = 0
    #cy = rn.randint(50,h-50)
    cv2.circle(img, (cx,cy),20,(34,204,0),cv2.FILLED)
    return img , [cx,cy], h

#def incrd(img,wp):
#    h, w, c = img.shape
#    if (wp[0]+10 >= w):
#        wp[0] = wp[0] - 10
#    if (wp[0]-10 <= 0):
#        wp[0] = wp[0] + 10
#    if (wp[1]+10 >= h):
#        wp[1] =wp[1] - 10
#    if (wp[1]-10 <= 0):
#        wp[1] =wp[1] - 10




pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)

detector = hm.handDetector()
points = 0
gotpoint = True

indexn = 8


while True:

    success, img = cap.read()
    img = cv2.flip(img, flipCode=1)
    img = detector.findHands(img,draw = False)
    lmList = detector.findPosition(img, draw= False)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)




    if gotpoint:
        img , winp, h = drawRanPoint(img)
    cv2.circle(img, (winp[0],winp[1]),20,(34,204,0),cv2.FILLED)



    # if points > 2:
    winp[1] = winp[1] + points+1



    gotpoint = False
    if winp[1] > h:
        gotpoint = True
    if len(lmList) !=0:
        print(lmList[4])
        if (lmList[indexn][1] > winp[0] - 20 and lmList[indexn][1] < winp[0] + 20 and lmList[indexn][2] < winp[1] + 20 and lmList[indexn][2] > winp[1] - 20):
            gotpoint = True
            points = points +1




    cv2.putText(img, "Points: " +str(points), (100, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)