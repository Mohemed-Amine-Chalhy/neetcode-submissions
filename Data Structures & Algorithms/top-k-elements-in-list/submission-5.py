from collections import defaultdict 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k :
                heapq.heappop(heap)
        res = []

        while len(res)<k:
            res.append(heapq.heappop(heap)[1])
        return res


        
