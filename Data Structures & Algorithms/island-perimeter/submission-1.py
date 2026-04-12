class Solution:
    """
    explore:
        return the perimeter of the island...

        Input: grid = [
                        [1,1,0,0],
                        [1,0,0,0],
                        [1,1,1,0],
                        [0,0,1,1]
                    ]

        Output: 18

        each square has a perimeter of 4, but if two squares are touching it'd be 6
            - 3 touching squares is 8
            - 4 touching
            - but squares can touch in different orientations
            - so will just need to consider total squares (roughly area) and touching points (-2 each time)
            - perimeter = 4(total squares) - 2(touch points)

    brainstorm:

        Input: grid = [
                        [1,1,0,0],
                        [1,0,0,0],
                        [1,1,1,0],
                        [0,0,1,1]
                    ]

        Output: 18

        - bfs should get the total touch points
        - could also just do a simple iteration and check right and down dirs to see if there's another square (tp)

    plan:

    input: grid

    rows, cols = len(grid), len(grid[0])

    area = 0
    touch_points = 0

    for r in range(rows):
        for c in ranges(cols):
            if grid[r][c] == 1:
                area += 1

                for dr, dc in [(1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows) and (0 <= nc < cols) and
                        grid[nr][nc] == 1:
                            touch_points += 1

    return 4 * area - 2 * touch_points
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        area = 0
        touch_points = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area += 1

                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc

                        if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                                touch_points += 1

        return 4 * area - 2 * touch_points
