class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=[0]*128
        max_chars=0
        count=0
        for st in range(len(s)):
            temp=chars[:]
            j=st
            count=0
            while j<len(s):
                if temp[ord(s[j])]==1:
                    break
                temp[ord(s[j])]+=1
                j+=1
                count+=1
                max_chars=max(max_chars,count)
        return max_chars
             
