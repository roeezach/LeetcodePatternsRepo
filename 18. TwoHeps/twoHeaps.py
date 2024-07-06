from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num: int) -> None:
        heappush(self.max_heap, -num)
        heappush(self.min_heap, -heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return -self.max_heap[0]

# Example usage
median_finder = MedianFinder()
median_finder.add_num(1)
median_finder.add_num(2)
print(median_finder.find_median())  # Expected Output: 1.5
median_finder.add_num(3)
print(median_finder.find_median())  # Expected Output: 2.0
