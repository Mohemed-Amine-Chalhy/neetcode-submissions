class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''

        s = strs[0]
        for i in range(len(s)):

            char = s[i]

            for j in range(1,len(strs)):

                if len(strs[j]) == i or char != strs[j][i]:
                    return s[:i]
        return s


