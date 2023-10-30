class Solution(object):
    def mostWordsFound(self, sentences):
        temp_dict = {}  # Create a dictionary for faster access
        for i in sentences:  # Loop through all strings in list
            temp_dict[i] = i.count(' ') + 1  # Add string and no. of words in dictionary in the form of key and values
        return max(temp_dict.values())  # Return the highest value in the dictionary, which is the max no. of words

        # """
        # :type sentences: List[str]
        # :rtype: int
        # """
