class Solution:
    def minOperations(self, boxes):
        ans = [0]*len(boxes)  # Initialize list to store data on no. of operations per box
        count_from_left = 0  # This counts the no. of operations from the previous box to the current box (iterating from left side)
        accumulated_left_count = 0  # This counts the total no. of operations to the left of the array of boxes
        count_from_right = 0  # This counts the no. of operations from the box ahead to the current box (iterating from right side)
        accumulated_right_count = 0  # This counts the total no. of operations to the right of the array of boxes
        for i in range(1, len(boxes)):  # Range starts from the 2nd box as first i iteration checks if the 1st box has a ball or not. If there is a ball, count from left + 1
            if boxes[i-1] == '1':  #
                count_from_left += 1
            accumulated_left_count += count_from_left  # As the loop iterates from left to right, this would accumulate the no. of operations to the left
            ans[i] = accumulated_left_count  # Since the no. of operations to the left is based on the previous box (on its left) , the current accumulation of operations to the left would be the actual no. of left operations for the current box
        for i in range(len(boxes)-2, -1, -1):  # Range starts from the 2nd last box as i starts from 2nd last box and iterates to the left. The if function checks if the previous box has a ball or not. If there is a ball, count from right + 1
            if boxes[i+1] == '1':
                count_from_right += 1
            accumulated_right_count += count_from_right  # As the loop iterates from right to left, this would accumulate the no. of operations to the right
            ans[i] += accumulated_right_count  # Since the no. of operations to the right is based on the previous box (on its right), the current accumulation of operations to the right would be the actual no. of right operations for the current box
        return ans  # ans now holds the total no. of operations per box