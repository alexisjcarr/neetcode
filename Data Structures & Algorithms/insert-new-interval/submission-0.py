class Solution:
    """
    Brainstorm:
    - intervals are already sorted
    - merge intervals but with an extra interval to place

    Plan:
    - no need to sort, as they're already sorted
    - merged_intervals[intervals[0]]

    for start, end in intervals:
        get the last end
        new_start, new_end = newInterval

        first see if new_start <= last_end:
            if so, merge newInterval with last interval and add to end of merged_intervals

        recompute last_end jic
        see if start <= last end:
            if so merge

    return merged_intervals
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
        