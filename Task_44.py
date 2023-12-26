"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


# C get_dummies
one_hot_data_gd = pd.get_dummies(data['whoAmI'])
data_one_hot_gd = pd.concat([data, one_hot_data_gd], axis=1)
print(data_one_hot_gd.head(10))

# Без get_dummies
one_hot_data = pd.DataFrame({'human': data['whoAmI'] == 'human', 'robot': data['whoAmI'] == 'robot'}).astype(int)
data_one_hot = pd.concat([data, one_hot_data], axis=1)
print(data_one_hot.head(10))

