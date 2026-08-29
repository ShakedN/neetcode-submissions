class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_={}
        for i in range(len(nums)):
            if nums[i] not in map_:
                map_[nums[i]]=1
            else:
                map_[nums[i]]=map_[nums[i]]+1
        l=list(map_.items())
        l.sort(key=lambda x:-x[1])
        l  = [x[0] for x in l]
        return l[:k]
