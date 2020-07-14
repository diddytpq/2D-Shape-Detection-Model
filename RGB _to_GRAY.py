import cv2


for i in range(1,21): #파일 개수
    if i<10:
        img=cv2.imread('dataset/train/2_triangle/triange_0{}.png'.format(i)) #변경전 파일 경로
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('dataset/train_gray/2_triangle/triangle_0{}.png'.format(i),img) #변경후 파일 경로
    else:
        img=cv2.imread('dataset/train/2_triangle/triange_{}.png'.format(i)) #변경전 파일 경로
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('dataset/train_gray/2_triangle/triangle_{}.png'.format(i),img) #변경호 파일 경로
