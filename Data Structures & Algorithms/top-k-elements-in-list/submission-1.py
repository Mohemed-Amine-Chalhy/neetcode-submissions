from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ordered = [(count[c], c) for c in count]
        ordered.sort(key = lambda x: x[0], reverse = True)
        return [x for _,x in ordered][:k]

        