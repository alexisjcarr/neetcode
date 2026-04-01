from collections import deque


class Solution:
    """
    Explore:
    return min number of minutes until no more fresh oranges

     - 0 = empty
     - 1 = fresh 🍊
     - 2 = rotten 🍊

     directions: { up, down, left, right }, no diagonals

    examples:
     min 0:[[2,1,1],
            [1,1,0], 
            [0,1,1]]

     min 1:[[2,2,1],
            [2,1,0], 
            [0,1,1]]

     min 2:[[2,2,2],
            [2,2,0], 
            [0,1,1]]

     min 3:[[2,2,2],
            [2,2,0], 
            [0,2,1]]

     min 4:[[2,2,2],
            [2,2,0], 
            [0,2,2]]

    Brainstorm:
     - iterate over grid and perform dfs on '2's. will need to ensure that we 
       don't go too deep at every iteration
        - O(m*n) time and space
     - could also do a bfs at every '2' node instead and this problem does well with this
        - O(m*n) time and space
     - I'll go with BFS

    Plan:
        - add 2s to q and their top, left, down, up neigbors
        - process
            - if empty or visited, skip
            - if 1, flip to rotten by adding to q
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        minutes, fresh_oranges = 0, 0

        # build queue and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))

                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # process queue
        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                # go through the 4 dirs if in range
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS 
                        and grid[nr][nc] == 1 
                        and (nr, nc) not in visited):
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            fresh_oranges -= 1
            
            minutes += 1

        return minutes if not fresh_oranges else -1
     