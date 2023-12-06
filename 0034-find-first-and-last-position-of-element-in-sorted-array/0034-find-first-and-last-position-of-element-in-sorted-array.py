class Solution(object):
    def searchRange(self, nums, target):
        left =0
        right = len(nums)-1
        while left<=right:
            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right -= 1
            else:
                return [left,right]
        return [-1,-1]
        