class Solution(object):
    def reverseVowels(self, s):
        #second solution
        s = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        i, j = 0, len(s) - 1
        while i < j:
            #iterate until found a vowel from front to back
            while i<j and s[i] not in vowels:
                i += 1
            #iterate until found a vowel from back to front
            while i< j and s[j] not in vowels:
                j -= 1 
            #after found, swap them
            s[i],s[j] = s[j],s[i]
            #after swapping, increment i, j to keep looking 
            i += 1
            j -= 1
            #join the list to return as string
        return ''.join(s)
            
                
            
        
        #first solution passed all but took too long 
        # vowels = ['a','e','i','o','u','A','E','I','O','U']
        # exist_vowels = []
        # vowels_index = []
        # for i, char in enumerate(s):
        #     if char in vowels:
        #         exist_vowels.append(char)
        #         vowels_index.append(i)
        # answer = [''] * len(s)
        # j = len(vowels_index) - 1
        # for i, char in enumerate(s): 
        #     if i not in vowels_index:
        #         answer[i] = s[i]
        #     else:
        #         answer[i] = exist_vowels[j]
        #         j -= 1
        # return ''.join(answer)        
        