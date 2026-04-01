class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(path[:])
                return

            # choose
            path.append(nums[i])

            # explore
            backtrack(i + 1)

            # unchoose
            path.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
        