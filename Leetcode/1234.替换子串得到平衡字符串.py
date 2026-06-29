#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:  # 已经符合要求啦
            return 0

        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            cnt[c] -= 1  # 注意 cnt 统计的是在子串 [left,right] 外面的字母个数
            while max(cnt.values()) <= m:  # 子串 [left,right] 满足要求
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1  # 缩小子串，把 s[left] 放到外面
                left += 1
        return ans
# @lc code=end

