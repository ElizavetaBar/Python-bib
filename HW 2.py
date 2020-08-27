#!/usr/bin/env python
# coding: utf-8

# #### 1.Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов.
# Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7.
# Будем считать, что каждый столбец - это признак, а строка - наблюдение.
# Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy.
# Результат запишите в массив mean_a, в нем должно быть 2 элемента.

# In[1]:


import numpy as np


# In[6]:


b = ([1, 6], [2, 8], [3, 11], [3, 10], [1, 7])


# In[7]:


a = np.array(b)


# In[8]:


a


# In[15]:


c = np.mean(a[1])


# In[19]:


d = np.mean(a[2])


# In[22]:


e = ([c, d])


# In[25]:


mean_a = np.array(e, dtype = int)
mean_a


# #### 2. Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

# In[ ]:




