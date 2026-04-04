# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    BOX 2:
    Brainstorming:
        - Fast pointer n+1 ahead of slow. When fast hits null, slow.next is the node to remove.
        - "Gap of n+1 (not n). Slow stops at node BEFORE the target."

    [1,2,3,4], n = 2
         s
             f
    Plan:
    dummy=ListNode(0,head); slow=fast=dummy

    for _ in range(n+1): fast=fast.next

    while fast: slow=slow.next; fast=fast.next

    slow.next=slow.next.next

    return dummy.next
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0, head)
            left = dummy
            right = head

            while n > 0:
                right = right.next
                n -= 1

            while right:
                left = left.next
                right = right.next

            left.next = left.next.next
            return dummy.next

        