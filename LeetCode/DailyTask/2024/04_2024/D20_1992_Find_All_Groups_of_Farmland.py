from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(x, y):
            stack = [(x, y)]
            min_row, min_col = x, y
            max_row, max_col = x, y
            visited.add((x, y))
            
            while stack:
                cur_x, cur_y = stack.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and land[nx][ny] == 1:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        min_row = min(min_row, nx)
                        min_col = min(min_col, ny)
                        max_row = max(max_row, nx)
                        max_col = max(max_col, ny)
            
            return (min_row, min_col, max_row, max_col)
        
        rows, cols = len(land), len(land[0])
        visited = set()
        result = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    min_row, min_col, max_row, max_col = dfs(i, j)
                    result.append([min_row, min_col, max_row, max_col])
        
        return result

# Example usage
solution = Solution()
land = [[1,0,0],[0,1,1],[0,1,1]]
print(solution.findFarmland(land))  # Output: [[0, 0, 0, 0], [1, 1, 2, 2]]

land = [[1,1],[1,1]]
print(solution.findFarmland(land)) 

land = [[0]]
print(solution.findFarmland(land)) 