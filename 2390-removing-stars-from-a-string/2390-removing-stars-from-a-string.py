class Solution(object):
    def removeStars(self, s):
        # l l e t * *
        strL = list(s)
        stack = []
        for char in strL:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        