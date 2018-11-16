# x1 = [s[i:i+2] for i in range(len(s)-2)]
#         s1 = s[1:]
# x2 = [s1[i:i+2] for i in range(len(s1)-2)]
s = "III"
roman_dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
roman_dict2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
sum_var = 0
# for key, value in roman_dict.items():
#     if len(key) == 2 and (key in x1 or key in x2):
#         sum_var += value
#         s.remove(key)
# for i in s:
#     sum_var += roman_dict[i]
i = 0
while(i!= (len(s))):
    if s[i:i+2] in roman_dict2.keys():
        print "lkfkm"
        print s[i:i+2]
        sum_var += roman_dict2[s[i:i+2]]
        i = i + 2
    else:
        sum_var += roman_dict1[s[i]]
        print sum_var, s[i], i
        i = i + 1
print sum_var  
# return sum_var