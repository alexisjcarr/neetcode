# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Explore
 - level order traversal
 - examples (to the left)

Brainstorming
 - use bfs with a queue
 - O(n) time | O(n) space

Plan
 - initiate queue and add the [root] to it
 - pop of queue and add left and right to the queue
 - do this until the queue is empty (no more nodes to process)
"""
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)

        res = []

        while q:
            q_len = len(q)
            level = []

            for _ in range(q_len):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)

        return res
