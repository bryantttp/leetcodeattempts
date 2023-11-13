#131123 Submission
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        # Approach
        # 1) Initialize output to store the no. of columns to delete
        # 2) Use nested loop to loop through the ith element in each string to check if column is sorted lexicographically. If ACSII value of current iteration is greater than the next iteration, output + 1. If the iteration is the last element, break and loop through the next colunmn -> O(n^2)
        # 2) Return output

        # output: int = 0
        # for i in range(len(strs[0])):
        #     for j in range(0,len(strs)-1):
        #         if ord(strs[j][i]) > ord(strs[j+1][i]):
        #             output += 1
        #             break
        # return output

        # Test cases (All passed)
        # 1) None are sorted lexicographically
        #    strs = ["xyz","ccc","ddd"] -> Returns 3
        #    strs = ["aaa","ccc","ddd"] -> Returns 3
        # 2) All are sorted lexicographically
        #    strs = ["aaa","bbb","ccc"] -> Returns 0
        #    strs = ["fff","jjj","kkk"] -> Returns 0
        # 3) Some are sorted lexicographically
        #    strs = ["cba","daf","ghi"] -> Returns 1
        #    strs = ["zxa","ywb","chc"] -> Returns 2

        # Runtime = 155ms, beats 26.20% of users
        # Memory = 17.03MB, beats 38.45% of users

        # Improved Approach
        # 1) Initialize output to count no. of columns to be deleted
        # 2) Use zip function to rearrange list based on columns -> O(n)
        # 3) Loop through new list to check if each element is equal to its sorted counterpart. If not equal, output + 1. -> O(n)
        # 4) Return output

        output: int = 0
        new_strs: List[str] = list(map(list,zip(*strs)))

        for i in new_strs:
            temp_list = sorted(i)
            if i != temp_list:
                output += 1
        return output

        # Runtime = 77ms, beats 98.87% of users
        # Memory = 17.33MB, beats 11.41% of users
       
