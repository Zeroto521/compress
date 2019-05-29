# Compress

> The extreme value is obtained at the interval endpoint for convex function, and therefore the endpoint degree of a sample is measured by making the unstable cuts of all attributes according to the basic property.

[![Build Status](https://travis-ci.com/Zeroto521/compress.svg?branch=master)](https://travis-ci.com/Zeroto521/compress) [![codecov](https://codecov.io/gh/Zeroto521/compress/branch/master/graph/badge.svg)](https://codecov.io/gh/Zeroto521/compress)

## Prerequisites

-   `numpy`

> More details for [requirements](requirements.txt) file.

## Installation

```bash
>>> git clone https://github.com/Zeroto521/compress.git
>>> cd compress
>>> python setup.py install
```

## Examples

```python
>>> from compress import Compression
>>> model = Compression(data, labels)  # Guess you have `data` which the shape is `(n, m)` and one column `labels` which the shape is `(n, 1)`.
>>> model.fit()  # Then use `fit()` function to fit model with data
>>> data_new = model.compress(data, labels, k=0)  # Then let use the `compress` to compress the data. `k` is the threshold to compress data
>>> data_new  # just show it
```

> More details for [examples](examples) folder and [compress.py](compress.py) source code.

## License

MIT License. [@Zeroto521](https://github.com/Zeroto521)

## Reference

-   [WANG Xizhao, XING Sheng, ZHAO Shixin. Unstable Cut-Points Based Sample Selection for Large Data Classification[J]. Pattern Recognition and Artificial Intelligence, 2016, 29 (09): 780-789.](https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ&filename=MSSB201609002)
