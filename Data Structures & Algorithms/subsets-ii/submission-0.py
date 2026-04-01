"""
Explore:
 - nums may have dupes
 - return all subsets

 - nums = [1,2,1]
 - output = [[], [1], [2], [1, 1], [1, 2], [1, 2, 1]]

Brainstorm:
 - backtrack with index

Plan:
 - res, path = []
 - def backtrack(i):
    - res.append(path[:])
    - if i == len(nums): return
    - choose: path.append(nums[i])
    - explore: backtrack(i + 1)
    - unchoose: path.pop()
 - backtrack(0)
 - return res
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        nums.sort()

        def backtrack(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:  # learn this
                    continue
                # choose
                path.append(nums[i])

                # explore
                backtrack(i + 1)

                # unchoose
                path.pop()

        backtrack(0)
        return res