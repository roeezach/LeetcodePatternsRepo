# Two Pointers Template

# Problem Exam[le]: Container With Most Water

from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Unit tests
assert max_area([1,8,6,2,5,4,8,3,7]) == 49
