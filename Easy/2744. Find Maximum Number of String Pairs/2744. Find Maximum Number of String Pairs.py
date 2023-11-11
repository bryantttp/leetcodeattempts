# 111123 Submission
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        # Approach
        # 1) Create a dictionary to store all values of words as keys and count of its reverse string starting from 0 as the value -> O(n)
        # 2) Loop through words and check if its reverse value is in keys. If it is, value of the key + 1 -> O(n)
        # 3) Return sum of all values / 2 -> O(1)

        # dictionary: [str,int] = {}
        # for i in words:
        #     dictionary[i] = 0
        # for j in words:
        #     if j[::-1] in dictionary.keys():
        #         dictionary[j[::-1]] += 1
        # return sum(dictionary.values())/2

        # Test case:
        # 1) one string in words
        #    words = ["hi"] -> returns 0.0
        # 2) all strings are pairs
        #    words = ["hi","ih","ah","ha"] -> returns 2.0
        # 3) some strings are pairs
        #    words = ["hi","ih","le","ko"] -> returns 1.0

        # Test cases are correct but question testcases are wrong
        # output is not int

        # Improved Approach
        # 1) Create a dictionary to store all values of words as keys and count of its reverse string starting from 0 as the value -> O(n)
        # 2) Loop through words and check if its reverse value is in keys AND it is not the same as itself (Since the strings in words are distinct, strings with the same element inside eg. "aa" will not appear twice but may be counted wrongly). If it is, value of the key + 1 -> O(n)
        # 3) Return int sum of all values / 2 -> O(1)

        dictionary: [str,int] = {}
        for i in words:
            dictionary[i] = 0
        for j in words:
            if j[::-1] in dictionary.keys() and j != j[::-1]:
                dictionary[j[::-1]] += 1
        return int(sum(dictionary.values())/2)

        # Runtime = 51ms, beats 75.23% of users
        # Memory = 16.14MB, beats 72.52% of users
        
