# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    BOX 1:

    Explore:
    0 - 1 - 2 - 3 - 4 - 5 - 6 => 0 - 6 - 1 - 5 - 2 - 4 - 3

    i.e.
    (0) - (n-1) - (1) - (n-2) - (2) - (n-3) - ...

    Brainstorming:
    - Three steps: find middle (slow/fast), reverse second half, interleave both halves.
    - "Find middle → reverse second half → interleave. In-place O(1) space."

    Plan:
    slow=fast=head

    while fast and fast.next: slow=slow.next; fast=fast.next.next
    
    prev,curr=None,slow.next; slow.next=None

    while curr: nxt=curr.next; curr.next=prev; prev=curr; curr=nxt

    l1,l2=head,prev
    while l2:
        t1,t2=l1.next,l2.next; l1.next=l2; l2.next=t1; l1,l2=t1,t2
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        l1, l2 = head, prev

        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2

