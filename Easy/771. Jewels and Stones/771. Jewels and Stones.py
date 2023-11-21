#211123 Submission
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # Approach
        # 1) Initialize output to store no. of jewels
        # 2) Loop through jewels and check if iteration is in stones, if it is, add stones.count(iteration) to output -> O(n^2)
        # 3) Return output

        output: int = 0
        for i in jewels:
            if i in stones:
                output += stones.count(i)
        return output

        # Test cases
        # 1) No Jewels
        #    jewels = "z", stones = "abcde" -> Returns 0
        # 2) All Jewels
        #    jewels = "Aa", stones = "aAaA" -> Returns 4
        # 3) Some jewels
        #    jewels = "aA", stones = "aAAbbbb" -> Returns 3

        # Runtime = 31ms, beats 92.72% of users
        # Memory = 16.36MB, beats 33.54% of users
        
