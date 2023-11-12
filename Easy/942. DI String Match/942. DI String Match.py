#121123 Submission
class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        # Approach
        # 1) Initialize output as an empty list
        # 2) Initialize a temporary counter b to count backwards, giving it a value of n and f to count forwards from the string, giving it value of 0
        # 3) Loop through s and check if it is "I" or "D". Append f to output if "I" and f = f + 1, otherwise append b and b = b - 1 -> O(n)
        # 4) Append f or c again (They would be the same number)
        # 5) Return output
        output: List[int] = []
        f = 0
        b = len(s)

        for i in s:
            if i == "I":
                output.append(f)
                f += 1
            else:
                output.append(b)
                b -= 1
        output.append(f)
        return output

        # Test cases:
        # 1) one element in s
        #    s = "I" -> Return [0,1]
        #    s = "D" -> Return [1,0]
        # 2) all same elements in s
        #    s = "III" -> Return [0,1,2,3]
        #    s = "DDD" -> Return [3,2,1,0]
        # 3) Mixture of elements
        #    s = "IDDI" -> Return [0,4,3,1,2]

        # Runtime = 62ms, beats 50.00% of users
        # Memory = 17.54MB, beats 63.88% of users

    
