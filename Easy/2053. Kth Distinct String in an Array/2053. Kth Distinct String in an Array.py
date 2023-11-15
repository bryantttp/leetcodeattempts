#151123 Submission
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        # Approach
        # 1) Create a dictionary and store each element in arr as the key and its occurence as its value. For each repetition, value + 1 -> O(n)
        # 2) Loop through arr and initialize a counter with value 1. If counter == k and value of iteration in dictionary == 1, return iteration. Else if its value in dictionary is 1, counter += 1. -> O(n)
        # 3) Add a return empty string, if there is no condition fulfilled in 2)

        dictionary: dict[str,int] = {}
        for i in arr:
            if i in dictionary.keys():
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        counter: int = 1
        for j in arr:
            if counter == k and dictionary.get(j) == 1:
                return j
            elif dictionary.get(j) == 1:
                counter += 1
        return ""
        
        # Test cases
        # 1) Empty string (No distinct string or k out of bounds)
        #    arr = ["a","a","b","b"], k = 1 -> Returns 0
        #    arr = ["a","a","b","c"], k = 3 -> Returns 0
        # 2) Returns a string
        #    arr = ["a","b","c","d"], k = 1 -> Returns "a"
        #    arr = ["a","b","c","d"], k = 3 -> Returns "c"
        #    arr = ["a","a","b","c"], k = 1 -> Returns "b"

        # Runtime = 77ms, beats 64.17% of users
        # Memory = 16.58MB, beats 48.21% of users
