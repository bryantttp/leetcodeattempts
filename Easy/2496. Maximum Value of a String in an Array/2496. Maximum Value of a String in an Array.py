#151123 Submission
class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        # Approach
        # 1) Initialize a list to store all alphabets
        # 2) Create a dictionary to store the string as the key and its value as the key's value. While looping through to add the string into the dictionary, check if the string has any alphabets, if so, return the string's length as its value. Otherwise, convert the string to int and store its max value as the key's value -> O(n)
        # 3) Return the max value of the dictionary values -> O(n)

        # alphabet: List[str] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
        # dictionary: dict[str,int] = {}

        # for i in strs:
        #     if i not in dictionary.keys():
        #         if i not in alphabet:
        #             dictionary[i] = int(max(i))
        #         else:
        #             dictionary[i] = len(i)
        # return max(dictionary.values())

        # Test cases (Error: line 14 does not actually check if i has any alphabets in it):
        # 1) Duplicate strings
        #    strs = ["bob","bob","02"] -> Return 3
        # 2) All strings have no numbers
        #    strs = ["bob","anna","dave"] -> Return 4
        # 3) All strings have no alphabets
        #    strs = ["00000","012","9"] -> Return 9
        # 4) Mix of strings and alphabets
        #    strs = ["alic3","bob","3","4","00000"] -> Return 5

        # Corrected approach
        # 1) Create a dictionary to store the string as the key and its value as the key's value. While looping through to add the string into the dictionary, check if converting the iteration has a ValueError, if so, return the string's length as its value. Otherwise, convert the string to int and store the key's value -> O(n)
        # 2) Return the max value of the dictionary values -> O(n)

        # dictionary: dict[str,int] = {}

        # for i in strs:
        #     if i not in dictionary.keys():
        #         try:
        #             dictionary[i] = int(i)
        #         except ValueError:    
        #             dictionary[i] = len(i)
        # return max(dictionary.values())

        # Runtime = 46ms, beats 19.81% of users
        # Memory = 16.34MB, beats 6.04% of users

        # Improved Approach (O(n) instead of O(2n))
        # 1) Initialize a variable to store highest value
        # 2) Initialize a temporary value and loop through strs. If i only contains digits, value = int(i). Else, value = len(i).
        # 3) If value > counter, counter = value -> O(n)
        # 4) Return value
        
        store: int = 0
        for i in strs:
            temp_value: int = 0
            if i.isdigit():
                temp_value = int(i)
            else:
                temp_value = len(i)
            if temp_value > store:
                store = temp_value
        return store

        # Runtime = 33ms, beats 94.20% of users
        # Memory = 16.30MB, beats 6.04% of users

