class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_chars=[0]*26
        max_ch=0
        left=0
        result=0
        for right in range(len(s)):
            count_chars[ord(s[right]) - ord('A')] += 1
            max_ch=max(max_ch,count_chars[ord(s[right])-ord('A')])
            while right-left+1-max_ch>k:
                count_chars[ord(s[left]) - ord('A')] -= 1
                left += 1
            result = max(result, right - left + 1)
        
        return result