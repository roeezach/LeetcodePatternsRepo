from heapq import heappop, heappush
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: List[ListNode]) -> ListNode:
    min_heap = []
    
    for i, lst in enumerate(lists):
        if lst:
            heappush(min_heap, (lst.val, i, lst))
    
    dummy = ListNode()
    current = dummy
    
    while min_heap:
        val, i, node = heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        node = node.next
        if node:
            heappush(min_heap, (node.val, i, node))
    
    return dummy.next
