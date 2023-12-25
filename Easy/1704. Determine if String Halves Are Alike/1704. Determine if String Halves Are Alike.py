#261223 Submission
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        # Approach
        # 1) Initialize a list of vowels
        # 2) Loop through s. Initialize 2 counters, one to count vowels at first half and another to count vowels at 2nd half.
        # 3) If count of both is same, return True, else false

        vowels: list[str] = ["a",'e','i','o','u',"A","E","I","O","U"]
        start_counter: int = 0
        end_counter: int = 0
        for i in range(len(s)):
            if i >= len(s)/2:
                if s[i] in vowels:
                    end_counter += 1
            else:
                if s[i] in vowels:
                    start_counter += 1

        if start_counter == end_counter:
            return True
        return False
        
        # Test cases
        # s = "book" -> Returns True

        # Runtime = 42ms, beats 57.02% of users
        # Memory = 17.33MB, beats 5.47% of users


        
