#161123 Submission
class Solution:
    def partitionString(self, s: str) -> int:
        
        # Approach
        # 1) Initialize empty list to store strings
        # 2) Loop through s and initialize a temporary variable to store strings. For each iteration of s, if iteration not in temp variable, add iteration into variable. If it is, append the variable into the list and reset the list.
        # 3) Return length of list

        output: List[str] = []
        temp: str = ""
        for i in s:
            if i not in temp:
                temp += i
            else:
                output.append(temp)
                temp = i
        output.append(temp)
        return len(output)
        
        # Test cases
        # 1) No Partition
        #    s = "abcdefg" -> Returns 1
        # 2) 1 Partition
        #    s = "abcdeafghi" -> Returns 2
        # 3) Multiple Partitions
        #    s = "abacaba" -> Returns 4

        # Runtime = 83ms, beats 91.90% of users
        # Memory = 18.99MB, beats 5.58% of users
