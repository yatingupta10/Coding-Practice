import math
def createPalindrome(inp, b , isOdd):
	n = inp
	palin = inp

	if (isOdd):
		n = n/b

	while (n>0):
		palin = palin*b + (n%b)
		n = n/b
	return palin

def generatePaldindromes(L,n):
	count = 0
	for j in range(2):
		i = 1
		while (True):
			a = createPalindrome(i, 10,j%2)
			if a>n:
				print a
				return count
			b = int(math.pow(a,2))
			if b<L:
				i += 1
				continue
			p = []
			while b>0:
				p.append(b%10)
				b = b/10
			pCheck = True
			pLen = len(p)

			for k in range(pLen/2):
				if p[k] != p[pLen-k-1]:
					pCheck = False
			if pCheck:
				count += 1
			i += 1
 
# Function to print decimal palindromic number 
# def generatePaldindromes(L,n):
	# count = 0

	# for j in range(2):
	# 	i = 1
 #        while (True):
 #        	a = createPalindrome(i, 10, j % 2)
 #        	if a > n:
 #        		print a
 #        		break
 #        	b = int(math.pow(a,2))
 #        	if b<L:
	# 			i += 1
	# 			continue
	# 		p = []
	# 		while b>0:
	# 			p.append(b%10)
	# 			b = b/10
	# 		pCheck = True
	# 		pLen = len(p)
	# 		for k in range(pLen/2):
	# 			if p[k] != p[pLen-k-1]:
	# 				pCheck = False
	# 		if pCheck:
	# 			count += 1
 #        	i = i + 1 
	# return 0
		# i = 1

		# while (True):
		# 	a = createPalindrome(i, 10, j % 2)
		# 	if a > n:	
		# 		print a
		# 		return count
		# 	b = int(math.pow(a,2))
		# 	# if b<L:
		# 	# 	i += 1
		# 	# 	continue
		# 	p = []
		# 	while b>0:	
		# 		p.append(b%10)
		# 		b = b/10
		# 	pCheck = True
		# 	pLen = len(p)
		# 	for k in range(pLen/2):
		# 		if p[k] != p[pLen-k-1]:
		# 			pCheck = False
		# 	if pCheck:
		# 		count += 1

		# 	i += 1
		# 	print a, pCheck
   
# Driver Program to test above function 
L = "1"
R = "19028"
L = int(L)
R = int(R)
print int(math.ceil(math.sqrt(R)))
count = generatePaldindromes(L,int(math.ceil(math.sqrt(R))))
if L<=1 and 1<=R:
    count+=1
if L<=4 and 4<=R:
    count+=1
if L<=9 and 9<=R:
    count+=1
print count

