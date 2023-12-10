#101223 Submission
class Solution:
    def countAsterisks(self, s: str) -> int:
        
        # Approach
        # 1) Initialize output to store answer
        # 2) Loop through s. Initialize temp output and counter. If iteration == "|", counter += 1. If iteration == "*" and counter = 0, add 1 to output. If iteration == "*" and counter = 1, add 1 to temp output. If counter == 2, counter = 0 and temp output = 0. Temp output add to output
        # 3) Return output

        output: int = 0
        
        temp_output: int = 0
        counter: int = 0

        for i in s:
            if i == "|":
                counter += 1
            if i == "*" and counter == 0:
                output += 1
            if i == "*" and counter == 1:
                temp_output += 1
            if counter == 2:
                counter = 0
                temp_output = 0
        output += temp_output

        return output

        # Test cases
        # 1) No asterisks
        #    s = "hello" -> Returns 0
        # 2) Some asterisks and pairs
        #    s = "l|*e*et|c**o|*de|" -> Returns 2
        #    s = "he**||*llo" -> Returns 3
        
        # Runtime = 28ms, beats 97.65% of users
        # Memory = 16.17MB, beats 77.03% of users
