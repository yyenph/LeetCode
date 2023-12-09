class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        # left,right = 0,k-1
        # count = 0
        # current_sum=sum(arr[left:right+1])
        # while right < len(arr):
        #     print(left,right)
        #     print(current_sum)/k
        #     if current_sum/k >= threshold:
        #         count+=1
        #     left+=1
        #     right+=1
        #     if right<len(arr):
        #         current_sum=current_sum - arr[left-1]+arr[right]
        # return count
        left,right = 0,0
        count = 0
        sum =0
        while right <len(arr):
            sum+=arr[right]
            if right-left+1 == k:
                if sum/k >= threshold:
                    count+=1
                    print('count',count)
                left+=1
                sum-=arr[left-1]
            right+=1
             
        return count
        