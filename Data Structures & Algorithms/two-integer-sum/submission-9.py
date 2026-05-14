class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = [[num, idx]for idx, num in enumerate(nums)]
        A.sort(key = lambda x:x[0])

        i = 0
        j = len(A) - 1

        while j > i:
            curr = A[i][0] + A[j][0]
            if curr == target:

                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif curr > target:
                j-=1
            elif curr < target:
                i += 1

        
            

        