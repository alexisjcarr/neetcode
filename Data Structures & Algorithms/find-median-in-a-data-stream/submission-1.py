import heapq


class MedianFinder:
    """
    BOX 1:
    Brainstorming:
        - Max-heap lo (lower half), min-heap hi (upper half). Always balanced. Median from tops.
        - "Two heaps. Push to lo first, bubble top to hi, rebalance so lo>=hi in size."
    """

    def __init__(self):
        self.hi = []  # min heap
        self.lo = []  # max heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    
    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0
