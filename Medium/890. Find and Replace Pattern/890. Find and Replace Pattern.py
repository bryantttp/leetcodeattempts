#191123 Submission
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        # Approach
        # 1) Initialize a list to store list of words that match the pattern
        # 2) Loop through words. If length of set(iteration) == len(set(pattern)), loop through set(words[i]) to check if words[i].count(j) not equal to pattern.count(j). Initialize a temporary counter to determine if word is added to list. If values are not equal, temp counter = 1. If temp counter = 0, append the iteration of word into the list -> O(n^2)

        # output: List[str] = []

        # for i in words:
        #     if len(set(pattern)) == len(set(i)):
        #         temp_counter: int = 0
        #         for j in range(len(i)):
        #             if i.count(i[j]) != pattern.count(pattern[j]):
        #                 temp_counter = 1
        #                 break
        #         if temp_counter == 0:
        #             output.append(j)
    
        # return output

        # Test cases
        # 1) No similar permutation
        #    words = ["abb","def","ghg"], pattern = "zzy" -> Return []
        # 2) All similar permutation
        #    words = ["aaa","bbb","ccc"], pattern = "aaa" -> Return ["a","b","c"]
        # 3) Some similar permutation
        #    words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb" -> Returns ["mee","aqq"]

        # Failed Testcase
        # words = ["badc","abab","dddd","dede","yyxx"], pattern = "baba" -> Returned ["abab","dede","yyxx"] but supposed to be ["abab","dede"]
        
        # Improved Solution
        # 1) Initialize a list to store list of words that match the pattern
        # 2) Create dictionary to check for the unique characters in pattern by allocating a number (BASED ON LENGTH OF DICTIONARY since it is increasing as you add more things into the dictionary) to each character -> O(1)
        # 4) Loop through words and create temporary dictionary to convert the iteration into numbered form. Check if numbered form of pattern == numbered form of word. If equal, add to list. -> O(n^2)

        output: List[str] = []
        dictionary: Dict[str,str] = {} 

        for i in pattern:
            if i not in dictionary.keys():
                dictionary[i] = str(len(dictionary))

        for j in words:
            temp_dict: Dict[str,str] = {}
            for k in j:
                if k not in temp_dict.keys():
                    temp_dict[k] = str(len(temp_dict))
            if list(map(temp_dict.get,j)) == list(map(dictionary.get,pattern)): # Checking if index of each character in pattern/j uses the same number as the other 
                output.append(j)
        return output

        # Runtime = 46ms, beats 24.12% of users
        # Memory = 16.40MB, beats 16.19% of users
