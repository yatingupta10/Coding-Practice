from itertools import permutations

s = raw_input("input: ")
s1 = raw_input("input 2 string: ")

s3 = s + s
s4 = s[::-1] + s[::-1]

print s3
print s4

perm_list = list()

for i in range(len(s3)/2):
	j = i + len(s)
	perm_list.append(s3[i:j])
	perm_list.append(s4[i:j])

# perm_list = [''.join(p) for p in permutations(s)]

# perm_list = list(set(perm_list))
for i in perm_list:
	if i in s1:
		print "T"
		break
print perm_list