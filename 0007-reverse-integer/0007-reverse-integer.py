class Solution(object):
    def reverse(self, x):
        max_limit = 2**31 -1
        min_limit = -2**31
        answer = 0
        #compare if answer > max or < min: return 0
        # x %10 to get last digit, put it in answer, keep doing until x 
        sign = 1 if x >=0 else -1
        ab_num = abs(x)
        while ab_num:
            #take the last digit
            digit = int(ab_num % 10)
            answer = answer*10+ digit
            if answer*sign > max_limit or answer*sign < min_limit:
                return 0
            #remove the last digit
            ab_num = int(ab_num//10)
        return answer * sign
        