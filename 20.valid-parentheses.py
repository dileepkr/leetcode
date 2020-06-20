#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.07%)
# Likes:    3950
# Dislikes: 192
# Total Accepted:    820.8K
# Total Submissions: 2.2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        br_dict = {}
        br_dict["("] = 1
        br_dict[")"] = 1
        br_dict["["] = 2
        br_dict["]"] = 2
        br_dict["{"] = 3
        br_dict["}"] = 3

        if not len(s) % 2 == 0 or len(s) == 0:
            return False
        else:
            retval = False
            for i, j in zip( range(0,len(s)/2), reversed(range(len(s)/2, len(s))) ):
                if not br_dict[s[i]] == br_dict[s[j]]:
                    retval = False
                    break
                    # return False
                else: 
                    retval = True
            return retval
        
# @lc code=end

