class Solution:
    def maxArea(self, heights: List[int]) -> int:
        high = 0
        p1 = 0
        p2 = len(heights) - 1
        while (p1 < p2):
            tmp = min(heights[p1], heights[p2]) * (p2-p1)
            print (tmp)
            if tmp > high: high = tmp
            if (heights[p2] < heights[p1]):
                p2 -= 1
            else:
                p1 += 1
        return high
        