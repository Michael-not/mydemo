import numpy as np
#1.1 Задаем размер масива
size = 11
#1.2 Создаем нулевой масив заданого размера
arr= np.zeros([size,size])
#1.3 Выводим созданный масив
print(arr,'\n')
#1.4 Заменяем диагонали с помощью двух циклов
for i in range(size):
    for j in range(size):
        if j == i:
            arr[i][j] = 1
        elif j == (size-1-i):
            arr[i][j] = 1
#1.5 Выводим созданный масив
print(arr)
