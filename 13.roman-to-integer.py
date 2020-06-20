#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (53.06%)
# Likes:    1659
# Dislikes: 3100
# Total Accepted:    555.2K
# Total Submissions: 1M
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given a roman numeral, convert it to an integer. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: "III"
# Output: 3
# 
# Example 2:
# 
# 
# Input: "IV"
# Output: 4
# 
# Example 3:
# 
# 
# Input: "IX"
# Output: 9
# 
# Example 4:
# 
# 
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#

# @lc code=start
from collections import OrderedDict
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = OrderedDict()
        roman['I']= 1
        roman['V']= 5
        roman['X']= 10
        roman['L']= 50
        roman['C']= 100
        roman['D']= 500
        roman['M']= 1000

        integer_val = 0
        s_to_list = list(s)
        prev_letter = None
        for cur_letter in s_to_list:
            
            integer_val += roman[cur_letter]

            if prev_letter == 'I': 
                if cur_letter == 'V':
                    integer_val -= 2
                if cur_letter == 'X':
                    integer_val -= 2
            if prev_letter == 'X': 
                if cur_letter == 'L':
                    integer_val -= 20
                if cur_letter == 'C':
                    integer_val -= 20
            if prev_letter == 'C': 
                if cur_letter == 'D':
                    integer_val -= 200
                if cur_letter == 'M':
                    integer_val -= 200
            
            prev_letter = cur_letter

        return integer_val
# @lc code=end

# if __name__ == "__main__":

#     s1 = Solution()
#     print(s1.romanToInt("IX"))
