# Basic Binary Search Algorithm
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Unit tests
assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
assert binary_search([1, 2, 3, 4, 5, 6], 7) == -1
