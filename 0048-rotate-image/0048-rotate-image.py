class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        #make row, become column, collumn become row
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]  
        # reverse the matrix
        for row in matrix:
            row.reverse()
        return matrix