#151123 Submission
class Solution:
    def sortVowels(self, s: str) -> str:

        # Approach
        # 1) Initialize a string to store the output, 2 lists to store vowels and consonants separately
        # 2) Initialize another list to store all ASCII values of vowels by looping through s and sort -> O(2n)
        # 3) Loop through s and initialize a temporary counter. If it is a consonant, add to output, otherwise, add ASCII value from ASCII list based on temp counter's count and temp counter + 1. -> O(n)
        # 4) Return output

        # output: str = ""
        # consonants: List[str] = ["B","b","C","c","D","d","F","f","G","g","H","h","J","j","K","k","L","l","M","m","N","n","P","p","Q","q","R","r","S","s","T","t","V","v","W","w","X","x","Y","y","Z","z"]
        # vowels: List[str] = ["A","a","E","e","I","i","O","o","U","u"]
        # vowel_ASCII_list: List[int] = []

        # for i in s:
        #     if i in vowels:
        #         vowel_ASCII_list.append(ord(i))
        # vowel_ASCII_list.sort()

        # counter: int = 0
        # for j in s:
        #     if j in consonants:
        #         output += j
        #     else:
        #         output += chr(vowel_ASCII_list[counter])
        #         counter += 1
        
        # return output

        # Test cases
        # 1) No consonants
        #    s = "aEiOu" -> Returns "uiaOE"
        # 2) No vowels
        #    s = "bhg" -> Return "bhg"
        # 3) Mix of vowels and consonants
        #    s = "BHagOu" -> Return "BHugaO"

        # Runtime = 322ms, beats 13.46% of users
        # Memory = 19.10MB, neats 54.70% of users

        # Improved Solution
        # 1) Initialize a string to store the output, 2 lists to store vowels and consonants separately
        # 2) Initialize another list to store all ASCII values of vowels by looping through s and sort -> O(2n)
        # 3) Loop through s and initialize a temporary counter. If it is a VOWEL, add ASCII value from ASCII list based on temp counter's count and temp counter + 1. Else, add the iteration into output -> O(n)
        # 4) Return output

        output: str = ""
        consonants: List[str] = ["B","b","C","c","D","d","F","f","G","g","H","h","J","j","K","k","L","l","M","m","N","n","P","p","Q","q","R","r","S","s","T","t","V","v","W","w","X","x","Y","y","Z","z"]
        vowels: List[str] = ["A","a","E","e","I","i","O","o","U","u"]
        vowel_ASCII_list: List[int] = []

        for i in s:
            if i in vowels:
                vowel_ASCII_list.append(ord(i))
        vowel_ASCII_list.sort()

        counter: int = 0
        for j in s:
            if j in vowels:
                output += chr(vowel_ASCII_list[counter])
                counter += 1
            else:
                output += j
        
        return output

        # Runtime = 167ms, beats 42.72% of users
        # Memory = 19.19MB, beats 54.70% of users
