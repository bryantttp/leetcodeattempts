class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Approach
        # 1) Check if .join function of both lists are the same
        return ''.join(word1) == ''.join(word2)  # .join function combines all element in a list in the form of a string with no space in between, since '' is used
        
