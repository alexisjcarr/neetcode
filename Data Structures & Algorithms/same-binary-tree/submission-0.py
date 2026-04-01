# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Explore

    1                 1
  2    3            2    3

Brainstorm
 - Will traverse down both trees and check values
 - O(n) time where n = num nodes | O(h) where h = tree height

Plan
 - dfs helper will recurse down both trees and check values
  
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                left = dfs(p.left, q.left)
                right = dfs(p.right, q.right)
                return left and right
            else:
                return False

        return dfs(p, q)

        