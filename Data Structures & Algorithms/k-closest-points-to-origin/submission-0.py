import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x*x + y*y                    # squared distance from origin
            heapq.heappush(heap, (dist, x, y))  # heap orders by dist first

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)    # always pops the closest remaining point
            result.append([x, y])
        return result