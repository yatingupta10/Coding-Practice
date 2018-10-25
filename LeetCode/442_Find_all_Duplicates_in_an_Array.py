class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dict_nums = dict()
        # # nums = list(nums)
        # for i in range(len(nums)):
        #     if str(nums[i]) not in dict_nums:
        #         dict_nums[str(nums[i])] = 1
        #     else:
        #         dict_nums[str(nums[i])] = dict_nums[str(nums[i])] + 1
        # l = list()
        # for key, value in dict_nums.items():
        #     if value == 2:
        #         l.append(int(key))
        # return l

        d = {}
        res = []
        for i in nums:
            if i in d:
                res.append(i)
            else:
                d[i] = 1
        return res