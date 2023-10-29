# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        count_length = head  # Set a variable as the first Node of the Linked List
        length = 0  # Initialize value of length
        while count_length:  # Loops through all Nodes
            length += 1
            count_length = count_length.next
        length -= 1  # Minus 1 so that the length would simulate the index of the Nodes

        iterator = head  # Set another variable as the first Node to loop through once more

        output = 0
        while iterator:
            output += iterator.val * 2 ** length  # Conversion of Binary value to Decimal value
            length -= 1
            iterator = iterator.next
        return output  # Returns answer

        # """
        # :type head: ListNode
        # :rtype: int
        # """
