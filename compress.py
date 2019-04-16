# -*- coding: utf-8 -*-

import numpy as np


def _is_equal(a, b):
    """Compare two values is equal or not

    Returns:
        bool
    """

    flag = False
    if a == b:
        flag = True
    return flag


def _neighbors(index, length):
    """Get neighbors from a array's index

    Arguments:
        index {int} -- index from a array
        length {int} -- array's length

    Returns:
        list -- the index list
    """

    if index == 0:
        neighbor = [index + 1]
    elif 0 < index < length-1:
        neighbor = [index - 1, index + 1]
    elif index == length-1:
        neighbor = [index - 1]

    return neighbor


def _check_unbpoint(index, labels):
    """Judge value is unblanceed point

    Arguments:
        index {int} -- the judged index of the value
        labels {np.ndarray, list} -- the class for data set

    Returns:
        int -- 0/1
    """

    index = index[0]
    value = labels[index]
    neighbors = _neighbors(index, len(labels))

    ngb_values = [labels[i] for i in neighbors]
    bool_list = [not _is_equal(value, ngb_value) for ngb_value in ngb_values]

    flag = 0
    if any(bool_list):
        flag = 1

    return flag


def _deal_with_column(column, labels):
    """Judge one column (attribute) unblance point

    Arguments:
        column {np.ndarray} -- one column for a date set
        labels {np.ndarray, list} -- the class for data set

    Returns:
        np.ndarray
    """

    index = np.arange(len(column))
    array = np.stack([index, column, labels], axis=1)  # combine to one array
    array = array[np.argsort(array[:, 1])]  # sort by attribute
    index = index.reshape((len(column), -1))
    array[:, 1] = np.apply_along_axis(
        _check_unbpoint, 1, index, labels=array[:, -1])
    array = array[np.argsort(array[:, 0])]  # sort to old place

    return array[:, 1]


def compress(data, labels, k=0):
    """The extreme value is obtained at the interval endpoint for convex function,and therefore the endpoint degree of a sample is measured by making the unstable cuts of all attributes according to the basic property.

    Arguments:
        data {np.ndarray} -- data set
        labels {np.ndarray, list} -- the class for data set

    Keyword Arguments:
        k {int} -- the threshold value to cut data (default: {0})

    Returns:
        np.ndarray
    """

    I = np.apply_along_axis(_deal_with_column, 0, data, labels=labels)
    K = I.sum(axis=1)
    return data[K > k]
