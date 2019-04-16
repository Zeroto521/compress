# -*- coding: utf-8 -*-

import pandas as pd

from compress import compress


df = pd.read_csv('data/iris.csv')
labels = df.values[:, -1]
data = df.values[:, :-1]

data_new = compress(data, labels, k=0)  # k defalut is 0
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))

data_new = compress(data, labels, k=1)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))

data_new = compress(data, labels, k=2)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))


"""result
old : new = 150 : 126
old : new = 150 : 65
old : new = 150 : 20
"""
