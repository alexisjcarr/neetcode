# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Explore:
 - 1 -> 2 -> 4
 - 1 -> 3 -> 5

Brainstorm:
 - sentinel to attach nodes to
 - compare the first nodes in while list1 and list2:
    - list1 <= list2:
        - temp = curr1
        - curr1 = curr1.next
        - temp.next = None
        - sentinel.next = temp
        - sentinel = temp
    - else:
        - temp = curr2
        - curr2 = curr2.next
        - temp.next = None
        - sentinel.next = temp
        - sentinel = temp
 - if list1:
        - sentinel.next(list1)
 - else:
        - sentinel.next(list2)

 - return sentinel.next
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list_sentinel = ListNode()
        curr = new_list_sentinel

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return new_list_sentinel.next
        