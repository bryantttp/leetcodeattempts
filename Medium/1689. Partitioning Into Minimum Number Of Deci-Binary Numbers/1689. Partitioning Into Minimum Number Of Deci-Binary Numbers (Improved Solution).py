class Solution(object):
    def minPartitions(self, n):
        return int(max(set(n)))  # Set creates a list and stores all unique values, max retains the highest value, which is the min no. of deci-binary numbers needed

        # """
        # :type n: str
        # :rtype: int
        # """
