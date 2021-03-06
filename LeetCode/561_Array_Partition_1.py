# class Solution(object):
#     def arrayPairSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         sum = 0
#         for i in range(0,len(nums),2):
#             sum = sum + nums[i]
#         return sum
#         
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[i] for i in range(len(nums)) if i%2==0)