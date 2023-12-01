#011223 Submission
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Approach
        # 1) Initialize dictionary to store sorted list of strings as key and the actual string in a list as value
        # 2) Initialize output to store answer
        # 3) Loop through strs. Check if sorted iteration is in dictionary.keys(). If it is, append iteration to the list. Else, add iteration into dictionary with its sorted value as the key
        # 4) Loop through dictionary and append each value into output
        # 5) Return output
        
        dictionary: Dict[List[str],List[str]] = {}
        output: List[List[str]] = []

        for i in strs:
            temp = "".join(sorted(i))
            if temp in dictionary.keys():
                dictionary[temp].append(i)
            else:
                dictionary[temp] = [i]
        
        for j in dictionary.keys():
            output.append(dictionary[j])
        
        return output

        # Test cases
        # 1) Empty strs
        #    strs = [""] -> Return [[""]]
        # 2) 1 element in strs
        #    strs = ["a"] -> Return [["a"]]
        # 3) Random elements in strs
        #    strs = ["eat","tea","tan","ate","nat","bat"] -> Return [["bat"],["nat","tan"],["ate","eat","tea"]]

        # Runtime = 97ms, beats 68.19% of users
        # Memory = 19.60MB, beats 77.41% of users
