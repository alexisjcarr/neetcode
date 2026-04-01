"""
Explore:
 - return unique combos of candidates that sum to target
 - Input: candidates = [9,2,2,4,6,1,5], target = 8

    Output: [
    [1,2,5],
    [2,2,4],
    [2,6]
    ]

Brainstorm:
 - this is a backtracking problem. will need to keep track of path and res. Build the path and check the sum
 - O(2^len(nums)) time | O(n) space

Plan:
 - global res and path
 - backtrack(start, path, current_sum):
    - if current_sum > target: return
    - if current_sum == target: copy path and return
    - for loop i from start to len(candidates):
        - choose: path.append(candidates[i])), backtrack(i + 1, path, current_sum += can[i])
        - path.pop(): unchoose()
 - backtrack(0)
 - return res
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, current_sum):
            if current_sum > target:
                return

            if current_sum == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # choose
                path.append(candidates[i])
                backtrack(i + 1, path, current_sum + candidates[i])
                path.pop()  # unchoose
                
        backtrack(0, [], 0)
        return res
        