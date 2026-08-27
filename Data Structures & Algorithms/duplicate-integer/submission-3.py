class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_={}
        count=0
        for i in range(len(nums)):
            if nums[i] not in map_:
                count+=1
                map_[nums[i]]=map_.get(nums[i],0)+1
            else:
                return True
        if count==len(nums):
            return False
        return False