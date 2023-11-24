#241123 Submission
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        # Approach
        # 1) Initialize output to store strings in list
        # 2) Loop from ord(s[0]) to ord(s[3]). Nested Loop from s[1] to s[4]. For each iteration, append str(char[i]) + str(j) to output -> O(n^2)
        # 3) Return output 
        
        output: List[str] = []
        for i in range(ord(s[0]),ord(s[3])+1):
            for j in range(int(s[1]),int(s[4])+1):
                output.append(chr(i)+str(j))
        return output

        # Test cases:
        # 1) Same Column, Different Row
        #    s = "A1:A5" -> Return ["A1","A2","A3","A4","A5"]
        # 2) Different Column, Same Row
        #    s = "A1:F1" -> Return ["A1","B1","C1","D1","E1","F1"]
        # 3) Different Column, Different Row
        #    s = "K1:L2" -> Return ["K1","K2","L1","L2"]

        # Runtime = 42ms, beats 78.41% of users
        # Memory = 16.30MB, beats 47.27% of users

        # Improved Approach
        # 1) Initialize output to store strings in list
        # 2) Loop through ord(s[0]) to ord(s[3]) and append each letter into 
