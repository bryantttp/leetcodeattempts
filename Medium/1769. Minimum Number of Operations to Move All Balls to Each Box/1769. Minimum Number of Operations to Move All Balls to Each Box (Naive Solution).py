class Solution(object):
    def minOperations(self, boxes):
        output = []  # Initialize list to return

        for i in range(len(boxes)):  # i is used to note the position of the box we are looking at
            count = 0
            for j in range(len(boxes)):  # j is used to loop through the boxes to see how many operations are needed to shift to current box
                if boxes[j] == '1' and j != i:  # Ensure that there is a ball in the jth box and that j is not the same position as the current box
                    count += abs(j - i)  # Absolute value of the difference of i and j would give the no. of operations needed to shift the ball to the current box, at that instance
            output.append(count)  # Adding all the values after iterating through j would give the list of min number of operations
        return output

        # """
        # :type boxes: str
        # :rtype: List[int]
        # """
