# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris

from compress import Compression

# load data set
iris = load_iris()
data = iris.data
labels = iris.target

# first we create the Class
cp = Compression(data, labels)
# than use it to fit the model
cp.fit()

# k defalut is 0
data_new = cp.compress(k=0)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))

data_new = cp.compress(k=1)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))

data_new = cp.compress(k=2)
length, length_new = len(data), len(data_new)
print("old : new = {} : {}".format(length, length_new))


"""result
old : new = 150 : 129  # k = 0
old : new = 150 : 66  # k = 1
old : new = 150 : 20  # k = 2
"""
