# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Explore
 - empty tree is balanced

Brainstorm
 - This will likely take a dfs approach where we need to find the difference between
 the heights of the left and right subtrees of the tree.
 - O(n) time, where n is the number of nodes | O(h) space, where h is the height of the 
 tree

Plan
 - can have a global height_delta variable
 - dfs will take root node: always decide what dfs is doing
    - if not node: return 0
    - find heights of each subtree and save to left, right variables
    - reset nonlocal height_delta to abs(left-right)
    - call dfs(root)
    - return if height_delta <= 1
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            
            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                return False

            return dfs(node.left) and dfs(node.right)


        def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))


        return dfs(root)
        
