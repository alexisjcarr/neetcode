# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Explore
 - 1 - 2 - 3 - 4
       |_______|

Brainstorm:
 - Can potentially use slow and fast pointers
 - O(n) | O(1)

Plan:
 - s, f = head, head
 - while f.next.next:
    - s = s.next
    - f = f.next.next
    - if s = f: return True
 - return False
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        