# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# class Solution(object):
#     def maxPoints(self, points):
#         """
#         :type points: List[Point]
#         :rtype: int
#         """
import numpy as np

points = [[1,2],[2,2],[2,3]]
max_coordinate = max(sum(points, []))
# print max_coordinate
grid = np.zeros((max_coordinate, max_coordinate))
# print grid
for i in points:
	grid[i[0]-1][i[1]-1] = 1

# print grid  
grid = grid[~np.all(grid == 0, axis=1)] 
# print [~np.all(grid == 0, axis=0)]
print grid
max_row = grid[grid.sum(axis=1).argmax()]  
max_column =  grid.sum(axis=0).argmax()   
print grid.diagonal()
print grid.trace()      