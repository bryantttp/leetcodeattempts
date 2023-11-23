#231123 Submission
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        # Approach
        # 1) Use while loop to check if part in s, use replace function to remove part from s
        # 2) return s

        while part in s:
            s = s.replace(part,"",1) # 1 here is important as you only want to replace the left most 'part' each time
        return s

        # Test cases
        # 1) part not in s
        #    s = "abcde", part = "f" -> Returns "abcde"
        # 2) part in s
        #    s = "daabcbaabcbc", part = "abc" -> Returns "dab"

        # Runtime = 41ms, beats 61.75% of users
        # Memory = 16.37MB, beats 37.12% of users

        
