#111223 Submission
class Solution:
    def replaceDigits(self, s: str) -> str:
        
        # Approach
        # 1) Initialize 2 dictionaries with key-value pair being alphabet and number assigned to it (flipped for one of the dictionary) -> O(26)
        # 2) Initialize output to store answer
        # 3) Initialize list of alphabets in lowercase along with counter to help the creation of 2 dictionaries
        # 3) Loop through s. If iteration is in dict_1.keys(), add to output. Else, temp_index = dict_1[s[i-1]] + i, add dict_2[temp_index] to output -> O(n)

        dict_1: Dict[str,int] = {}
        dict_2: Dict[str,int] = {}
        output: str = ""

        alphabets: str = "abcdefghijklmnopqrstuvwxyz"
        counter: int = 1
        
        for i in alphabets:
            dict_1[i] = counter
            dict_2[counter] = i
            counter += 1
        
        for j in range(len(s)):
            if s[j] in dict_1.keys():
                output += s[j]
            else:
                temp_index = dict_1[s[j-1]] + int(s[j])
                output += dict_2[temp_index]
        
        return output

        # Test cases:
        # 1) Multiple changes in alphabets
        #    s = "a0b1c2" -> Returns "aabcce" 

        # Runtime = 34ms, beats 85.01% of users
        # Memory = 16.31MB, beats 12.79% of users
