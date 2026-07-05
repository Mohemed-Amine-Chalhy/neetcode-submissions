#Boyer Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        stamina = 0
        for num in nums:
            if num == candidate:
                stamina +=1
            else:
                stamina -=1
                if stamina == 0:
                    candidate = num
                    stamina = 1


        return candidate



        