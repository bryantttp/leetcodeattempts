# 121123 Submission
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        # Approach
        # 1) Create a list consisting of the reverse string of each element in words -> O(n)
        # 2) Check if each element with the same index is the same. If it is, return the element in words. Else, loop until length of words and return empty array -> O(n)
        # reverse_words: List[str] = []
        # for i in words:
        #     reverse_words.append(i[::-1])
        # for j in range(len(words)):
        #     if reverse_words[j] == words[j]:
        #         return words[j]
        # return ""

        # Test case
        # 1) No palindrome
        #    words = ["hi"] -> Return ""
        # 2) 1 palindrome
        #    words = ["aaa"] -> Return "aaa"
        # 3) some palindrome
        #    words = ["asl","sts","lop","lol"] -> Returns "sts"
        # 4) all palindrome
        #    words = ["sss","aaa","ttt","ppp"] -> Returns "sss"

        # Runtime = 91ms, beats 32.70% of users
        # Memory = 16.49MB, beats 18.49% of users

        # Improved Approach
        # 1) Loop through words and check if the element is a palindrome by comparing its reversed string. Return the element it is a palindrome, otherwise loop through all elements. Return "" if there are no palindromes -> O(n)

        for i in words:
            if i == i[::-1]:
                return i
        return ""

        # Runtime = 73ms, beats 93.14% of users
        # Memory = 16.20MB, beats 97.86% of users
