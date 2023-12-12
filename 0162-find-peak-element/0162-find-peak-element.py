class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        mid=0
        while left < right:
            mid = (left+right)//2
            if nums[mid]> nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return right
                
        
        
# [1]
# [1,2]
# [1,5,4]
# [1,3,2,1]
# [1,2,3,1]
# [7,4,5,1,9,4,4]
# index of any of the peaks