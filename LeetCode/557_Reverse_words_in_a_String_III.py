class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        a = str()
        for i in s:
            i = i[::-1]
            a = a + i + " "
        a = a[:-1]
        return a