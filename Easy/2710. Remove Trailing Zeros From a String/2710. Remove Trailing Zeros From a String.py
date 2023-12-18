#181223 Submission
class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        # Approach
        # 1) Initialize counter to count no. of 0
        # 2) Loop through num in reverse. If iteration == 0, counter += 1, else break
        # 3) Return num[0:len(num)-counter]

        counter: int = 0

        for i in range(len(num)-1,0,-1):
            if num[i] == "0":
                counter += 1
            else:
                break
        
        return num[0:len(num)-counter]

        # Test cases
        # 1) No 0 at the back
        #    num = "123" -> Return 123
        # 2) Some 0 at the back
        #    num = "51230100" -> Return 512301
        
        # Runtime = 48ms, beats 57.79% of users
        # Memory = 16.44MB, beats 23.64% of users
        
