# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Explore
root:      1
         2   3
        4 5

subroot:     2
           4   5

Brainstorm:
 - find head of subtree in tree and check recurse down to see if the other nodes match
 - O(n) | O(n)

Plan:
 - dfs helper: 
    - check base case of not node
    - check if node.val == subRoot.val:
    -   if so check vals for left and right subtrees
    - if no: return False
"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, subnode):
            if not node and not subnode:
                return True

            if node and subnode and node.val == subnode.val:
                return sameTree(node.left, subnode.left) and sameTree(node.right, subnode.right)

            return False

        def dfs(node):
            if not node:
                return False

            if sameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        