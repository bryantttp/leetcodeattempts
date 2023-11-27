#271123 Submission
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # Approach
        # 1) Use set function to return distinct elements in sentence -> O(n)
        # 2) Check if its length is equal to 26

        output: str = set(sentence)
        return len(output) == 26

        # Test cases
        # 1) False scenerio
        #    sentences = "hello" -> Return False
        # 2) True scenerio
        #    sentences ="aabbcdefghijklmmmmnopqrstuvwxyyzz" -> Return True

        # Runtime = 35ms, beats 79.87% of users
        # Memory = 16.27MB, beats 38.82% of users
        
