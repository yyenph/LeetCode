# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l,r = 1,n
        while l < r:
            # myguess = (l+r)//2
            #using right switch 
            myguess = (l+r) >> 1 #right shift by 1
            result = guess(myguess)
            if result ==0:
                return myguess
            elif result == -1:
                r = myguess - 1                
            elif result == 1:
                l = myguess + 1
        return r if guess(r)==0 else 1 # check if upperbound need to be return like in case when input is (2,2)
            
            
        