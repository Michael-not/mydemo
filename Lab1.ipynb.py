import cv2
import numpy as np
import matplotlib.pyplot as plt
#1 читаем черно белое и разноцветное изображение
img_bw = cv2.imread("1_8.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("rgb.png")

#2 отоброжаем разноцветное изображение
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.show();
#2  отоброжаем чернобелое изображение
plt.figure(figsize=(10,10))
plt.imshow(img_bw,cmap = 'gray')
plt.show();

#3 Превращаем разноцветное изображение из BGR в RGB и отображаем
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show();
#3 Превращаем разноцветное изображение из BGR в HSV и отображаем
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img_rgb)
plt.show();

#4 Отдельно отображаем разноцветные каналы для моделей RGB
b, g, r = cv2.split(img_rgb)
plt.subplot(131);
R = np.zeros(img_rgb.shape, dtype='uint8')
R[:, :, 0] = r
plt.imshow(R)

plt.subplot(132);
G = np.zeros(img_rgb.shape, dtype='uint8')
G[:, :, 1] = g
plt.imshow(G)

plt.subplot(133);
B = np.zeros(img_rgb.shape, dtype='uint8')
B[:, :, 2] = b
plt.imshow(B)

plt.show()
#4 Отдельно отображаем разноцветные каналы для моделей HSV
b, g, r = cv2.split(img_hsv)
plt.subplot(131);
R = np.zeros(img_hsv.shape, dtype='uint8')
R[:, :, 0] = r
plt.imshow(R)

plt.subplot(132);
G = np.zeros(img_hsv.shape, dtype='uint8')
G[:, :, 1] = g
plt.imshow(G)

plt.subplot(133);
B = np.zeros(img_hsv.shape, dtype='uint8')
B[:, :, 2] = b
plt.imshow(B)

plt.show()
#5 Скопировать область интереса черно белого изображения(и отобразили)
img_crop_bw = img_bw[0:int(img_bw.shape[0]/2), 0:int(img_bw.shape[0]/2)]
print(img_crop_bw)
plt.imshow(img_crop_bw, cmap='gray')
plt.show()
#Сохраняем область интереса
cv2.imwrite("obl_interest.png",img_crop_bw)
