#131223 Submission
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        # Approach
        # 1) Initialize counter to count answer
        # 2) Loop through patterns. For each iteration, if it is in word, counter += 1
        # 3) Return counter

        counter: int = 0
        for i in patterns:
            if i in word:
                counter += 1
        return counter

        # Test cases
        # 1) Pattern not in word
        #    patterns = ["x","y","z"], word = "abc" -> Returns 0
        # 2) Pattern in word
        #    patterns = ["a","abc","bc","d"], word = "abc" -> Returns 3

        # Runtime = 36ms, beats 93.13% of users
        # Memory = 16.48MB, beats 9.88% of users
        
