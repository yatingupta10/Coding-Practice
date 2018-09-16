from itertools import permutations

s = raw_input("input: ")
s1 = raw_input("input 2 string: ")

# s3 = s + s
# s4 = s[::-1] + s[::-1]

# print s3
# print s4

# perm_list = list()

# for i in range(len(s3)/2):
# 	j = i + len(s)
# 	perm_list.append(s3[i:j])
# 	perm_list.append(s4[i:j])

# perm_list = [''.join(p) for p in permutations(s)]

# perm_list = list(set(perm_list))

char_map = {x:0 for x in s}

for i in range(len(s)):
	char_map[s[i]] += 1
# print char_map
substrings_s1 = [s1[i:i+len(s)] for i in xrange(len(s1) - len(s) + 1)]
print substrings_s1

substrings_s1_1 = {k:v for k,v in char_map.items()}
print substrings_s1_1
for i in substrings_s1:
	substrings_s1_1 = {k:v for k,v in char_map.items()}
	for letter in i:
		if letter in substrings_s1_1:
			# print "++++++++++++++"
			substrings_s1_1[letter] -= 1
	if all(x==0 for x in substrings_s1_1.values()) == True:
		print "True"
		break

