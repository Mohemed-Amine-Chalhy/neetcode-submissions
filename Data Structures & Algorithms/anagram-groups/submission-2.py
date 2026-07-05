class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            c = tuple((sorted(s)))
            d[c].append(s)
            
        return list(d.values())
            

        