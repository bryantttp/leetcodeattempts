class Solution(object):
    def restoreString(self, s, indices):

        temp_dict = {}  # Create a dictionary to access the index-string pair, since we need to check the correct index and input the string

        for i in range(len(indices)):  # Loops through the index of indices
            temp_dict[indices[i]] = s[i]  # Pair the string to their allocated index, where index is the key and string is the value

        output = ''  # Initialize the output

        for j in range(len(indices)):  # Similar code as the loop above, but here I'm looking to loop through in ascending order (0,1,2,3...) to get the string back in the correct order
            output += temp_dict.get(j)  # For each number looped through, access the dictionary based on the number (key) and add the string (value) to output.

        return output

        # """
        # :type s: str
        # :type indices: List[int]
        # :rtype: str
        # """
