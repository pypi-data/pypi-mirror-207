﻿# ndfind

[![pypi](https://img.shields.io/pypi/v/ndfind.svg)](https://pypi.python.org/pypi/ndfind)
[![python](https://img.shields.io/pypi/pyversions/ndfind.svg)](https://pypi.org/project/ndfind/)
![pytest](https://github.com/axil/ndfind/actions/workflows/python-package.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/pypi/l/ndfind)](https://pypi.org/project/ndfind/)

A collection of three cython-optimized search functions for NumPy. When the required value is found,
they return immediately, without scanning the whole array. It can result in 1000x or larger speedups for 
huge arrays if the value is located close to the the beginning of the array.

## Installation: 

    pip install ndfind

## Contents

Basic usage:  
- `find(a, v)` finds v in a, returns index of the first match or -1 if not found
- `first_above(a, v)` finds first element in a that is strictly greater than `v`, 
returns its index or -1 if not found  
- `first_nonzero(a)` finds the first nonzero element in a, 
returns its index or -1 if not found

Advanced usage:
- `find(a, v, rtol=1e-05, atol=1e-08, sorted=False, missing=-1, raises=False)`
    Returns the index of the first element in `a` equal to `v`.
    If either a or v (or both) is of floating type, the parameters
    `atol` (absolute tolerance) and `rtol` (relative tolerance) 
    are used for comparison (see `np.isclose()` for details).
   
    Otherwise, returns the `missing` value (-1 by default)
    or raises a `ValueError` if `raises=True`.

    For example,

```python
    >>> find([3, 1, 4, 1, 5], 4)
    2
    >>> find([1, 2, 3], 7)
    -1
    >>> find([1.1, 1.2, 1.3], 1.2)
    1
    >>> find(np.arange(0, 1, 0.1), 0.3) 
    3
    >>> find([[3, 8, 4], [5, 2, 7]], 7)
    (1, 2)
    >>> find([[3, 8, 4], [5, 2, 7]], 9)
    -1
    >>> find([999980., 999990., 1e6], 1e6)
    1
    >>> find([999980., 999990., 1e6], 1e6, rtol=1e-9)
    2
```

- `first_above(a, v, sorted=False, missing=-1, raises=False)`
    Returns the index of the first element in `a` strictly greater than `v`.
    If either a or v (or both) is of floating type, the parameters
    `atol` (absolute tolerance) and `rtol` (relative tolerance) 
    are used for comparison (see `np.isclose()` for details).

    In 2D and above the the values in `a` are always tested and returned in
    row-major, C-style order.

    If there is no value in `a` greater than `v`, returns the `default` value 
    (-1 by default) or raises a `ValueError` if `raises=True`.

    `sorted`, use binary search to speed things up (works only if the array is sorted)

    
    For example,

```python
    >>> first_above([4, 5, 8, 2, 7], 6)
    2 
    >>> first_above([[4, 5, 8], [2, 7, 3]], 6)
    (0, 2) 
    >>> first_above([5, 6, 7], 9)
    3 
```

- `first_nonzero(a, missing=-1, raises=False)`
    Returns the index of the first nonzero element in `a`.

    In 2D and above the the values in `a` are always tested and returned in
    row-major, C-style order.

    For example,

```python
>>> first_nonzero([0, 0, 7, 0, 5])
2
>>> first_nonzero([False, True, False, False, True])
1
>>> first_nonzero([[0, 0, 0, 0], [0, 0, 5, 3]])
(1, 2)
```

## Testing

Run `pytest` in the project root.