class Solution(object):
    def truncateSentence(self, s, k):
        new_s = s.split()
        output = ' '.join(new_s[0:k])
        return output
        # """
        # :type s: str
        # :type k: int
        # :rtype: str
        # """
