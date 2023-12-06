class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        # left_product = [1] * n
        # reverve_product = [1] * n
        temp_l,temp_r = 1 , 1
        # for i in range(n):
        #     left_product[i] *= temp_l
        #     temp_l *= nums[i]
        #     reverve_product[n - 1 - i] *= temp_r #this code is to merge second loop into 1
        #     temp_r *= nums[n - 1 - i]
        # for j in range(n - 1 , -1, -1):
        #     reverve_product[j] *= temp_r
        #     temp_r *= nums[j]
     
        # return [left_product[i] * reverve_product[i] for i in range(n)]
#Optimize solution 1
        result = [1] * n
        for i in range(len(nums)):
            result[i] *= temp_l
            temp_l *= nums[i]

            result[n-1-i] *= temp_r
            temp_r *= nums[n - 1 - i]
        return result


        