"""
Explore:
 - perms from nums that may have dupes

Brainstorm:
 - backtracking with a sort and dupe check

Plan:
 - sort nums and have a res array and a used array of len num (init all False)
 - backtrack(path):
    - len of path == len of nums: add path to res
    - iterate of range(nums):
        - if i > 0 and nums[i] == nums[i - 1]: continue
        - if no used[i]:
            - CHOOSE: 
            - change used[i] = True
            - add nums[i] to path
            - EXPLORE: backtrack(path)
            - UNCHOOSE: path.pop()
    - call backtrack([]), return res
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                elif not used[i]:
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

        