import matplotlib.pyplot as plt
import numpy as np

#1.1 Создаем диапазон функции от 0 до 2 с шагом 0.1
t = np.arange(0.0, 2.0, 0.01)
#1.2 Задачем частоты синусоидам
s1 = np.sin(2 * np.pi * t)
s2 = np.sin(4 * np.pi * t)
s3 = np.sin(6 * np.pi * t)
s4 = np.sin(8 * np.pi * t)
#1.4 Рисуем графики
fig= plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(t, s1, c='r',linewidth=4.0)
ax1.set( title='Сінус1 функція')
ax1.grid()

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(t, s2, c='y',linewidth=4.0)
ax2.set( title='Сінус2 функція')
ax2.grid()

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(t, s3, c='g',linewidth=4.0)
ax3.set( title='Сінус3 функція')
ax3.grid()

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(t, s4, c='b',linewidth=4.0)
ax4.set( title='Сінус4 функція')
ax4.grid()

plt.show()
