from typing import List

def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
print(single_number([2, 2, 1]))  # Expected Output: 1
print(single_number([4, 1, 2, 1, 2]))  # Expected Output: 4
