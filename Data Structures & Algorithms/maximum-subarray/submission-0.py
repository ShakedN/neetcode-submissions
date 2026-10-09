class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -float("inf")
        m_sum=nums[0]
        curr_sum=nums[0]
        for n in nums[1:]:
            curr_sum=curr_sum+n
            if curr_sum<n:
                curr_sum=n
            m_sum=max(m_sum,curr_sum)
           
        return m_sum
                