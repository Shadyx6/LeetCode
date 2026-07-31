class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        notRotten = 0
        mins = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2 :
                    q.append((i,j))
                if grid[i][j] == 1:
                    notRotten+=1
        while q and notRotten > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                if r>0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    notRotten -=1
                    q.append((r-1,c))
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    notRotten -=1
                    q.append((r,c-1))
                if r < rows -1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    notRotten -=1
                    q.append((r+1,c))
                if c < cols -1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    notRotten -=1
                    q.append((r,c+1))                             

            mins+=1

        if notRotten > 0:
            return -1
        return mins

        