# def numIslands(grid):
#     q = [(i,j) for i,rows in enumerate(grid) for j,island in enumerate(rows) if island=='1']
#     removed = []
#     for i,j in q:
#         for I,J in (i,j+1), (i+1,j):
#             if 0<=I<len(grid) and 0<=J<len(grid[0]) and grid[I][J]=='1':
#                 q.remove(I,J)
#                 if (i,j) not in removed:
#                     removed += (i,j),
    
#     return len(q) - len(removed)
    
# # print(numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1',]]))
# # print(numIslands([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0',]]))

def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            # map() itself won't return anything, list(map()) can force it return value
            list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))