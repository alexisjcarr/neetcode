# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Explore:
 - right side view of tree
 - if one node, just print node
 - only printing the rightmost elements of the tree on each level

Brainstorm
 - could do a level order traversal and only print the last of the level
 - O(n) time and O(n) space

Plan
 - will need a q and will need to put root int
 - res = []
 - while q:
    - level = []
    - qLen
    - for _ in qLen:
        - pop off node
        - if node:
        - level add node
        - append l and right nodes to q
    - if level:
        - res.append(level[-1])
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            level = []
            q_len = len(q)

            for _ in range(q_len):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level[-1])

        return res
        