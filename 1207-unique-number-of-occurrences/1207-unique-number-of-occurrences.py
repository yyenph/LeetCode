class Solution(object):
    def uniqueOccurrences(self, arr):
        #Solution 1, nlogn because of sorting
        # occurence_cnt = []
        # sorted_arr = sorted(arr)
        # i,count = 0,1
        # while i < len(arr):
        #     if i == len(arr) -1:
        #         if count in occurence_cnt:
        #             return False
        #     elif sorted_arr[i] != sorted_arr[i+1]:
        #         if count in occurence_cnt:
        #             return False
        #         occurence_cnt.append(count)
        #         count = 1
        #     else:
        #         count += 1
        #     i += 1
        # return True
        #Solution 2, using hashmap and set to compare the count value. Time: O(n)
        occurence_cnt = {}
        for num in arr:
            occurence_cnt[num] = occurence_cnt.get(num, 0) + 1
            
        unique_count = set()
        for count in occurence_cnt.values():
            if count in unique_count:
                return False
            else:
                unique_count.add(count)
        return True
                
        
                