graph = [[1,2], [3], [3], []]

# if len(graph[0] == 0):
# 	res [[]]

res = []
path  = []

# for i in graph[0]:
# 	path.append(i)
# 	if len(graph[i]) != 0:
# 		path.append(graph[i])
# 	res.append(path)
# print res
def dfs(index, q):
	if index == len(graph) - 1:
	    result.append(q)
	for val in graph[index]:
		# print val
		dfs(val, q + [val])

result = []
dfs(0, [0])
print result