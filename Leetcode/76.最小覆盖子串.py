#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r = Counter(t)
        left = 0
        ans = ""
        min_len = len(s) + 1

        for right in range(len(s)):
            if s[right] in r:
                r[s[right]] -= 1

            while all(v <= 0 for v in r.values()):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left : right + 1]

                if s[left] in r:
                    r[s[left]] += 1

                left += 1

        return ans


# @lc code=end
