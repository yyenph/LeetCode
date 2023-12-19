# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        #find out the lenght of the linked list
        n = 0
        currentNode = head
        while currentNode:
            n += 1
            currentNode = currentNode.next
        #find the mid node
        if n <= 1:
            return None
        mid = n //2
        # delete the middle one
        current = head
        #find the node before the mid node, to move pointer to next.next node
        for i in range(mid-1):
            current = current.next
        current.next = current.next.next
        # return the head
        return head
        