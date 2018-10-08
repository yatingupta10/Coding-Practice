def func():
	s1 = "aa"
	s2 = "aa"
	if len(s1) != len(s2):
		return False
	count = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			count += 1
			if count == 1:
				a = s1[i]
				b = s2[i]
			else:
				if s1[i] != b or s2[i] != a:
					return False
		if count>2:
			return False
	if count == 1:
		return False
	if count == 0:
		l = [0]*26
		for x in s1:
			if l[ord(x) - ord('a')] == 1:
				return True
			else:
				l[ord(x) - ord('a')] += 1
		return False
	return True

print func()

