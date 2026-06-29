#
# @lc app=leetcode.cn id=3795 lang=python3
#
# [3795] 不同元素和至少为 K 的最短子数组长度
#

# @lc code=start
class Solution:
    def minLength(self, nums: list[int], k: int) -> int:
        cnt = Counter()
        left = 0
        ans = 100001
        distinct_sum = 0

        for right, x in enumerate(nums):
            # x 第一次进入窗口，才加入不同元素和
            if cnt[x] == 0:
                distinct_sum += x
            cnt[x] += 1

            # 当前窗口不同元素和 >= k，尝试缩小窗口
            while distinct_sum >= k:
                ans = min(ans, right - left + 1)

                y = nums[left]
                cnt[y] -= 1

                # y 被完全移出窗口，才从不同元素和里减掉
                if cnt[y] == 0:
                    distinct_sum -= y

                left += 1

        return ans if ans<100001 else -1
# @lc code=end
