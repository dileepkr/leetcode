#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = []
        for idx, num in enumerate(nums, start=0):
            sec_val = (target - num)
            if num == sec_val:
                dup_idxs = [i for i, x in enumerate(nums) if x == num][:]
                if ( len(dup_idxs) <= 1 ):
                    continue
                else:
                    return dup_idxs
            elif(sec_val in nums):
                indices = [idx, nums.index(sec_val)]
                break
        
        return indices