class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
    
    # Approach
    # 1) Loop through s
    # 2) For each iteration of s, check if the first character of the ith string in words is the same -> Worst Time Complexity = O(n)
    # 3) Return true if all characters are the same, otherwise return false

    # for i in range(len(s)):
    #     if s[i] != words[i][0]:
    #         return False
    # return True
      
    # Test cases:
    # 1) Only one element
    #    words: ["a"], s:'a' -> True
    # 2) elements in words > elements in s 
    #    words: ["hi","how","are","you"], s:'hha' -> Returns True but should be False
    # 3) elements in words < elements in s
    #    words: ["fine","what","about","you"], s: 'fwayt' -> Error: Out of range

    # Improved Approach:
    # 1) Check if length of s is same as the no. of elements in words, otherwise return False -> Worst Time Complexity = O(1)
    # 2) Loop through s
    # 2) For each iteration of s, check if the first character of the ith string in words is the same -> Worst Time Complexity = O(n)
    # 3) Return true if all characters are the same, otherwise return false
    
        if len(s) != len(words):
            return False
        for i in range(len(s)):
            if s[i] != words[i][0]:
                return False
        return True
