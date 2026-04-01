class Solution:
    """
    iterate over idx, num in nums
        check to see if target - num in hash
            if so, return [idx, hash[target - num]]
        add hash[num] = idx
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = collections.defaultdict(int)

        for i, num in enumerate(nums):
            if (target - num) in hash:
                return [hash[target - num], i]
            hash[num] = i
    