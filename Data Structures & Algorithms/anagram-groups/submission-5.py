from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = dict()
        for s in strs:
            count = frozenset(Counter(s).items())
            if count in out:
                out[count].append(s)
            else :
                out[count] = [s]
        return list(out.values())

        