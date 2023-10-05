import cv2
import numpy as np
from random import randrange

def createImgWithPointRand(h,w):
    img = np.ones((heigthImg,widthImg),np.float32)
    #randrange(x) return une valeur aléatoire entre 0 et x
    randPointY,RandPointX = randrange(heigthImg),randrange(widthImg)
    img[randPointY,RandPointX] = 0 
    return img


def findBlackPoint(img):
    for y in range(heigthImg):
        for x in range (widthImg):
            if(img[y,x]==0):
                return (y,x)
                break

heigthImg=200
widthImg =400
pas = 10

img = createImgWithPointRand(heigthImg,widthImg)

q = 'a'
(yp,xp) = findBlackPoint(img)

#kernel = np.ones((10,10), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (19,19))

print(kernel)

while(True):
    print('apres ',yp,' === ',xp, 'q =',ord('q'))
    
    
    if(52 == q and xp-pas>=0):
        img[yp,xp] = 1
        xp=xp-pas
        img[yp,xp] = 0
        print('decale1')
    if(54 == q and xp+pas<=widthImg):
        img[yp,xp] = 1
        xp=xp+pas
        img[yp,xp] = 0
        print('decale2')
    if(56 == q and yp-pas>=0):
        img[yp,xp] = 1
        yp=yp-pas
        img[yp,xp] = 0
        print('decale3')
    if(50 == q and yp+pas<=heigthImg):
        img[yp,xp] = 1
        yp=yp+pas
        img[yp,xp] = 0
        print('decale4')

    imgRes = img.copy()
    #imgRes[yp-6:yp+6,xp-6:xp+6] = 0

    imgRes = cv2.erode(img, kernel, iterations=1)
    cv2.imshow('image gray',imgRes)
    q = cv2.waitKey(0) & 0xFF
    print(q)
    if(48 == q):
        break
    
cv2.destroyAllWindows()
