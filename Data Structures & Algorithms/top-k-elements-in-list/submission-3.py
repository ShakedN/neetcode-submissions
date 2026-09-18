class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_amount={}
        for num in nums:
            map_amount[num]=1+map_amount.get(num,0)
        arr=[]
        for num,count in map_amount.items():
            arr.append([count,num])
        arr.sort()
        output=[]
        while len(output)<k:
            output.append(arr.pop()[1])
        return output




