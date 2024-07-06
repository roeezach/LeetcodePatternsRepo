# Problem: Find All Missing Numbers

from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    
    return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]

# Unit tests
assert findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
assert findDisappearedNumbers([1,1]) == [2]