l = []
findNums = [4,1,2]
nums = [1,3,4,2]
for i in range(len(findNums)):
    flag = 0
    for j in range(len(nums)):
    	if nums[j] == findNums[i]:
    		temp = j
    		break
    temp_list = nums[j+1:]
    print temp_list
    for k in range(len(temp_list)):
    	if temp_list[k] > findNums[i]:
    		l.append(temp_list[k])
    		flag = 1
    		break
    if flag == 0:
    	l.append(-1)
    # for j in range(findNums.index(findNums[i]), len(nums)):
    #     if nums[j] > findNums[i]:
    #         l.append(nums[j])
    #         flag = 1
    #         break
    # if flag == 0:
    #     l.append(-1)
print l

# nums = [9,6,4,2,3,5,7,0,1]
# num1 = []
# for i in range(len(nums)+1):
# 	num1.append(i)
# # print num1
# print set(num1) - set(nums)