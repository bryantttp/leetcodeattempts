#261123 Submission
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        # Approach
        # 1) Initialize list to store distinct values of alphabets in message -> O(n)
        # 2) Initialize a dictionary to store alphabets as value and each iteration of list in 1) as its key -> O(26)
        # 3) Initialize output to return secret message
        # 4) Loop through message and append dictionary[iteration] to output. Add a space for each space in message -> O(n)

        # dictionary: Dict[str,str] = {}
        # alphabet: List[str] = ["a","b","c","d","e","f","g","h",'i',"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        # output: str = ""
        # distinct_key = []
        
        # for i in key:
        #     if i != " ":
        #         if i not in distinct_key:
        #             distinct_key.append(i)

        # for j in range(len(alphabet)):
        #     dictionary[distinct_key[j]] = alphabet[j]
        
        # for k in message:
        #     if k == " ":
        #         output += " "
        #     else:
        #         output += dictionary[k]
        # return output

        # Test cases:
        # 1) key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv" -> Returns "this is a secret"
        # 2) key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb" -> Returns "the five boxing wizards jump quickly"
                
        # Runtime = 45ms, beats 33.78% of users
        # Memory = 16.32MB, beats 33.78% of users

        # Improved Approach
        # 1) Initialize a dictionary to store alphabets as value and each distinct iteration of key as its key -> O(n)
        # 2) Initialize output to return secret message
        # 3) Loop through message and append dictionary[iteration] to output. Add a space for each space in message -> O(n)

        dictionary: Dict[str,str] = {}
        alphabet: List[str] = ["a","b","c","d","e","f","g","h",'i',"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        output: str = ""

        temp_counter = 0    
        for i in key:
            if temp_counter == 26:
                break
            if i not in dictionary.keys() and i != " ": #Take note of spaces in key to omit
                dictionary[i] = alphabet[temp_counter]
                temp_counter += 1
        
        for j in message:
            if j == " ":
                output += " "
            else:
                output += dictionary[j]
        return output

        # Runtime = 40ms, beats 66.36% of users
        # Memory = 16.43MB, beats 5.52% of users

