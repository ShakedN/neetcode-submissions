from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(arr):
            @lru_cache(None)
            def index(i):
                if i >= len(arr):
                    return 0
                return max(arr[i] + index(i + 2), index(i + 1))
            return index(0)

        return max(rob_line(tuple(nums[1:])), rob_line(tuple(nums[:-1])))