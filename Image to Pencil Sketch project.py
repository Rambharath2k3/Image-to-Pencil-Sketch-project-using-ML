#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import cv2

#Loading an image
image=cv2.imread(r'C:\Users\rambh\OneDrive\Pictures\Saved Pictures\PRABHAS.jpg')

#Convering color to Grayscale image
img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Inverting the gray image
inverted_gray_image=255-img_gray

#Now blur the image using the guassian blur
blurred_img=cv2.GaussianBlur(inverted_gray_image,(21,21),0)
    
#Now invering the blurred image
inverted_blurred_image=255-blurred_img

#Now let's create the pencil sketch
pencil_sketch_img=cv2.divide(img_gray,inverted_blurred_image,scale=256.0)

plt.figure(figsize=(5,5))
plt.imshow(pencil_sketch_img,cmap='gray')
plt.axis('off')
plt.show()


# In[ ]:




