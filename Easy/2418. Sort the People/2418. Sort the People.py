# 111123 Submission
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # Approach
        # 1) Initialize list to store output
        # 2) Store heights in a dictionary with its element as the key and its index as its value -> O(n)
        # 3) Loop through the dictionary keys and find the highest value, using its dictionary value to add the element in names with the same index into the output list. Remove that key from the dictionary -> O(n)
        # 4) Return output list

        # output: List[str] = []
        # dictionary: dict[int,int] = {}
        # for i in range(len(heights)):
        #     dictionary[heights[i]] = i

        # loop = len(dictionary.keys())
        # for j in range(loop):
        #     temp_key = max(dictionary.keys())
        #     output.append(names[dictionary.get(temp_key)])
        #     dictionary.pop(temp_key)
        # return output

        # Test case
        # 1) One name
        #    names = ["John"], heights = [170] -> Return ["John"]
        # 2) All different names
        #    names = ["John","Mary","Tom"], heights = [170,165,171] -> Returns ["Tom","John","Mary"]
        # 3) Some similar names
        #    names = ["Alice","Bob","Bob"], heights = [155,185,150] -> Returns ["Bob","Alice","Bob"]

        # Runtime = 195ms, beats 14.36% of users
        # Memory = 16.74MB, beats 73.36% of users

        # Improved Approach
        # 1) If len(words) == 1, return words. Otherwise, continue with code
        # 2) Initialize list to store output
        # 3) Store heights in a dictionary with its element as the key and the corresponding name in names as its value -> O(n)
        # 4) Sort heights in descending order and loop through the list. For each height in dictionary, append its value (name) to the list
        # 5) Return output list

        output: List[str] = []
        dictionary: dict[int,int] = {}
        for i in range(len(heights)):
            dictionary[heights[i]] = names[i]

        heights.sort(reverse=True)
        
        for j in heights:
            output.append(dictionary.get(j))
        return output

        # Runtime = 109 ms, beats 85.28% of users
        # Memory = 16.76MB, beats 73.36% of users
