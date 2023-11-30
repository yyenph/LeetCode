class Solution(object):
    def findDifference(self, nums1, nums2):
        answer = [[],[]]
        # convert to set
        set1 = set(nums1)
        set2 = set(nums2)
        # getting distinct num using - or set1.difference(set2) 
        answer[0]= list(set1 - set2)
        answer[1]= list(set2-set1)
        return answer
        