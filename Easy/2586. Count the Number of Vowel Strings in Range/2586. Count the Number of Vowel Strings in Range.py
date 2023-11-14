#141123 Submission
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        # Approach
        # 1) Initialize counter to count no. of vowel strings and list of vowels to check
        # 2) Loop through the list with range from left to right + 1. If the current iteration's first and last element is a vowel, counter + 1 -> O(n)
        # 3) Return counter

        # vowels: List[str] = ["a","e","i","o","u"]
        # counter:int = 0
        # for i in range(left,right+1):
        #     if words[i][0] in vowels and words[i][len(words[i])-1] in vowels:
        #         counter += 1
        # return counter

        # Test cases
        # 1) No vowel strings
        #    words = ["hello","hi","yes"], left = 0, right = 2 -> Returns 0
        # 2) All vowel strings
        #    words = ["ao","ie"], left = 0, right = 1 -> Returns 2
        # 3) Some vowel strings
        #    words = ["hello","ao","yes","ie","hi"] , left = 2, right = 4 -> Returns 1

        # Runtime = 75ms, beats 62.92% of users
        # Memory = 16.49MB, beats 64.44% of users

     
        
