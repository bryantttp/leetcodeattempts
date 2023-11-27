#271123 Submission
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        # Approach
        # 1) Initialize output to store invalid strings and counter to count no. of moves required for ")"
        # 2) Loop through s. If i = "(", output add "(". If i = ")" and "(" in output, output.pop(). Else, counter + 1 -> O(n)
        # 3) Return len(output) + counter
        
        output: List[str] = []
        counter: int = 0

        for i in s:
            if i == "(":
                output.append(i)
            elif i == ")" and "(" in output:
                output.pop()
            else:
                counter += 1
        
        return len(output) + counter

        # Test cases
        # 1) No valid strings
        #    s = "(((" -> Returns 3
        # 2) Mix of valid strings
        #    s = "())" -> Returns 1
        # 3) All valid strings
        #    s = "((()))" -> Returns 0

        # Runtime = 38ms, beats 61.33% of users
        # Memory = 16.20MB, beats 72.54% of users
