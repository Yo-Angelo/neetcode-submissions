class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 1
        p2 = len(numbers)
        while (p1-1 < len(numbers) - 1):
            while (p2 != p1):
                if (numbers[p1-1] + numbers[p2-1] == target):
                    return [p1, p2]
                p2 -= 1
            p1 += 1
            p2 = len(numbers)

        return []
                
        