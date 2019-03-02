class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxr = [max(row) for row in grid]
        maxc = [max(col) for col in zip(*grid)]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < maxr[i] and grid[i][j] < maxc[j]:
                    count = count + (min(maxr[i], maxc[j]) - grid[i][j])
        return count