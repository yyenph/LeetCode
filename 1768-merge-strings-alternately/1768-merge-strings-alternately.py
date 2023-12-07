class Solution(object):
    def mergeAlternately(self, word1, word2):
        merge = ""
        maxlen = max(len(word1),len(word2))
        for i in range(maxlen):
            if i < len(word1):
                merge += word1[i]
            if i < len(word2):
                merge += word2[i]
        return merge
                

        