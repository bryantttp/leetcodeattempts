# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        length = 0  # Initialize the counter for length of linked list
        iterator = head
        while iterator:  # Loop through list to count length of linked list
            length += 1
            iterator = iterator.next

        count = 0  # Count here is used to identify the position before the position of the 'middle' node
        if length % 2 == 0:
            count = length / 2
        else:
            count = round(length / 2)

        itr = head
        while count:  # Since count is the position before the middle node, while loop will stop at the 'middle' node
            count -= 1  # This allows us to loop through and stop at the 'middle' node
            itr = itr.next  # Replaces the current node with the next node
        return itr

        # """
        # :type head: ListNode
        # :rtype: ListNode
        # """
