# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Explore
 - left subtree values < node.val
 - right subtree values > node.val

Brainstorm
 - max of bst should be the rightmost node
 - could bruteforce and just grab all of the nodes in a tree and put them in an array... 
 - do an inorder traversal to sort them and return arr[k-1]

Approach
 - res = []
 - def dfs(node)
    - if not node: return
    - dfs(node.left)
    - res.append(node)
    - dfs(node.right)

 - dfs(root)
 - return res[k - 1]
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k - 1]

        