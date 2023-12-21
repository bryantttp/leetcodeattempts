# 211223 Submission
class Solution:
    def generateTheString(self, n: int) -> str:

        # Approach
        # 1) If n=1, return "a"
        # 2) Initialize output 
        # 3) If n is odd and not 1, add n*"a" to output and return output
        # 4) If n is even, add (n-1)*"a" + "b" to output and return output

        if n == 1:
            return "a"
        
        output: str = ""

        if n%2 == 1 and n != 1:
            output += n*"a"
        
        if n%2 == 0:
            output += (n-1)*"a"
            output += "b"
        
        return output

        # Test cases
        # 1) n is odd
        #    n = 3 -> Returns "aaa"
        # 2) n is even
        #    n = 4 -> Returns "aaab"

        # Runtime = 39ms, beats 44.74% of users
        # Memory = 17.37MB, beats 14.13% of users
