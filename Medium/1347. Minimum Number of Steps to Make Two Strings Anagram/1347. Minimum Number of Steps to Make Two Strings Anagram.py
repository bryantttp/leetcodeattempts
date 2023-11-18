#181123 Submission
class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # Approach
        # 1) Initialize a counter to count no. of steps to make t an anagram of s
        # 2) Create 2 dictionaries to store each string in s/t as the key and its occurance as the value -> O(2n)
        # 3) Loop through len(t/s). Check if t iteration is in s dictionary keys and if it is, add the difference between the values in both dictionaries to counter. Check if s iteration is in t and if it is not, counter + 1. If t iteration is not in s dictionary, counter + 1. Check if s iteration is in t and if it is not, counter + 1. -> O(n)
        # 4) Return counter/2

        # counter: int = 0
        # s_dictionary: dict[str,int] = {}
        # t_dictionary: dict[str,int] = {}

        # for i in range(len(s)):
        #     if s[i] not in s_dictionary.keys():
        #         s_dictionary[s[i]] = 1
        #     else:
        #         s_dictionary[s[i]] += 1
        # for j in range(len(t)):
        #     if t[j] not in t_dictionary.keys():
        #         t_dictionary[t[j]] = 1
        #     else:
        #         t_dictionary[t[j]] += 1

        # for k in range(len(t)):
        #     if t[k] in s_dictionary.keys() and t[k] in t_dictionary.keys():
        #         counter += abs(s_dictionary.get(t[k]) - t_dictionary.get(t[k]))
        #         s_dictionary.pop(t[k])
        #         t_dictionary.pop(t[k])
        #         if s[k] not in t:
        #             counter += 1
        #     else:
        #         if t[k] not in s:
        #             counter += 1
        #         if s[k] not in t:
        #             counter += 1
        # counter = int(counter/2)

        # return counter

        # Test cases
        # 1) No steps needed
        #    s = "anagram", t = "mangaar" -> Return 0
        # 2) Some steps needed
        #    s = "apple", t = "bread" -> Return 3
        
        # Runtime = 471ms, beats 5.14% of users
        # Memory = 17.06MB, beats 5.14% of users

        # Improved Approach
        # 1) Initialize a counter to count no. of steps to make t an anagram of s
        # 2) Loop through a distinct list of elements in s, for each iteration,  if the difference between s.count(i) > t.count(i), add their difference to counter. This counts what is missing in t to become a anagram of s. If s.count(i) < t.count(i), whatever that t has in excess will be replaced by what it is missing in s, which has been taken into account in the previous line of code.
        # 3) Return output

        counter: int = 0
        for i in set(s):
            if (s.count(i)-t.count(i)) > 0:
                counter += (s.count(i)-t.count(i))
        return counter

        # Runtime = 100ms, beats 94.57% of users
        # Memory = 16.89MB, beats 65.13% of users
