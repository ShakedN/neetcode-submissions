class Solution:
    import random
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(path,used):
            if len(path)==len(nums):
                result.append(path[:])
                return 
            for num in nums:
                if num in used:
                    continue
                else:
                    path.append(num)
                    used.add(num)
                    backtrack(path,used)
                    path.pop()
                    used.remove(num)
        backtrack([],set())
        return result



