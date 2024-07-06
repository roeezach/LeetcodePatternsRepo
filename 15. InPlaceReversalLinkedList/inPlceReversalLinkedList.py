from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Unit tests
def list_to_array(head: ListNode) -> List[int]:
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array

def array_to_list(array: List[int]) -> ListNode:
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

head = array_to_list([1, 2, 3, 4, 5])
reversed_head = reverse_list(head)
output = list_to_array(reversed_head)
print("Actual Output:", output)  # Expected Output: [5, 4, 3, 2, 1]
