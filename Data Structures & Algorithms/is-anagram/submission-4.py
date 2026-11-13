class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        ord_a = ord('a')
        l = [0 for i in range(0,(ord('z') - ord_a )+1)] 
        for i in range(len(s)):
            l[ord(s[i]) - ord_a] += 1 
            l[ord(t[i]) - ord_a] -= 1 
        
        return l == [0 for _ in range(ord('z')- ord_a+1)]
        