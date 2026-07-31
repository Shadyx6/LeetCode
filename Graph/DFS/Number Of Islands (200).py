class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(c,r):
            if r < 0 or r>=rows or c< 0 or c>=cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(c-1,r)
            dfs(c+1,r)
            dfs(c,r-1)
            dfs(c,r+1)
            return
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(c,r)
                    islands+=1
        return islands