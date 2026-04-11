import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for idx in range(k):
            heapq.heappush(min_heap, nums[idx])

        for idx in range(k, len(nums)):
            heapq.heappush(min_heap, nums[idx])

            while len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
        