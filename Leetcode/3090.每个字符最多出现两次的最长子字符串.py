#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#


# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()  # type: ignore
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
