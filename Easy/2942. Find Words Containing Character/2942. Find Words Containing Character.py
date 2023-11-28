#281123 Submission
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        # Approach
        # 1) Initialize output to store answer
        # 2) Loop through words. If x in words[i], output.append(i) -> O(n)
        # 3) Return output

        output: List[str] = []

        for i in range(len(words)):
            if x in words[i]:
                output.append(i)
        
        return output

        # Test cases
        # 1) x not in words
        #    words = ["abc","bcd","aaaa","cbc"], x = "z" -> Returns []
        # 2) x in all words
        #    words = ["leet","code"], x = "e" -> Returns [0,1]
        # 3) x in some words
        #    words = ["abc","bcd","aaaa","cbc"], x = "a" -> Returns [0,2]

        # Runtime = 65ms, beats 65.36% of users
        # Memory = 16.48MB, beats 22.01% of users
        
