from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
   
        @lru_cache(None)
        def index(i):
            if i>=n:
                return 0
            sum_max=max(index(i+2)+nums[i],index(i+1))
            return sum_max
        summ=index(0)
        return summ