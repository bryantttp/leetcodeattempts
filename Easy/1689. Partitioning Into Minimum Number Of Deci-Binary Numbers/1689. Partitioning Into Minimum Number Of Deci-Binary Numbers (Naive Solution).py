class Solution(object):
    def minPartitions(self, n):
        output = 0  # Initialize the output
        for i in n:  # Loop through all elements in the string
            if output < int(i):  # This checks if the current element is higher than what is stored in output
                output = int(i)
        return output  # Returns highest value which would be the min no. of deci-binary numbers needed

        # """
        # :type n: str
        # :rtype: int
        # """