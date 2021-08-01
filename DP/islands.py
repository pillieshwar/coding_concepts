class Solution:
    def dfs(self, grid, r, c, nr, nc):
        
        if(r<0 or c<0 or r>=nr or c>=nc or grid[r][c]=="0"):
            return 0
        
        grid[r][c]="0"
        self.dfs(grid,r-1,c, nr, nc)
        self.dfs(grid,r+1,c, nr, nc)
        self.dfs(grid,r,c-1, nr, nc)
        self.dfs(grid,r,c+1, nr, nc)
        
    def numIslands(self, grid: List[List[int]]) -> int:
        if(grid==None or len(grid) ==0):
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        
        no_of_islands = 0
        for r in range(nr):
            for c in range(nc):
                if(grid[r][c]=="1"):
                    no_of_islands += 1
                    self.dfs(grid, r, c, nr, nc)
                
        return no_of_islands
