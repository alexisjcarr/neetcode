class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, seen = 0, set()

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            area = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and 0 <= nc < COLS and
                    (nr, nc) not in seen and 
                    grid[nr][nc] == 1
                ):
                    seen.add((nr, nc))
                    area += dfs(nr, nc)

            return area

        ROWS, COLS = len(grid), len(grid[0])
        spots = ROWS * COLS

        for spot in range(spots):
            r, c = spot // COLS, spot % COLS

            if grid[r][c] == 1:
                seen.add((r, c))
                max_area = max(max_area, dfs(r, c))

        return max_area
        