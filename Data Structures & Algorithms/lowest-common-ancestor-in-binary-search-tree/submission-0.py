# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Explore
 - BST: left vals smaller than parent, right
 - a node can be its own parent
 -            5
         3*         8
       1    4*     7  9
         2

 Brainstorm

 - cases:
    - if p|q <= root <= q|p => current node is parent
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else:
                return curr
        