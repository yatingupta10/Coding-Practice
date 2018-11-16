class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(len(str(num))!=1):
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s
        return num