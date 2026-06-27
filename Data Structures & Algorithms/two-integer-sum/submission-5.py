class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}

        for i,n in enumerate(nums):
            if (target-n) not in pair:
                pair[n] = i
            else:
                return [pair[target-n], i]
        return

            
        