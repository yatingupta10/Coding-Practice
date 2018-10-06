# def check_palindrome(s):
# 	s1_len = len(s)
# 	for i in range(s1_len/2):
# 		if s[i] != s[s1_len - i - 1]:
# 			return False
# 	return True


# s_input = raw_input("input: ")

# # print s_input

# no_palindromes = 0
# s_len = len(s_input)
# list_palindromes = list()
# # list_palindromes = list(s_input)
# # print list_palindromes
# # print no_palindromes

# # h = check_palindrome("ab", 2) 
# # print h
# #implementing brute force

# for i in xrange(s_len):
# 	for j in xrange(i, s_len):
# 		x = check_palindrome(s_input[i:j + 1])
# 		if x == True:
# 			list_palindromes.append(s_input[i:j + 1])
# 			no_palindromes = no_palindromes + 1

# print no_palindromes
# print list_palindromes



########################Actual Code##########################################
class Solution(object):
    

    def countSubstrings(self, s):
        if s == None or len(s) == 0:
            return 0
        global count
        count = 0
        for i in range(len(s)):
            self.ext_palindrome(s, i, i) #odd length
            self.ext_palindrome(s, i, i + 1) #even length
        
        return count
    
    def ext_palindrome(self, s, left, right):
        global count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -=1
            right += 1
    
