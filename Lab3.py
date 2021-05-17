#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

#1.1 загружаем изображение
img_half = cv2.imread("C:\\Users\\User\\Desktop\\Slavik\\Lab_3\\lab\\Lab3_half100.png",cv2.IMREAD_GRAYSCALE)
img_chess = cv2.imread("C:\\Users\\User\\Desktop\\Slavik\\Lab_3\\lab\\Lab3_chess100.png",cv2.IMREAD_GRAYSCALE)

#1.2-1.3
plt.figure(figsize=(20,10))
plt.subplot(121)
plt.imshow(img_half, cmap = 'gray');
plt.subplot(122)
hist_half = cv2.calcHist([img_half], [0], None, [256], [0, 256])
plt.plot(hist_half); plt.xlim([0, 255]); plt.grid(); plt.show();
#1.2-1.3
plt.figure(figsize=(20,10))
plt.subplot(121)
plt.imshow(img_chess, cmap = 'gray');
plt.subplot(122)
hist_chess =cv2.calcHist([img_chess], [0], None, [256], [0, 256])
plt.plot(hist_chess); plt.xlim([0, 255]); plt.grid(); plt.show();

#1.4 просторова фильтрация изображения размытием Гауса с размерами 3х3,5x5,9x9,15x15.

half_blur3 = cv2.GaussianBlur(img_half,(3,3),0)
half_blur5 = cv2.GaussianBlur(img_half,(5,5),0)
half_blur9 = cv2.GaussianBlur(img_half,(9,9),0)
half_blur15 = cv2.GaussianBlur(img_half,(15,15),0)

chess_blur3 = cv2.GaussianBlur(img_chess,(3,3),0)
chess_blur5 = cv2.GaussianBlur(img_chess,(5,5),0)
chess_blur9 = cv2.GaussianBlur(img_chess,(9,9),0)
chess_blur15 = cv2.GaussianBlur(img_chess,(15,15),0)
#1.5 Визначити гістограми для всіх отриманих зображень.
half_blur3_hist = cv2.calcHist([half_blur3], [0], None, [256], [0, 256])
half_blur5_hist = cv2.calcHist([half_blur5], [0], None, [256], [0, 256])
half_blur9_hist = cv2.calcHist([half_blur9], [0], None, [256], [0, 256])
half_blur15_hist = cv2.calcHist([half_blur15], [0], None, [256], [0, 256])

chess_blur3_hist = cv2.calcHist([chess_blur3], [0], None, [256], [0, 256])
chess_blur5_hist = cv2.calcHist([chess_blur5], [0], None, [256], [0, 256])
chess_blur9_hist = cv2.calcHist([chess_blur9], [0], None, [256], [0, 256])
chess_blur15_hist = cv2.calcHist([chess_blur15], [0], None, [256], [0, 256])
#1.6.Відобразити отримані після фільтрації зображення та відповідно визначені гістограми за допомогою функції plt.subplot:
plt.figure(figsize=(20,20))
plt.subplot(421)
plt.imshow(half_blur3,cmap = 'gray');plt.title('blur 3x3')
plt.subplot(422)
plt.plot(half_blur3_hist);plt.xlim([0, 255]); plt.grid();
plt.subplot(423)
plt.imshow(half_blur5,cmap = 'gray');plt.title('blur 5x5')
plt.subplot(424)
plt.plot(half_blur5_hist);plt.xlim([0, 255]); plt.grid();
plt.subplot(425)
plt.imshow(half_blur9,cmap = 'gray');plt.title('blur 9x9')
plt.subplot(426)
plt.plot(half_blur9_hist);plt.xlim([0, 255]); plt.grid();
plt.subplot(427)
plt.imshow(half_blur15,cmap = 'gray');plt.title('blur 15x15')
plt.subplot(428)
plt.plot(half_blur15_hist);plt.xlim([0, 255]); plt.grid();plt.show();

plt.figure(figsize=(20,20))
plt.subplot(421)
plt.imshow(chess_blur3,cmap = 'gray');plt.title('blur 3x3')
plt.subplot(422)
plt.plot(chess_blur3_hist);plt.xlim([0, 255]); plt.grid();
plt.subplot(423)
plt.imshow(chess_blur5,cmap = 'gray');plt.title('blur 5x5')
plt.subplot(424)
plt.plot(chess_blur5_hist);plt.xlim([0, 255]); plt.grid();
plt.subplot(425)
plt.imshow(chess_blur9,cmap = 'gray');plt.title('blur 9x9')
plt.subplot(426)
plt.plot(chess_blur9_hist);plt.xlim([0, 255]); plt.grid();
plt.subplot(427)
plt.imshow(chess_blur15,cmap = 'gray');plt.title('blur 15x15')
plt.subplot(428)
plt.plot(chess_blur15_hist);plt.xlim([0, 255]); plt.grid();plt.show();


# In[ ]:




