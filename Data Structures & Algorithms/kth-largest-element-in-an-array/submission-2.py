import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_max=[]
        for n in nums:
            heapq.heappush(heap_max,-n)
        for i in range(k):
            n=heapq.heappop(heap_max)
        return -n