class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}

        for idx, num in enumerate(nums):
            val_idx[num] = idx

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in val_idx and val_idx[diff] != idx:
                return [idx, val_idx[diff]]

        return []