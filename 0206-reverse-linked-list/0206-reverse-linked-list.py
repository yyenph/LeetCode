# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        currentN = head
        
        prevN = None
        while currentN:
            nextN = currentN.next #save the next Node before swapping
            currentN.next = prevN #swap current
            prevN = currentN #update PrevN
            currentN = nextN #update current
          
        return prevN
        