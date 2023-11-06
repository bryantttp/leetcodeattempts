class Solution(object):
    def truncateSentence(self, s, k):
        new_s = s.split()  # Function creates a list and stores each string into list
        output = ' '.join(new_s[0:k])  # Function returns a string with each element up til the kth element with a space in between each other
        return output
        # """
        # :type s: str
        # :type k: int
        # :rtype: str
        # """
