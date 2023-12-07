class Solution(object):
    def maxArea(self, height):
        #area  == height * width (width is gap between left and right)
        left, right = 0, len(height)-1
        n = len(height)
         # width = right - left; height min(height[left],height[right])
        maxA = (right - left) * min(height[left],height[right])
        while left < right:
            maxA = max(maxA,((right - left) * min(height[left],height[right])))
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return maxA
    