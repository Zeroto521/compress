# -*- coding: utf-8 -*-

import pandas as pd

from compress import compress


df = pd.read_csv('data/iris.csv')
labels = df.values[:, -1]
data = df.values[:, :-1]

data_new = compress(data, labels)
length, length_new = len(data), len(data_new)

print("Data size")
print("old : new = {} : {}".format(length, length_new))
