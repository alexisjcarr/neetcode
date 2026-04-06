class Solution:
    """
    BOX 1:
    Brainstorming:
        - Kadane's: max_current = max(num, max_current + num). Restart when extending makes things worse.
        - "Kadane's algorithm. At each element: extend or start fresh (if current sum went negative)."

    Plan:
    cur=mx=nums[0]
    for n in nums[1:]: cur=max(n,cur+n); mx=max(mx,cur)
    return mx
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub, curr_sum = nums[0], 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sub = max(max_sub, curr_sum)

        return max_sub
