class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_r=[]
        arr_r.append(1)
        multi=1
        for i in range(1,len(nums)):
            multi*=nums[i-1]
            arr_r.append(multi)
        arr_l=[1]*len(nums)
        multi=1
        for i in range(len(nums)-2,-1,-1):
            multi*=nums[i+1]
            arr_l[i]=multi
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=arr_r[i]*arr_l[i]
        return res


