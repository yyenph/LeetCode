class Solution(object):
    def twoSum(self, numbers, target):
        # left=0
        # right=len(numbers)-1
        # while right>left:
        #     if numbers[left]+numbers[right]<target:
        #         left+=1
        #     elif numbers[left]+numbers[right]>target:
        #         right-=1
        #     else:
        #         return [left +1,right+1]
        # return []
     
       l,r = 0, len(numbers) -1
       while l < r:
            if numbers[l] + numbers[r] < target:
               l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]


