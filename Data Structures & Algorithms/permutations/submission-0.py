"""
Explore:
 - return all possible permutations from nums
 - a permutation is combination where order matters (only use each num once
 in each permutation)

Brainstorm:
 - this will be a backtracking problem...
 - O(n * n!) time and O(n) space, where n is the size of the input array

Plan:
 - have a used array
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, used = [], [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    # choose
                    used[i] = True
                    path.append(nums[i])

                    # explore
                    backtrack(path)

                    # unchoose
                    path.pop()
                    used[i] = False

        backtrack([])
        return res