import numpy as np
import cv2
import tensorflow.keras as keras

def categorical(img):
    img=cv2.resize(img,(100,100))
    img=img.flatten()/255
    img=img.reshape(1,100,100,1)
    x=model.predict(img)
    predict_arg=np.argmax(x)
    score=x[:,predict_arg]*100

    if predict_arg==0:
        return str('circle')+str(score),0
    elif predict_arg==1:
        return str('rectangle')+str(score),1
    elif predict_arg==2:
        return str('triangle')+str(score),2




model=keras.models.load_model('model/model_v1.2.h5')

img=cv2.imread('test_02.png')
img=cv2.resize(img,None,fx=0.7,fy=0.7)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(3,3),0)
#img_canny=cv2.Canny(img_blur,10,50)

ret,img_th=cv2.threshold(img_blur,127,255,cv2.THRESH_BINARY_INV)  #이미지 이진화
contours, hierachy=cv2.findContours(img_th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 

rects=[cv2.boundingRect(i) for i in contours]

for (x,y,w,h) in rects:
    detect_img=img_gray[y-10:y+h+10,x-10:x+w+10]
    
    shape,clr=categorical(detect_img)
    cv2.putText(img,shape,(x,y-25),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)
    if clr==0:color=(255,0,0)
    elif clr==1:color=(0,255,0)
    elif clr==2:color=(0,0,255)
    cv2.rectangle(img,(x-10,y-10),(x+w+10,y+h+10),color,2)


cv2.imshow('0',img)
#cv2.imshow('1',img_blur)
#cv2.imshow('2',img_canny)
#cv2.imshow('3',img_gray)
#cv2.imshow('4',img_th)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()