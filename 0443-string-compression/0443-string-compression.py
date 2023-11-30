class Solution(object):
    def compress(self, chars):
        count = 1
        i = 0
        updating_i =0
    # check all the c except the last one
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                if count > 1:
                    chars[updating_i] = chars[i]
                    updating_i += 1 
                    strcount = str(count)
                    for digit in strcount:
                        chars[updating_i] = digit
                        updating_i += 1 
                    count = 1
                else:
                    chars[updating_i] = chars[i]
                    updating_i += 1
        #handling last c
        chars[updating_i] = chars[-1]
        updating_i += 1 
        if count > 1:
            strcount = str(count)
            for digit in strcount:
                chars[updating_i] = digit
                updating_i += 1
        # the new len is same as updating_i 
        return updating_i



           

            
        