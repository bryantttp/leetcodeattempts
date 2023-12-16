#151223 Submission
class Solution:
    def freqAlphabets(self, s: str) -> str:

        # Approach
        # 1) Initialize output to store answer
        # 2) Initialize alphabet as a string
        # 3) Loop through s. Check if i+2 == #, if it is, output += alphabet[int(i+(i+1))-1] and i = i+2. else, output += alphabet[i]
        # 4) Return output

        output: str = ""
        alphabet: str = "abcdefghijklmnopqrstuvwxyz"
        counter: int = 0

        for i in range(len(s)):
            if counter != 0:
                counter -= 1
            elif i+2 <= len(s)-1 and s[i+2] == "#":
                output += alphabet[int(s[i]+s[i+1])-1]
                counter = 2
            else:
                output += alphabet[int(s[i])-1]
        return output

        # Test cases:
        # 1) No #
        #    s = "1234" -> Returns "abcd"
        # 2) All #
        #    s = "10#11#12#" -> Returns "jkl"
        # 3) Mix of # 
        #    s = "1326#" -> Returns "acz"

        # Runtime = 39ms, beats 53.49% of users
        # Memory = 16.31MB, beats 22.96% of users
