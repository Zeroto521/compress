# -*- coding: utf-8 -*-
"""
Compress
=====
The extreme value is obtained at the interval endpoint for convex function,
and therefore the endpoint degree of a sample is measured by making
the unstable cuts of all attributes according to the basic property.

Example
----------------------------
    >>> from compress import Compression
    >>> cp = Compression(data, labels)  # Guess you have `data` which the shape is `(n, m)` and one column `labels` which the shape is `(n, 1)`.
    >>> cp.fit()  # Then use `fit()` function to fit model with data
    >>> data_new = compress(data, labels, k=0) # Then let use the `compress` to compress the data. `k` is the threshold to compress data
    >>> data_new  # just show it

Copyright Zeroto521
----------------------------
"""

import numpy as np


__version__ = '0.1.1'
__license__ = 'MIT'
__short_description__ = 'Compress data help for big data & unbalanced data classification.'


class Compression():

    def __init__(self, data, labels):
        """Compress data help for big data & unbalanced data classification.

        Compress
        =====
        The extreme value is obtained at the interval endpoint for convex function,
        and therefore the endpoint degree of a sample is measured by making
        the unstable cuts of all attributes according to the basic property.

        Example
        ----------------------------
            >>> from compress import Compression
            >>> cp = Compression(data, labels)  # Guess you have `data` which the shape is `(n, m)` and one column `labels` which the shape is `(n, 1)`.
            >>> cp.fit()  # Then use `fit()` function to fit model with data
            >>> data_new = compress(data, labels, k=0) # Then let use the `compress` to compress the data. `k` is the threshold to compress data
            >>> data_new  # just show it

        Arguments
        ----------------------------
            data {np.ndarray} -- data set
            labels {np.ndarray, list} -- the class for data set
        """
        self.data = data
        self.labels = labels

    @property
    def data_amount(self):
        """Calculate the amount of data

        Returns:
            int
        """
        return len(self.labels)

    def _neighbors(self, index):
        """Get neighbors from a array's index

        Arguments:
            index {int} -- index from a array

        Returns:
            list -- the index list
        """

        if index == 0:
            neighbor = [index + 1]
        elif 0 < index < self.data_amount-1:
            neighbor = [index - 1, index + 1]
        elif index == self.data_amount-1:
            neighbor = [index - 1]

        return neighbor

    def _check_unbpoint(self, index, labels):
        """Judge value is unblanceed point

        Arguments:
            index {int} -- the judged index of the value
            labels {np.ndarray, list} -- the class for data set

        Returns:
            int -- 0/1
        """

        index = index[0]
        value = labels[index]
        neighbors = self._neighbors(index)

        ngb_values = [labels[i] for i in neighbors]
        bool_list = [not (value == ngb_value) for ngb_value in ngb_values]

        flag = 1 if any(bool_list) else 0
        return flag

    def _deal_with_column(self, column):
        """Judge one column (attribute) unblance point

        Arguments:
            column {np.ndarray} -- one column for a date set
            labels {np.ndarray, list} -- the class for data set

        Returns:
            np.ndarray
        """

        index = np.arange(len(column))
        # combine to one array
        array = np.stack([index, column, self.labels], axis=1)
        array = array[np.argsort(array[:, 1])]  # sort by attribute
        index = index.reshape(self.data_amount, -1)

        array[:, 1] = np.apply_along_axis(
            self._check_unbpoint, 1, index, labels=array[:, -1])
        array = array[np.argsort(array[:, 0])]  # sort to old place

        return array[:, 1]

    def fit(self):
        """Fit the model using `data` and `labels`
        """

        self.I = np.apply_along_axis(self._deal_with_column, 0, self.data)
        self.K = self.I.sum(axis=1)

    def compress(self, k=0):
        """main function

        Keyword Arguments:
            k {int} -- the threshold value to cut data (default: {0})

        Returns:
            np.ndarray
        """

        return self.data[self.K > k]
