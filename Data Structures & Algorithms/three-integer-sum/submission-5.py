class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        sol = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]: # Duplicate values
                continue

            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    sol.append([nums[i], nums[j], target])
            
            for j in range(i+1, len(nums)):
                count[nums[j]] +=1
        return sol
            