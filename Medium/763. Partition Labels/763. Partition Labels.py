#161123 Submission
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Approach
        # 1) Initialize output to store size of partitions and x to act as a counter to access output
        # 2) While loop for len(s) != sum(output). -> O(n)
        # 3) If output is empty, for loop through s, if iteration == s[0], temp counter = iteration. Check if the iteration is the last iteration in s, if not, check if other iteration from temp counter to len(s) in s using for loop. If so, temp counter = iteration -> O(2n)
        # 4) If output is not empty, for loop through s from sum(output). if s[sum(output)] == s[i], temp counter = i. Check if iteration is last in s, if not, check if other iteration from temp counter to len(s) in s using for loop. If so, temp counter = iteration -> O(2n)
        # 4) Return output

        # output: List[int] = []
        # x: int = 0

        # while len(s) != sum(output):
        #     temp_counter: int = 0
        #     if output == []:
        #         for i in range(len(s)):
        #             if s[0] == s[i]:
        #                 temp_counter = i
        #         if temp_counter+1 != len(s):
        #             for j in range(temp_counter+1,len(s)):
        #                 if s[j] in s[0:temp_counter+1]:
        #                     temp_counter = j
        #         output.append(temp_counter+1)
        #     else:
        #         y = sum(output)
        #         for k in range(y,len(s)):
        #             if s[y] == s[k]:
        #                 temp_counter = k
        #         if temp_counter+1 != len(s):
        #             for l in range(temp_counter+1,len(s)):
        #                 if s[l] in s[output[x]:temp_counter+1]:
        #                     temp_counter = l
        #         output.append(temp_counter+1-sum(output))
        #         x += 1
        
        # return output

        # Test cases
        # 1) No partition
        #    s = "eccbbbbdec" -> Returns [10]
        # 2) 1 partition
        #    s = "aaaaaabbbbbb" -> Returns [6,6]
        # 3) Multiple partitions
        #    s = "ababcbacadefegdehijhklij" -> Returns [9,7,8]

        # Runtime = 80ms, beats 5.10% of users
        # Memory = 16.16MB, beats 71.71% of users


        # Improved Approach
        # 1) Initialize dictionary to store each iteration of s as its key and the index as its value
        # 2) Initialize output to store size of partitions and a counter to store the value of the last index of the particular iteration
        # 3) Loop through s. counter =  max(dictionary[i],counter). if counter == i, output.append(i+1-sum(output)). -> O(n)
        # 4) Return output
        
        dictionary_last_index: dict[str,int] = {}
        output: List[int] = []
        counter: int = 0

        for i in range(len(s)):
            dictionary_last_index[s[i]] = i
        
        # OR you can use
        # for i, j in enumerate(s):
        #     dictionary_last_index[j] = i

        for j in range(len(s)):
            counter = max(dictionary_last_index[s[j]],counter)
            if counter == j:
                output.append(j+1-sum(output))

        return output

        # Runtime = 38ms, beats 91.91% of users
        # Memory = 16.42MB, beats 8.07% of users


            


        
