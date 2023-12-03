class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return len(s) == i #at the end of the loop if all char in s has been found in t, the i will be last index of s + 1,means same as len of s
        