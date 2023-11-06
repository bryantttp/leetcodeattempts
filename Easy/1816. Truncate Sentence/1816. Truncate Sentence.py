class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

    # Approach
    # 1) Count number of spaces in the string -> Worst Time Complexity : O(n)
    # 2) Loop through string to find the kth space and print from start to the kth space -> Worst Time Complexity : O(n)

    # Total time complexity = O(2n) = O(n)

    # Test cases
    # 1) s = 'Hi how are you', k = 2 -> return 'Hi how'
    # 2) s = 'a', k = 1 -> return 'a'
    
    # Improved Approach
    # 1) Count number of spaces in the string -> Worst Time Complexity : O(n)   
    # 2) If k - 1 = no. of spaces, return the string, otherwise, the for function will return NULL since the last space does not exist
    # 3) Loop through string to find the kth space and print from start to the kth space -> Worst Time Complexity : O(n)
    
        count: int = 0
        if k - 1 == s.count(' '):
            return s
        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
                if count == k:
                    return s[0:i]


        
