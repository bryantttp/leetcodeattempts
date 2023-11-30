#301123 Submission
class Solution:
    def removeStars(self, s: str) -> str:

        # Approach
        # 1) Initialize a list to simulate stack
        # 2) Loop through s. For each iteration, if it is not a star, append it to the list, else, use pop() on the list
        # 3) Return the list

        output: List[str] = []
        
        for i in s:
            if i == "*":
                output.pop()
            else:
                output.append(i)
        return "".join(output)

        # Test cases:
        # 1) All stars on the left
        #    s = "****hello" -> Returns "hello"
        # 2) All stars on the right
        #    s = "heyhowareyou***" -> Returns "heyhoware"
        # 3) Mix of stars and letters
        #    s = "leet**cod*e" -> Returns "lecoe"
        
        # Runtime = 179ms, beats 80.17% of users
        # Memory = 17.94MB, beats 22.43% of users
