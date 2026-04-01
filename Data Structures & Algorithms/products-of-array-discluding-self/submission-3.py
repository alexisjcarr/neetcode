class Solution:
    """
    Explore:
    Example 1:
    Input: nums = [1,2,4,6]
    Output: [48,24,12,8]

    Example 2:
    Input: nums = [-1,0,1,2,3]
    Output: [0,-6,0,0,0]

    - what if we have an array of lengths 0 or 1? won't happen.

    Brainstorm:
    - nested for loop through array
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i != j:
                    temp *= j

        O(len(nums)**2) | O(len(nums))

    - find product of all nums and then go through and divide nums[i] from each position
        O(len(nums)) | O(1)

    Plan:
     - product_without_zeros, zeros = 1, 0
     - iterate through and accumulate product, and count zeros
     [1, 0, 2, 3] => product_without_zeros = 6
     - if zeros > 1 => [0] * len(nums)
     - else if zeros >= 1: iterate over nums again, 
        if num[i] == 0, nums[i] = product_without_zeros
        else nums[i] == 0
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeros = 1, 0

        for num in nums:
            if not num:
                zeros += 1
            else:
                product *= num

        if zeros > 1:
            return [0] * len(nums)

        for idx, num in enumerate(nums):
            if zeros:
                nums[idx] = product if nums[idx] == 0 else 0
            else:
                nums[idx] = product // num

        return nums
        