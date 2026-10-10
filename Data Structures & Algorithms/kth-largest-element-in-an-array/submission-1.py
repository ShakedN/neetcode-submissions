import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapmin=[]
        for n in nums:
            heapq.heappush(heapmin,-n)
        for i in range(k):
            n=heapq.heappop(heapmin)
        return -n