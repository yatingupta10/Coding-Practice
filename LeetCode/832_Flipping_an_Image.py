class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # for i in range(len(A)):
        #     A[i].reverse()
        #     b = [1]*len(A[i])
        #     A[i] = map(operator.sub, b, A[i])
        # return A
        # res = []
        
        # for row in A:
        #     tmp = row[::-1]
        #     res.append([1-i for i in tmp])
        # return res
        # return [[1-i for i in row[::-1]] for row in A]
        return [map(lambda x: 1 - x, i[::-1]) for i in A]