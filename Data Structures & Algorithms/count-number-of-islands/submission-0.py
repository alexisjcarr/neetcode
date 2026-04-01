class Solution:
    """
    Explore:
     see examples

    Brainstorm:
     - dfs in the appropriate directions and increase a counter with a seen set
     - O(m*n)

    Plan:
     - counter, seen = 0, set()
     - ROWS, COLS = len(grid), len(grid[0])
     - spots = ROWS * COLS
     - for spot in spots:
        - if spot == '1':
            - count += 1
            - r, c = spots // COLS, spots % COLS
            - dfs(r, c) 
        - else:
            continue
        
     - dfs(r, c):
        - if g[nr][nc] == '0':
            return
        - directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        - for dr, dc in directions:
            - nr, nc = r + dr, c + dc
            - if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1' and (nr, nc) not in seen:
                - seen.add((nr, nc))
                - return dfs(nr, nc)
     - return counter
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            if grid[r][c] == '0':
                return

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 
                0 <= nc < COLS and 
                grid[nr][nc] == '1' and 
                (nr, nc) not in seen):
                    seen.add((nr, nc))
                    dfs(nr, nc)

        count, seen = 0, set()

        ROWS, COLS = len(grid), len(grid[0])
        spots = ROWS * COLS

        for spot in range(spots):
            r, c = spot // COLS, spot % COLS
            
            if grid[r][c] == '1' and (r, c) not in seen:
                count += 1
                seen.add((r, c))
                dfs(r, c)
            
            else:
                continue

        return count

        