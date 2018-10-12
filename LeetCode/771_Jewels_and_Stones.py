class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = list(J)
        counts = 0
        for c in J:
            counts += S.count(c)
        return counts