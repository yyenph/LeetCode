class Solution(object):
    def uniquePaths(self, m, n):
       #m is row, n is col
        row = [0] * n
        for num in range(m):
            next_row=[1]*n #temporary value before computing
            for ind in range(n-2,-1,-1):
            #last index has 1 way to go, so it stay as 1, also to avoid out of index for the following line (using val in row and the one after to calculate number of way)
                next_row[ind]=row[ind] + next_row[ind + 1]
            row = next_row
            print(num,row)
        return row[0]
        
        
        
        