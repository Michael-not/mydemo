import numpy as np
import cv2
#2.1 создаем нулевой масив 255х255
size=255
horizontal_gradient1 = np.zeros((size,size))
#2.2 узнаем размеры масива
w = horizontal_gradient1.shape[0]
h = horizontal_gradient1.shape[1]
#2.3 по элементно изменяем яркость каждого пикселя
for i in range(size):
    for j in range(size):
        horizontal_gradient1[i][j] = j+1
#2.4 записываем изображения с помощью OpenCV
cv2.imwrite('horizontal_grad1.jpg', horizontal_gradient1)
#2.5 Аналогично создаем горизонтальный градиент в другой бок

horizontal_gradient2 = np.zeros((size,size))

w = horizontal_gradient2.shape[0]
h = horizontal_gradient2.shape[1]

for i in range(size):
    for j in range(size):
        horizontal_gradient2[i][j] = size-j
        
cv2.imwrite('horizontal_grad2.jpg', horizontal_gradient2)

#2.6 Создаем нулевой масив 255х255
vertical_gradient1 = np.zeros((size,size))
#2.7 узнаем размеры масива
w = vertical_gradient1.shape[0]
h = vertical_gradient1.shape[1]
#2.8 по элементно изменяем яркость каждого пикселя
for i in range(size):
    for j in range(size):
        vertical_gradient1[j][i] = j+1
#2.9 записываем изображения с помощью OpenCV
cv2.imwrite('vertical_grad1.jpg', vertical_gradient1)
#2.10 Аналогично создаем вертикальный градиент в другой бок
vertical_gradient2 = np.zeros((size,size))

w = vertical_gradient2.shape[0]
h = vertical_gradient2.shape[1]

for i in range(size):
    for j in range(size):
        vertical_gradient2[j][i] = 255-j
        
cv2.imwrite('vertical_grad2.jpg', vertical_gradient2)
