# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Explore

s -> 1 -> 2 -> 3 -> 4 -> None
p     c   r

s <- 1   2 -> 3 -> 4 -> None 
              p     c   r
Brainstorm:
 - iterative better for time complexity

Plan:
 - sentinel.next = head
 - curr = head, prev = sentinel
 - while curr:
    - rest = curr.next
    - curr.next = prev
    - prev = curr
    - curr = rest

 return prev
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            rest = curr.next
            curr.next = prev
            prev = curr
            curr = rest

        return prev