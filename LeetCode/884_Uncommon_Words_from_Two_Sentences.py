class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        list_A = A.split(" ")
        list_B = B.split(" ")
        dict_ab = dict()
        for i in (list_A + list_B):
            if i not in dict_ab:
                dict_ab[i] = 1
            else:
                dict_ab[i] = dict_ab[i] + 1
        l = list()
        for key,value in dict_ab.items():
            if value == 1:
                l.append(key)
        return l
                