class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         dict_num = dict()
#         for i in nums:
#             if str(i) not in dict_num.keys():
#                 dict_num[str(i)] = 1
#             else:
#                 dict_num[str(i)] = dict_num[str(i)] + 1
#         for key, value in dict_num.items():
#             if value == 1:
#                 result = int(key)
                
#         return result
        return 2*sum(set(nums))-sum(nums)       