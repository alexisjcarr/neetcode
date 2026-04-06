class Solution:
    """
    BOX 1:
    Brainstorming:
        - DFS backtracking. Mark cell with '#' before recursing, restore after. Match char by char.
        - "DFS from each cell as potential start. Temporarily mark visited with '#', unmark on backtrack."

    Plan:
        - Try starting from every cell.
        - At each step:
            - if we've matched the whole word, return True
            - if out of bounds or char doesn't match, return False
            - mark visited
            - recurse in 4 directions
            - unmark before returning
    R,C=len(board),len(board[0])
    def dfs(r,c,i):
        if i==len(word): return True
        if r<0 or r>=R or c<0 or c>=C or board[r][c]!=word[i]: return False
        tmp=board[r][c]; board[r][c]='#'
        found=any(dfs(r+dr,c+dc,i+1) for dr,dc in[(1,0),(-1,0),(0,1),(0,-1)])
        board[r][c]=tmp; return found
    return any(dfs(r,c,0) for r in range(R) for c in range(C))
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols):
                return False

            if board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False