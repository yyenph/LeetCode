class Solution(object):
    def uniqueOccurrences(self, arr):
        occurence_cnt = []
        sorted_arr = sorted(arr)
        i,count = 0,1
        while i < len(arr):
            if i == len(arr) -1:
                if count in occurence_cnt:
                    return False
            elif sorted_arr[i] != sorted_arr[i+1]:
                if count in occurence_cnt:
                    return False
                occurence_cnt.append(count)
                count = 1
            else:
                count += 1
            i += 1
        return True
                