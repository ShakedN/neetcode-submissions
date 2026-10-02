class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_arr =sum(nums)#10
        if sum_arr%2==1:
            return False
        target=sum_arr/2
        def sum_target(target,i):
            if target==0:
                return True
            elif target<0 or i==len(nums):
                return False
            return sum_target(target-nums[i],i+1) or sum_target(target,i+1)
        summ=sum_target(target,0)
        return summ