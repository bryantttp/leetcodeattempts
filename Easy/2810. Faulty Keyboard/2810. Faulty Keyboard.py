#091223 Submission
class Solution:
    def finalString(self, s: str) -> str:

        # Approach
        # 1) Initialize output to store answer
        # 2) Loop through s. For each iteration, if iteration == "i", output = [::-1]. else, add iteration to output -> O(n)
        # 3) Return output

        output: str = ""

        for i in s:
            if i == "i":
                output = output[::-1]
            else:
                output += i
        return output
        
        # Test cases:
        # 1) Only 1 i
        #    s = "string" -> Returns "rtsng"
        # 2) Multiple i
        #    s = "poiinter" -> Returns "ponter"
        
        # Runtime = 47ms, beats 73.98% of users
        # Memory = 50.18%, beats 50.18% of users
