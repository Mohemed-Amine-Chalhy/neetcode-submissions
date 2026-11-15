from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        sol = []
        for i in range(k):

            f = max(count, key= count.get)
            sol.append(f)
            del count[f]
        return sol
