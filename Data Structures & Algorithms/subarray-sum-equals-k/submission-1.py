class Solution:
    """
    Explore
     - nums = [2,-1,1,2], k = 2
        4

    Brainstorm
     - can use prefix sum pattern
     - prefix_sum = { pfs: count } => { 0: -1 } make this defaultdict
     - total = 0
     - for num in nums:
        -   total += num
        -   diff = total - k
        -   if (total - k) in prefix_sum:
            - prefix_sum[total - k] += 1
        prefix_sum[total] += 1
     - return prefix_sum[k]
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        pfs = collections.defaultdict(int)
        pfs[0] = 1
        total, count = 0, 0

        for num in nums:
            total += num

            if (total - k) in pfs:
                count += pfs[total - k]

            pfs[total] += 1

        return count