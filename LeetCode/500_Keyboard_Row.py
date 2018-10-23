class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o','p']
        middle_row = ['a','s','d','f','g','h','j','k','l']
        bottom_row = ['z','x','c','v','b','n','m']

        return [word for word in words if all(letter.lower() in top_row for letter in word) or all(letter.lower() in middle_row for letter in word) or all(letter.lower() in bottom_row for letter in word)]