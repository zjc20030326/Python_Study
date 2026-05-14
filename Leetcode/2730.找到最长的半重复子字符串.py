#
# @lc app=leetcode.cn id=2730 lang=python3
#
# [2730] 找到最长的半重复子字符串
#


# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 1
        left = 0
        cnt = 0  # 当前窗口中相邻相同字符的对数

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                cnt += 1

            while cnt > 1:
                if s[left] == s[left + 1]:
                    cnt -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# @lc code=end
