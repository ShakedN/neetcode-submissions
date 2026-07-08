class Solution:
    def maxArea(self, heights: List[int]) -> int:
        num_high=heights[0]
        i=0
        j=len(heights)-1
        sum_max=0
        while i<j:
            sum_max=max((j-i)*min(heights[i],heights[j]),sum_max)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return sum_max
