
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            res = max(left_height + right_height, res)

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return res       