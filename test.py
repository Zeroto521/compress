# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris

from compress import compress

# load iris data set
iris = load_iris()
data = iris.data
labels = iris.target

# next let compress the data

# k = 0
data_new = compress(data, labels, k=0)  # k defalut is 0
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))

# k = 1
data_new = compress(data, labels, k=1)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))

# k = 1
data_new = compress(data, labels, k=2)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))


"""result
old : new = 150 : 129  # k = 0
old : new = 150 : 66  # k = 1
old : new = 150 : 20  # k = 2
"""
