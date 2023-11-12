#131123 Submission
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        # Approach
        # 1) Initialize counter 
        # 2) Loop through words. If length of pref > length of element, break and move to next iteration. If element sliced from 0 to length of pref is equal to pref, counter + 1 -> O(n)
        # 3) Return counter

        # counter: int = 0
        # for i in words:
        #     if len(pref) > len(i):
        #         break
        #     else:
        #         if i[0:len(pref)] == pref:
        #             counter += 1
        
        # return counter

        # Test cases
        # 1) No prefix
        #    words = ["hello","how","apple"], pref = "te" -> Returns 0
        # 2) All contains prefix
        #    words = ["hello","how","heather"], pref = "h" -> Returns 3
        # 3) Some contains prefix
        #    words = ["pay","attention","practice","attend"], pref = "at" -> Returns 2

        # Error with submission
        
        # Approach
        # 1) Initialize counter 
        # 2) Loop through words. If length of pref < or equal to length of element, break and move to next iteration. If element sliced from 0 to length of pref is equal to pref, counter + 1 -> O(n)
        # 3) Return counter

        counter: int = 0
        for i in words:
            if len(pref) <= len(i):
                if i[0:len(pref)] == pref:
                    counter += 1
        
        return counter

        # Runtime = 51ms, beats 35.07% of users
        # Memory = 16.37MB, beats 54.18% of users

