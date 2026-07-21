import math

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        result_max = -math.inf
        while start < end:
            w = end - start
            h = heights[start] if heights[start] < heights[end] else heights[end]
            a = w * h
            result_max = max(result_max, a)
            # temp1 = abs(heights[start+1] - heights[end])
            # temp2 = abs(heights[start] - heights[end-1])
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return result_max
        