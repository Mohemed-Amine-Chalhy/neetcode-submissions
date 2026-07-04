class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len : int = min([len(s) for s in strs])

        for i in range(min_len, -1, -1):

            pref = [s[:i] for s in strs]
            set_pref = set(pref)
            
            if len(set_pref) == 1:
                return pref[0]
