#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.46%)
# Likes:    2733
# Dislikes: 4240
# Total Accepted:    905.9K
# Total Submissions: 3.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # num_list = list(str(x))
        # if x < 0:
        #     num_list.pop(0)
        #     ret_list = num_list[::-1]
        #     ret_list.insert(0,"-")
        #     retval_str = "".join(ret_list)
        #     retval = int(retval_str)
        # else:
        #     ret_list = num_list[::-1]
        #     retval_str = "".join(ret_list)
        #     retval = int(retval_str)
        
        # if (abs(retval) > 2 ** 31 -1):
        #     return 0
        # else:
        #     return retval

        # String based solution
        sign = (x > 0) - (x < 0)
        ret = int(str(x*sign)[::-1])
        return ret * sign * ( ret < 2**31 )

# @lc code=end