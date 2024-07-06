# Top K Elements Template
# Problem: Top K Frequent Elements

import heapq
# from heapq import heappush, heappop
from collections import Counter
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
            counter = Counter(nums)
            min_heap= []
            for num, count in  counter.items():
                if len(min_heap) < k:
                    heapq.heappush(min_heap, (count,num))
                elif min_heap and count > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (count,num))
            top_k_numbers = [num for count, num in min_heap]
            return top_k_numbers        
        
# Unit tests
assert top_k_frequent([1,1,1,2,2,3], 2) == [2, 1]
assert top_k_frequent([1], 1) == [1]
