class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        roman_dict2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        sum_var = 0
        i = 0
        while(i!= (len(s))):
            if s[i:i+2] in roman_dict2.keys():
                sum_var += roman_dict2[s[i:i+2]]
                i = i + 2
            else:
                sum_var += roman_dict1[s[i]]
                i = i + 1
        return sum_var
                