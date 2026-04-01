class Solution:
    """
    Explore
    [[1,2,4,8],
    [10,11,12,13],
    [14,20,30,40]]
    
    target = 10
    l, r = m[0][0], r[2][3]
    mdpt = m[1][1]

    Brainstorm
     - ROWS, COLS = len(m), len(m[0])
     - have l, r pointers at 0 and ROWS * COLS - 1
     - while l <= r:
        - mid = (l + r) // 2
        - row, col = mid // COLS, mid % COLS # why?
        - if mid == target: return True
        - elif m[row][col] < target:
            - l = m + 1
        - else:
            - r = m - 1
     - return False

    """
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(m), len(m[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // COLS, mid % COLS

            if m[row][col] == target:
                return True

            elif m[row][col] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False
        