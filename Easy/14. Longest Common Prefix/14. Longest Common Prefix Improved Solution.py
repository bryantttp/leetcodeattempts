class Solution(object):
    def longestCommonPrefix(self, strs):
        output = ''  # Initialize empty string for output
        for i in range(len(strs[0])):  # Loop through each letter in a string
            for j in strs[1:]:  # Start from the second string, since we are using the first string to compare
                if i == len(j) or strs[0][i] != j[i]:  # Loop breaks if i reaches length of the iterated string, as it will go out of bounds OR if the element in the same index of both strings are not equal
                    return output
            output += strs[0][i]  # If loop does not break, that would mean that the ith element in all strings in strs is the same, hence we add it into output as that would be part of the prefix
        return output

        # """
        # :type strs: List[str]
        # :rtype: str
        # """