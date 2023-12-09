class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = {}
        for str in strs:
            char_count = [0] * 26 #array of 26 to count all c inside each str
            for c in str:
                char_count[ord(c)-ord('a')] +=1
            key_tuple=tuple(char_count) #convert to tupler to be ablt to use as key
            

            #if key_tuple is in anagram_map
            if key_tuple in anagram_map:
                anagram_map[key_tuple].append(str)
            else:
                anagram_map[key_tuple]=[str]
        return anagram_map.values()



