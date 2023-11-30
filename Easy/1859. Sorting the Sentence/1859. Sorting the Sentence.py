#301123 Submission
class Solution:
    def sortSentence(self, s: str) -> str:
        
        # Approach
        # 1) Initialize dictionary to store position as its key and remaining string as the value -> O(n)
        # 2) Initialize output to store answer
        # 3) Loop through dictionary and add to output -> O(n)

        dictionary: Dict[str:str] = {}
        output: str = ""
        for i in s.split():
            dictionary[i[-1]] = i[:len(i)-1]
        
        for j in range(len(dictionary)):
            if str(j+1) in dictionary.keys():
                output += dictionary[str(j+1)]
                output += " "
        output = output[:-1] # Removes the last extra space
        return output
        
        # Test cases
        # 1) s = "is2 sentence4 This1 a3" -> Returns "This is a sentence"
        # 2) s = "Myself2 Me1 I4 and3" -> Returns "Me Myself and I"

        # Runtime = 37ms, beats 63.96% of users
        # Memory = 16.20MB, beats 77.37% of users
        
