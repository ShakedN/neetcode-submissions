class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_diff={}
        for i,num in enumerate(nums):
            if num in map_diff:
                return [map_diff[num],i]
            map_diff[target-num]=i
        