import heapq


class MedianFinder:
    """
    BOX 1:
    Brainstorming:
        - Max-heap lo (lower half), min-heap hi (upper half). Always balanced. Median from tops.
        - "Two heaps. Push to lo first, bubble top to hi, rebalance so lo>=hi in size."
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0