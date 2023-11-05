class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
    # Approach:
    # 1) Create an empty list with length of s -> Worst Time complexity = O(1)
    # 2) Loop through indices and add letter from s into the empty list, using indices[i] as its index -> Worst Time complexity = O(n)
    # 3) Return list using .join function -> Worst Time complexity = O(n)

    # Total Worst Time Complexity -> O(2n) = O(n)

    # Test Case:
    # 1) Duplicates in string: s = 'heyheyhey', indices = [0,1,2,6,8,7,4,3,5]
    # -> return 'heyehyhye'
    # 2) Empty string: s = '', indices = []
    # -> return ''

    # Improved Approach:
    # 1) Create an empty list with length of s -> Worst Time complexity = O(1)
    # 2) If s is empty, return empty list 
    # 2) Loop through s and add letter s[i] into the empty list, using indices[i] as its index -> Worst Time complexity = O(n)
    # 3) Return list using .join function

   
        output = ['']*len(s)
        if len(s) == 0:
            return ''.join(output)

        for i in range(len(s)):
            output[indices[i]] = s[i] 
        return ''.join(output)
