class Solution:
    """
    Explore:
    intervals = [[1,3],[1,5],[6,7]]
    [[1, 5][6, 7]]

    Brainstorming:
     - sort the intervals first by starts, add first interval to res
     - iterate over the intervals starts and ends: 
        - last_end = res[-1][1]
        - if start <= last_end:
            - res[-1][1] = max(last_end, end)
        - else
            - output.append([start, end])
     - return output
     - O(nlogn) | O(n) space
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for start, end in intervals:
            last_end = res[-1][1]

            if start <= last_end:
                res[-1][1] = max(last_end, end)

            else:
                res.append([start, end])

        return res
        