#271123 Submission
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        # Approach
        # 1) Initialize output to store answer
        # 2) Nested Loop. Loop through nums. In each iteration, loop through nums again. If sum of strings = target and i != j, output + 1 -> O(n^2)
        # 3) Return output

        # output: int = 0

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             output += 1

        # return output

        # Test cases
        # 1) nums = ["777","7","77","77"], target = "7777" -> Return 4
        # 2) nums = ["123","4","12","34"], target = "1234" -> Return 2
        # 3) nums = ["1","1","1"], target = 11 -> Return 6

        # Runtime = 66ms, beats 48.39% of users
        # Memory = 16.54MB, beats 6.74% of users
        
