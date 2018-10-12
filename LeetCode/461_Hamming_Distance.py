class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binx = '{0:032b}'.format(x)
        biny = '{0:032b}'.format(y)
        return sum([1 for x,y in zip(binx,biny) if x!=y])
        