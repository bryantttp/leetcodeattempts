#221123 Submission
class Solution:
    def balancedStringSplit(self, s: str) -> int:

        # Approach
        # 1) Initialize output to count no. of balanced strings
        # 2) Initialize 2 counters to count no. of R and L and loop through s. For each iteration, check if it is R or L and add to respective counters. Check if counters are equal, if they are, add 1 to output and reset R and L to 0.

        output: int = 0
        R_counter: int = 0
        L_counter: int = 0
        for i in s:
            if i == "R":
                R_counter += 1
            elif i == "L":
                L_counter += 1
            if R_counter != 0 and L_counter != 0:
                if R_counter == L_counter:
                    output += 1
                    R_counter = 0
                    L_counter = 0
        return output

        # Test cases
        # 1) Mix of R and L
        #    s = "RLRRLLRLRL" -> Return 4
        
        # Runtime = 34ms, beats 82.76% of users
        # Memory = 16.20MB, beats 69.25% of users
        
