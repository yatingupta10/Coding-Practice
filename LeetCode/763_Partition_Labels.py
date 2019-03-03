S = "ababcbacadefegdehijhklij"


# print D

# def String_man(S):
# 	D = dict()
# 	for i in S:
# 		if i not in D:
# 			D[i] = S.count(i)
# 	key = max(D.iteritems(), key=lambda x:x[1])
# 	enum_list = list(enumerate(S))
# 	for i in enum_list:
# 		if i[1] == key[0]:
# 			index = i[1]
# 	L = S[:index]
# 	res.append(len(L))
# 	String_man(S[index:])
# 	return res

sizes = []
while S:
    i = 1
    # print set(S[:i]), set(S[:i])
    while set(S[:i]) & set(S[i:]):
    	print set(S[:i])&set(S[i:])
        i += 1
    sizes.append(i)
    S = S[i:]