# Backtracking Template
# Problem: Permutations

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    
    def backtrack(start=0):
        if start == len(nums):
            result.append(nums[:])
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack()
    return result


# Unit tests
print(permute([1, 2, 3]))
assert permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
