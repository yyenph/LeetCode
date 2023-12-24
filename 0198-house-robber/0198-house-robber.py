class Solution(object):
    def rob(self, nums):
        #[1,2,3,1] 
        # choice1 = 0+1; c2 = 0 => max = 1
        #update: choice1 = 0, choice 2= 1
        #choice1 = 2 > choice2 (1) => max= 2
        #update: choice2 = 2, choice 1 = 1
        #choice1(1+3) = 4 > choice2 = 2 =>max=4
        #update choice1 = 2,choice2 = 4
        choice1,choice2 = 0,0
        for num in nums:
            currentmax = max(choice1 + num, choice2)
            choice1 = choice2
            choice2 = currentmax
        return currentmax
            
            
        