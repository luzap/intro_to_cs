# Recursion

## Sorting

- Most sorting algorithms benefit from recursion
- Selection sort: start a pointer at the head of the list, swap the smallest element, moving it forward
- Complexity: a measure of the amount of work an algorithm has to do to solve a problem.
- Merge sort: recursively split the lists into pairs. Sort those pairs. Merge until original list length is regained

Selection sort:

```python
def selection(nums):
    n = len(nums)

    for current in range(n - 1):
        smallest = current
        for i in range(current + 1, n):
            if nums[i] < nums[smallest]:
                smallest = i

            swap = nums[smallest]
            nums[smallest] = nums[current]
            nums[current] = swap

    return nums
```

Merge sort

```python
import heapq

def merge(nums):
    n = len(nums)
    if n <= 1:
        return nums
    middle = n // 2
    l = nums[:middle]
    r = nums[middle:]

    left = merge(l)
    right = merge(r)

    return list(heapq.merge(left, right))
```

## Backtracking

- Backtracking: incrementally try solutions until you find the right one
- when combined with recursion, it's amazing
- allows us to incrementally try potentials and remember our work