# compress

> The extreme value is obtained at the interval endpoint for convex function, and therefore the endpoint degree of a sample is measured by making the unstable cuts of all attributes according to the basic property.

## Prerequisites

`numpy`

## Installation

```bash
>>> git clone https://github.com/Zeroto521/compress.git
>>> cd compress
>>> python setup.py install
```

## Example

```python
>>> from compress import compress
# Guess you have `data` which the shape is `(n, m)` and one column `labels` which the shape is `(n, 1)`.
# Then let use the `compress` to compress the data.
>>> data_new = compress(data, labels, k=0)  # k is the threshold to compress data
>>> data_new
```

> More details for `test.py` and `compress.py`.

## License

MIT License. [@Zeroto521](https://github.com/Zeroto521)

## Reference

-   [WANG Xizhao, XING Sheng, ZHAO Shixin. Unstable Cut-Points Based Sample Selection for Large Data Classification[J]. Pattern Recognition and Artificial Intelligence, 2016, 29 (09): 780-789.](https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ&filename=MSSB201609002)
