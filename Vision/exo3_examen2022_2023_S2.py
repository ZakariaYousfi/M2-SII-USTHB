#sssssssss22222222222222222222222
import cv2
import numpy as np

lo=np.array([95, 80, 50])
hi=np.array([115, 255, 255])
def detect_inrange(image, surface):
    points=[]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image=cv2.blur(image, (5, 5))
    mask=cv2.inRange(image, lo, hi)
    mask=cv2.erode(mask, None, iterations=2)
    mask=cv2.dilate(mask, None, iterations=2)
    elements=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    elements=sorted(elements, key=lambda x:cv2.contourArea(x), reverse=True)
    for element in elements:
        if cv2.contourArea(element)>surface:
            ((x, y), rayon)=cv2.minEnclosingCircle(element)
            points.append(np.array([int(x), int(y)]))
        else:
            break
    return points, mask


def affiche_raquette(img,x,y,w,B,G,R):
    if (x>0 and y>0 and x+w<img.shape[1] and y+5<img.shape[0]):
        img[y:y+6,x:x+w+1] = [B,G,R]

    return img


VideoCap=cv2.VideoCapture(0)
posX = 10
posY = 200
pas = 10
vitesse = 1000 #pixel par second  #+temps de calcul
w = 100
B,G,R = 255,0,255

while(True):
    ret, frame=VideoCap.read()
    cv2.flip(frame,1,frame)
    
    points, mask=detect_inrange(frame, 200)
    if (len(points)>0):
        cv2.circle(frame, (points[0][0], points[0][1]), 10, (0, 0, 255), 2)
        
        if points[0][0] > posX+w/2 and posX+w+pas < frame.shape[1]: 
            posX += pas
        else : 
            if posX-pas > 0: 
                posX -= pas

    
    frame = affiche_raquette(frame,posX,posY,w,B,G,R)
    cv2.imshow('image', frame)
    #if mask is not None:
       # cv2.imshow('mask', mask)

    if cv2.waitKey(int(pas*1000/vitesse))&0xFF==ord('q'):
        break
VideoCap.release()
cv2.destroyAllWindows()