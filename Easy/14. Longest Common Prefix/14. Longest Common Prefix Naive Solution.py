class Solution(object):
    def longestCommonPrefix(self, strs):
        output = strs[0]  # Set the first string as the prefix
        for i in strs[1:]:  # Loop through the 2nd string onwards in strs
            if len(output) >= len(i):  # Check to make sure loop does not loop out of range
                output = output[0:len(i)]  # Shave output to make sure it is the same length as the iterated string
                for j in range(len(i)):
                    if output[j] != i[j]:  # Checks to see if element in both output and iterated string (with the same index) is the same
                        output = output[0:j]  # Cuts off the jth element in output since elements in both strings are not the same
                        break
            if len(output) < len(i):  # Check to make sure loop does not loop out of range
                i = i[0:len(output)]  # Shave the iterated string to make sure it is the same length as output
                for k in range(len(output)):
                    if output[k] != i[k]:
                        output = output[0:k]  # Cuts off the kth element in output since elements in both strings are not the same
                        break
        return output

        # """
        # :type strs: List[str]
        # :rtype: str
        # """