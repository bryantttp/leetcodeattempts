#031223 Submission
class Solution:
    def reverseWords(self, s: str) -> str:

        # Approach
        # 1) Initialize a counter to store first iteration of each string after a space
        # 2) Initialize output to store answer
        # 3) Loop through s. If iteration not equals to len of s and iteration == " ", temp = s[counter:iteration+1], add temp[::-1] to output and counter = iteration + 1. -> O(n)
        # 4) Return output
        
        # counter: int = 0
        # output: str = ""

        # for i in range(len(s)):
        #     if i != len(s)-1 and s[i] == " ":
        #         temp = s[counter:i]
        #         output += temp[::-1] # Slicing twice takes alot of time
        #         output += " "
        #         counter = i+1
        #     elif i == len(s)-1:
        #         temp = s[counter:i+1]
        #         output += temp[::-1]
        
        # return output

        # Test cases
        # 1) s = "Let's take LeetCode contest" -> Returns "s'teL ekat edoCteeL tsetnoc"
        # 2) s = "Mr Ding" -> Returns "rM gniD"

        # Runtime = 96ms, beats 6.28% of users
        # Memory = 16.98MB, beats 58.86% of users

        # Improved Approach
        # 1) Initialize output to store answer
        # 2) Use split function to split string into separate strings in a list
        # 3) Loop through list to add i[::-1] to output
        # 4) Return output

        output: str = ""
        a = s.split()

        for i in a:
            output += i[::-1]
            output += " "
        output = output[:-1]

        return output

        # Runtime = 42ms, beats 65.23% of users
        # Memory = 17.08MB, beats 31.50% of users
