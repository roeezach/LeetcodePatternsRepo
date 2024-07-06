# Subset Template
# Problem: Subsets

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    
    def backtrack(start=0, current_subset=[]):
        result.append(current_subset[:])
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
    
    backtrack()
    return result

# Unit tests
assert subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
