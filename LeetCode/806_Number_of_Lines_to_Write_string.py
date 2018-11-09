class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        d = { b:a for a,b in zip(widths,string.ascii_lowercase)}
        lines, count = 1,0
        for c in S:
            if count + d[c] > 100:
                lines += 1
                count = 0
            count += d[c]
        return [ lines, count]