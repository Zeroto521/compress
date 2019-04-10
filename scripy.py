# -*- coding: utf-8 -*-

import os

import numpy as np
import pandas as pd


def getNeighbor(index, length):
    neighbor = []
    if index == 0:
        neighbor.append(index + 1)
    elif 0 < index < length-1:
        neighbor.extend([index-1, index+1])
    elif index == length-1:
        neighbor.append(index-1)

    return neighbor


def is_equal(a, b):
    flag = False
    if a == b:
        flag = True
    return flag


def is_point(index, labels):
    neighbor_index = getNeighbor(index, len(labels))
    value = labels[index]
    flag = 0
    if len(neighbor_index) == 1:
        if not is_equal(value, labels[neighbor_index[0]]):
            flag = 1
    elif len(neighbor_index) == 2:
        neighbor_labels = [labels[i] for i in neighbor_index]
        bool_list = [not is_equal(value, label) for label in neighbor_labels]
        if any(bool_list):
            flag = 1

    return flag


def clean_attr(df_attr, attr, label_name, local='local'):
    labels = df_attr[label_name].values
    points = []
    for index, (i, local_index) in enumerate(zip(df_attr[attr], df_attr[local])):
        flag = is_point(index, labels)
        points.append((local_index, flag))

    points.sort(key=lambda x: x[0])
    points = [i[1] for i in points]

    return points


def data_clean(df, attr_names, label_name, local='local'):
    I = []
    for attr in attr_names:
        df_attr = df.loc[:, [local, attr, label_name]]
        df_attr.sort_values(attr, inplace=True)
        points = clean_attr(df_attr, attr, label_name)
        I.append(points)

    I = np.asarray(I).T

    return I


if __name__ == "__main__":
    path = 'data/iris.csv'
    k = 0

    df = pd.read_csv(path)
    attr_names = df.columns[: -1]
    label_name = df.columns[-1]
    local = 'local'
    df[local] = df.index
    I = data_clean(df, attr_names, label_name)
    K = I.sum(axis=1)

    df_res = df[K > k]
    path, filename = os.path.split(path)
    filename = (
        os.path.splitext(filename)[0] + '_clean' + os.path.splitext(filename)[1])
    del df_res[local]
    path = os.path.join(path, filename)
    df_res.to_csv(path, index=False)

    print('Done')
