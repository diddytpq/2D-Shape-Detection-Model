import tensorflow.keras as keras
import cv2
#import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

train_datagen=keras.preprocessing.image.ImageDataGenerator(rescale=1./255,
                                                        rotation_range=45,
                                                        width_shift_range=None,
                                                        height_shift_range=None,
                                                        zoom_range=0.3,
                                                        fill_mode='nearest')

test_datagen=keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

for i in range(1,21):
    if i<10:
        img=cv2.imread('dataset/train_gray/1_rectangle/rectangle_0{}.png'.format(i),0) 
    else:
        img=cv2.imread('dataset/train_gray/1_rectangle/rectangle_{}.png'.format(i),0)
        
    img_data=img.reshape(1,100,100,1)
    
    cnt=0
    
    for batch in train_datagen.flow(img_data,batch_size=1,
                               save_to_dir='dataset/train_gen/1_rectangle',
                               save_prefix='rectangle',
                               save_format='png'):
        cnt+=1
        print(cnt)
        if cnt>29:
            print('done')
            breaks