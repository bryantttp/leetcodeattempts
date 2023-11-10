#101123 Submission

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        # Approach
        # 1) Initialize a counter to count no. of inconsistent strings
        # 2) Initialize a list to store allowed individually
        # 3) Loop through allowed to store it in the list -> Worst Time Complexity = O(n) 
        # 4) Loop through words and check if each iteration contains any element in allowed and use .replace to remove them. If iteration length == 0, add 1 to counter -> Worst Time Complexity = O(n^2)
        # 5) Return counter

        # counter: int = 0
        # allowed_list: List[str] = []
        # for i in allowed:
        #     allowed_list.append(i)

        # for j in words:
        #     for k in allowed_list:
        #         if k in j:
        #             j = j.replace(k,"")
        #     if len(j) == 0:
        #         counter += 1
        # return counter

        # Test cases
        # 1) all words are consistent
        #    words = ["aabb","ab","aa","bb","a","b"], allowed = "ab" -> Returns 6
        # 2) no words are consistent
        #    words = ["xyz","yyy","zzz"], allowed = "ab" -> Returns 0
        # 3) some words are consistent
        #    words = ["abc","abcd","aab","bb"], allowed = "ab" -> Returns 2
        
        # Runtime = 287ms, beats 11.00% of users
        # Memory = 18.29MB, beats 85.62% of users

        # Improved Approach
        # 1) Initialize a counter to count no. of inconsistent strings
        # 2) Initialize a temp counter to track if the current string in words is inconsistent
        # 3) Loop through words and loop through each element of the iteration to check if element of the iteration is in allowed. If it is not, temp counter + 1. Else, loop continues. Once loop is done, if temp counter = 0, counter + 1 -> Worst Time Complexity = O(n^2)
        # 4) Return counter 
        
        counter:int = 0
        for i in words:
            temp_counter = 0
            for j in i:
                if j not in allowed:
                    temp_counter = 1
            if temp_counter == 0:
                counter += 1
        return counter

        # Runtime = 231ms, 68.67% of users beat
        # Memory = 18.42MB, 12.95% of users beat
