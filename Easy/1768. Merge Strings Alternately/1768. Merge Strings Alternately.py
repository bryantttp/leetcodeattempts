#171223 Submission
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Approach
        # 1) Initialize output to store answer
        # 2) Check which word is shorter. Loop through shorter len. For each iteration, output += iteration of word1 then word2. Loop from shorter len to longer len. output += iteration from the longer word
        # 3) Return output
        
        output: str = ""

        if len(word1) > len(word2):
            for i in range(len(word2)):
                output += word1[i]
                output += word2[i]
            for j in range(len(word2),len(word1)):
                output += word1[j]
            return output
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                output += word1[i]
                output += word2[i]
            for j in range(len(word1),len(word2)):
                output += word2[j]
            return output
        else:
            for i in range(len(word1)):
                output += word1[i]
                output += word2[i]
            return output

        # Test cases:
        # 1) Word 1 is longer than Word 2
        #    word1 = "abcd", word2 = "pq" -> Returns "apbqcd"
        # 2) Word 2 is longer than Word 1
        #    word1 = "ab", word2 = "pqrs" -> Returns "apbqrs"
        # 3) Both same length
        #    word1 = "abc", word2 = "pqr" -> Returns "apbqcr"

        # Runtime = 38ms, beats 61.53% of users
        # Memory = 16.17MB, beats 85.74% of users
