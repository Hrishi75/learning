# NumPy Basics

**Topic:** ai-ml-data
**Date:** 2026-06-09
**Source:** self-study, guided

## What it is

NumPy = "Numerical Python". A library that gives Python a fast **array** type
(`ndarray`) plus math that runs on whole arrays at once. It's the foundation
every other data/ML library (pandas, scikit-learn, PyTorch) is built on.

## Why it matters

Plain Python lists are slow for math and clumsy for tables of numbers.
NumPy arrays are:
- **Fast** — math runs in optimized C under the hood, not slow Python loops.
- **Vectorized** — do math on the whole array in one line, no loop needed.
- **The common language** — data in ML is just arrays of numbers. Learn this
  and pandas/ML models stop looking scary.

## Key points

- Import convention (everyone writes it this way):
  ```python
  import numpy as np
  ```
- An **array** is a grid of numbers. 1D = a list, 2D = a table/matrix.
- `shape` tells you the dimensions, e.g. `(3,)` = 3 items, `(2, 3)` = 2 rows × 3 cols.
- Math on arrays applies **element by element** — no loops.
- **Broadcasting** = NumPy auto-stretches a smaller thing (like a single number)
  to match the array, so `arr + 10` adds 10 to every element.

## Example

Run these in order. Use a Jupyter notebook OR a `.py` file OR the Python prompt.

```python
import numpy as np

# 1. Make arrays
a = np.array([1, 2, 3, 4])          # 1D array from a list
print(a)                            # [1 2 3 4]
print(a.shape)                      # (4,)  -> 4 elements
print(a.dtype)                      # int64 -> type of the numbers

# 2. 2D array (a table / matrix): 2 rows, 3 columns
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.shape)                      # (2, 3)

# 3. Vectorized math — no loop, whole array at once
print(a + 10)                       # [11 12 13 14]  (broadcasting)
print(a * 2)                        # [2 4 6 8]
print(a ** 2)                       # [1 4 9 16]

# 4. Quick-build helpers
print(np.zeros(3))                  # [0. 0. 0.]
print(np.ones((2, 2)))              # 2x2 of ones
print(np.arange(0, 10, 2))          # [0 2 4 6 8]  (start, stop, step)
print(np.linspace(0, 1, 5))         # 5 evenly spaced numbers 0..1

# 5. Indexing & slicing (same idea as lists, but powerful)
print(a[0])                         # 1   -> first element
print(a[-1])                        # 4   -> last element
print(a[1:3])                       # [2 3] -> items index 1,2
print(m[0])                         # [1 2 3] -> first row
print(m[1, 2])                      # 6   -> row 1, col 2

# 6. Stats in one call
print(a.sum())                      # 10
print(a.mean())                     # 2.5
print(a.max(), a.min())             # 4 1

# 7. Boolean filtering (HUGE in data work)
print(a[a > 2])                     # [3 4] -> keep only elements > 2
```

## Gotchas / things I got wrong

- Array math is **element-wise**, NOT matrix algebra. `a * b` multiplies
  matching positions. For real matrix multiply use `a @ b`.
- Slicing returns a **view**, not a copy — editing the slice edits the original.
  Use `.copy()` if you want an independent copy.
- `shape` is a tuple. `(4,)` (note the comma) means 1D with 4 items, different
  from `(4, 1)` which is a 2D column.

## Links

- Official quickstart: https://numpy.org/doc/stable/user/quickstart.html
- Cheat sheet: https://numpy.org/doc/stable/user/absolute_beginners.html

## My takeaway (fill after running)

- One thing that clicked: ...
- One thing still fuzzy: ...
