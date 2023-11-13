class Solution:
    def countSeniors(self, details: List[str]) -> int:

        # Approach
        # 1) Initialize counter to count no. of 60 year olds
        # 2) Loop through details to check the int version of the 12th and 13th character, which is the person's age, to see if it is more than 60. If it is, counter + 1 -> O(n)
        # 3) Return counter

        counter: int = 0
        for i in details:
            if int(i[11:13]) > 60:
                counter += 1
        return counter

        # Test cases (All passed)
        # No seniors
        # details = ["1234567890M2201"] -> Returns 0
        # details = ["1234567890M2201","2345678901F2302"] -> Returns 0
        # Some seniors
        # details = ["1234567890M2201","2345678901F6102"] -> Returns 1
        # details = ["2345678901F6102","1234567890M2201","3456789012M7603"] -> Returns 2
        # All seniors
        # details = ["1234567890M6101"] -> Returns 1
        # details = ["1234567890M6101","2345678901F6102"] -> Returns 2

        # Runtime = 50ms, beats 65.27% of users
        # Memory = 16.23MB, beats 41.96% of users




        
