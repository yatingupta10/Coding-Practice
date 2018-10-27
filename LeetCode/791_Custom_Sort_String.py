class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # T = "yatinyatin"
        freq_alphabet = dict(zip(list("abcdefghijklmnopqrstuvwxyz"), [0] * 26))
        ans = ""
        for x in freq_alphabet.keys():
            freq_alphabet[x] = T.count(x)
            # print T.count(x)
        # print freq_alphabet

        for x in S:
            ans += x * freq_alphabet[x]
            freq_alphabet[x] = 0

        for x in freq_alphabet.keys():
            if freq_alphabet[x] > 0: 
                ans += x * freq_alphabet[x]

        return ans