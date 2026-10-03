class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ_n=0
        summ=0
        flagZ=0
        for i in range(len(nums)):
            summ+=nums[i]
            summ_n+=i
        summ_n+=len(nums)
        return summ_n-summ
        