"""
Explore (RE):
 - given a list of distinct nums that can be used
 to build a target
 - return all possible/unique combinations

- nums = [2, 5, 6, 9], target = 9
[9], [2, 2, 5]

Brainstorm(EA):
 - this will be a backtracking problem
 - O(len(nums)^?)

Plan(A):
 - backtrack(start, path, total)


"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_path, res = [], []

        def backtrack(idx, total):
            # base case
            if total == target:
                res.append(curr_path[:])
                return

            if idx >= len(nums) or total > target:
                return

            # choose
            curr_path.append(nums[idx])
            backtrack(idx, total + nums[idx])
            curr_path.pop()
            backtrack(idx + 1, total)
            

        backtrack(0, 0)
        return res