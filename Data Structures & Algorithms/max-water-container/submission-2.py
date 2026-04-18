class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_amount = 0

        while left < right:
            cur_dist = right - left
            cur_amount = min(heights[left], heights[right]) * cur_dist

            max_amount = max(max_amount, cur_amount)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_amount