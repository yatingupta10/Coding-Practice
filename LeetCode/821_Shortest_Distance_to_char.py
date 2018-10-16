# S = "loveleetcode"
# C = 'e'
# char_dist = [1]*len(S)
# for i in range(len(char_dist)):
# 	if S[i] == C:
# 		char_dist[i] = 0

# for i in range(1, len(char_dist) - 1):
# 	frwd = float("inf")
# 	bkwd = float("inf")
# 	if char_dist[i] != 0:	
# 		for jf in range(i+1, len(char_dist)):
# 			if char_dist[jf] == 0:
# 				frwd = jf
# 				break
# 		for jb in range(i-1, -1, -1):
# 			print "hi"
# 			if char_dist[jb] == 0:
# 				bkwd = jb
# 				break
# 		print frwd
# 		print bkwd
# 		if frwd < bkwd:
# 			char_dist[i] = frwd - i
# 		else:
# 			char_dist[i] = i - bkwd
# print char_dist

############Final Solution#######################
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        N = len(S)
        ans = [0]*N
				
        dist = float('inf')
        for i in range(N):
            if S[i] == C:
                dist = 0
            ans[i] = dist
            dist += 1
						
        dist = float('inf')
        for i in reversed(range(N)):
            if S[i] == C:
                dist = 0
            ans[i] = min(ans[i], dist)
            dist += 1
        return ans
