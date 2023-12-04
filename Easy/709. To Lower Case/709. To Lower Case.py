#041223 Submission
class Solution:
    def toLowerCase(self, s: str) -> str:

        # Approach
        # 1) Initialize output to store answer
        # 2) Loop through s. Check if iteration is uppercase, if it is, add the lowercase to output. Else, add iteration to output

        output: str = ""

        for i in s:
            if i.isupper() == True:
                output += i.lower()
            else:
                output += i
        return output

        # Test cases
        # 1) All uppercase
        #    s = "HELLO" -> Returns "hello"
        # 2) All lowercase
        #    s = "hello" -> Returns "hello"
        # 3) Mix of upper and lower case
        #    s = "hElLo" -> Return "hello"
        
        # Runtime = 34ms, beats 78.82% of users
        # Memory = 16.44MB, beats 6.94% of users
        
