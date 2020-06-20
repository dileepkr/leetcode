#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.00%)
# Likes:    1875
# Dislikes: 1595
# Total Accepted:    610.4K
# Total Submissions: 1.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
from operator import xor

class Solution(object):
    def single_lcp(self, str1, str2):
        lcp = []
        for c1, c2 in zip(str1, str2):
            if c1 == c2:
                lcp.append(c1)
            else:
                break
        ret_val = "".join(lcp)
        return ret_val

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        ret_lcp = strs[0]
        for i in range(0, len(strs)):
            ret_lcp = self.single_lcp(ret_lcp, strs[i])
            if ret_lcp == "":
                return ""
        return ret_lcp


# @lc code=end

# if __name__ == "__main__":
#     s1 = Solution()
#     strs = ['a', 'b']
#     print(s1.longestCommonPrefix(strs))

