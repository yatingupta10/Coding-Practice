# s = ["eat", "tea", "tan", "ate", "nat", "bat"]


# s_dict = dict()
# for ele in s:
# 	l = [0]*26
# 	for x in ele:
# 		l[ord(x) - ord('a')] += 1
# 	for i in range(len(l)):
# 		l[i] = str(l[i])
# 	str1 = ','.join(l)
# 	if str1 in s_dict:
# 		s_dict[str1].append(ele)
# 	else:
# 		s_dict[str1] = [ele]

# answer = []
# for key,value in s_dict.items():
# 	answer.append(value)

# print answer

#########################Final answer#################
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s_dict = dict()
        for ele in strs:
            l = [0]*26
            for x in ele:
                l[ord(x) - ord('a')] += 1
            for i in range(len(l)):
                l[i] = str(l[i])
            str1 = ','.join(l)
            if str1 in s_dict:
                s_dict[str1].append(ele)
            else:
                s_dict[str1] = [ele]

        answer = []
        for key,value in s_dict.items():
            answer.append(value)
        return answer