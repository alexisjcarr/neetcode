# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Explore
 - a root is always a good node
 - if the tree is empty, it has no good nodes 

Brainstorm
 - I think we can do dfs here while keeping track of the maximum of the path
 - O(n) time | O(n) space

Plan
 - count = 0
 - dfs(node, curr_max):
    - nonlocal count
    - if not node: return 0

    - if node.val >= curr_max: count += 1, curr_max = node.val
    - dfs(node.left, curr_max)
    - dfs(node.right, curr_max)
 - dfs(root, float("-inf"))
 - return count
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, curr_max):
            nonlocal count

            if not node:
                return 0

            if node.val >= curr_max:
                count += 1
                curr_max = node.val

            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, root.val)
        return count
        