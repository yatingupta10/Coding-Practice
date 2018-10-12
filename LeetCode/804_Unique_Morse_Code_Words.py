class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sets = set()
        dict = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}
        for word in words:
            str1=""
            for j in word:
                str1+=dict[j]
            sets.add(str1)
        return len(sets)