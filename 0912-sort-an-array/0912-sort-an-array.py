class Solution(object):
    def sortArray(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = nums[:mid]
        right = nums [mid:]
        left_nums = self.sortArray(left)
        right_nums = self.sortArray(right)
        return self.mergeSort(left_nums,right_nums) 
        
    def mergeSort(self,left,right):
        l_index, r_index = 0,0
        result =[]
        while l_index < len(left) and r_index < len(right):
            if left[l_index] < right[r_index]:
                result.append(left[l_index])
                l_index += 1
            else: 
                result.append(right[r_index])
                r_index += 1
        result.extend(left[l_index:])
        result.extend(right[r_index:])
        return result
                
        
        
        
   