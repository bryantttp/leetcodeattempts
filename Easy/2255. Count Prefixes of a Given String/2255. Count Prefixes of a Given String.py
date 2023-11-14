#141123 Submission
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

        # Approach
        # 1) Initialize counter to count no. of strings that are a prefix of s
        # 2) Loop through words. If length of iteration is = len(s) and iteration = s, counter + 1. If length of iteration < s and the iteration is equal to sliced s from 0 to len(iteration), counter + 1 -> O(n) 
        # 3) Return counter

        # counter: int = 0
        # for i in words:
        #     if len(i) == len(s):
        #         if i == s:
        #             counter += 1
        #     elif len(i) < len(s):
        #         if i == s[0:len(i)]: # Note: String slicing here is O(n), meaning worst time complexity for this code is O(n^2)
        #             counter += 1
        # return counter

        # Test cases
        # 1) No strings
        #    words = ["z","y","x"], s = "apple" -> Returns 0
        # 2) All strings
        #    words = ["a","ap","app"], s = "apple" -> Returns 3
        # 3) Some strings
        #    words = ["z","app","x"], s = "apple" -> Returns 1
                        
        # Runtime = 77ms, beats 6.25% of users
        # Memory = 16.51MB, beats 21.93% of users

        # Improved Solution
        # 1) Initialize counter to count no. of strings that are a prefix of s
        # 2) Loop through words. If length of iteration is <= len(s) and s startswith iteration, counter += 0
        # 3) Return counter

        counter: int = 0
        for i in words:
            if len(i) <= len(s):
                if s.startswith(i):
                    counter += 1
        return counter

        # Runtime = 51ms, beats 99.17% of users
        # Memory = 16.45MB, beats 60.02% of users
