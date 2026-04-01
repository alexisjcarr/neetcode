"""
Explore:
 - all possible combos of k numbers in range [1,n]
 - n = 3, k = 2 [[1,2], [2,3], [1,3]]

Brainstorm:
 - variation on combo sum, just don't sum
 -                          []
            [1]             [2]             [3]
        [1,2][1,3]       [2,1]*[2,3]      [3,1]*[3,2]*
     
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start, n + 1):
                # choose
                path.append(i)

                # explore
                backtrack(i + 1)

                # unchoose
                path.pop()


        backtrack(1)
        return res

        