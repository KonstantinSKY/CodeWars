# Spiralize

A function to generate a square matrix of size n, filled with 1's in a spiral pattern, starting from the top-left corner and moving clockwise, except for the center element which is always 1.

## Usage

```python
spiralize(size: int) -> List[List[int]]
```

## Arguments
size: an integer representing the size of the square matrix to generate. Must be greater than or equal to 5.
## Example

>>> spiralize(5)
[[1, 1, 1, 1, 1],
 [0, 0, 0, 0, 1],
 [1, 1, 1, 0, 1],
 [1, 0, 0, 0, 1],
 [1, 1, 1, 1, 1]]
>>> spiralize(8)
[[1, 1, 1, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1]]
