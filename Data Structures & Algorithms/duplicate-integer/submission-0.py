class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}
        for i in nums:
            if i not in numsMap:
                numsMap[i] = 1;
            else:
                return True
        return False

        