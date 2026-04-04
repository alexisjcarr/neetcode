class Solution:
    """
    BOX 1

    Instead of checking every speed one by one, we notice that the total time needed decreases as the eating speed increases.
This means the answer lies in a sorted search space from 1 to max(piles).

Because the search space is ordered, we can use binary search to efficiently find the smallest speed that allows finishing the piles within h hours.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res