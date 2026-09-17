class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_ch ={}
        count=len(t)
        for i in s:
            map_ch[i] = map_ch.get(i, 0) + 1
        for i in t:
            if i not in map_ch:
                return False
            if map_ch[i]==0:
                return False
            map_ch[i]=map_ch[i]-1
            count-=1
        if count==0:
            return True
        else:
            return False

            