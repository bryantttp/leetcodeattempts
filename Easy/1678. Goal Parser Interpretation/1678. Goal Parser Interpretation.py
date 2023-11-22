#221123 Submission
class Solution:
    def interpret(self, command: str) -> str:
        
        # Approach
        # 1) Initialize output to store string
        # 2) Loop through command and check iteration. If "G", add "G" to output. If "(", check if next iteration is "a". If it is, add "al" to output and add 3 to iteration. Else, add "o" to output and add 1 to iteration
        # 3) Return output

        output: str = ""
        for i in range(len(command)):
            if command[i] == "G":
                output += "G"
            elif command[i] == "(":
                if command[i+1] == "a":
                    output += "al"
                    i += 3
                else:
                    output += "o"
                    i += 1
        return output

        # Test cases:
        # 1) Only one type of letter
        #    command = "GGGG" -> Return "GGGG"
        #    command = "()()()" -> Return "ooo"
        # 2) All types of letters
        #    command = "G()(al)" -> Return "Goal"

        # Runtime = 36ms, beats 71.98% of users
        # Memory = 16.17MB, beats 64.13% of users

        
