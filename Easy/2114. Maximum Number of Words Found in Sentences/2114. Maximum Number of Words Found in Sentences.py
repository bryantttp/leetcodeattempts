class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0  # Initialize the counter
        for i in sentences:  # Loop through all strings in the list
            if count < i.count(' ') + 1:  # Check if the existing counter is smaller than the no. of spaces within the string + 1 -> which is the same as the no. of words in the string
                count = i.count(' ') + 1  # Update counter with the largest no. of words
        return count # Return the value for the largest no. of words
        # """
        # :type sentences: List[str]
        # :rtype: int
        # """
