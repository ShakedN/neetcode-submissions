class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        count=0
        def dfs(grid,r,c):
            if r==rows or c==cols or r==-1 or c==-1 or grid[r][c]=='0' : 
                return
            grid[r][c]='0'
            dfs(grid,r+1,c)
            dfs(grid,r,c+1)
            dfs(grid,r-1,c)
            dfs(grid,r,c-1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    dfs(grid,r,c)
                    count+=1
                    grid[r][c]='0'
        return count
