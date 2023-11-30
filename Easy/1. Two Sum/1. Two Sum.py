#301123 Submission
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Approach
        # 1) Initialize output to store answer
        # 2) Loop through nums. If difference between iteration and target is in nums, store index of iteration in output and loop through nums to find the difference and store its index -> O(n^2)
        # 3) Return output

        # output: List[int] = []

        # for i in range(len(nums)):
        #     if len(output) == 2:
        #         break
        #     difference = target - nums[i]
        #     if difference in nums:
        #         for j in range(len(nums)):
        #             if nums[j] == difference and i != j:
        #                 output.append(i)
        #                 output.append(j)
    
        
        # return output

        # Test cases
        # 1) nums = [2,7,11,15], target = 9 -> Returns [0,1]
        # 2) nums = [1,2,3,5], target = 6 -> Returns [0,4]
        # 3) nums = [3,3], target = 6 -> Returns [0,1]
        
        # Runtime = 552ms, beats 37.71% of users
        # Memory = 17.12MB, beats 66.21% of users

        # Improved Approach
        # 1) Initialize output to store answer
        # 2) Initialize dictionary to store difference between target and iteration as key and the iteration as the value.
        # 3) Loop through nums. Check if iteration is in values of dictionary. If it is, add [dictionary[iteration],iteration] to output. Else, add the iteration into the dictionary accordingly -> O(n)
        # 4) Return output

        output: List[int] = []
        dictionary: Dict[int,int] = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in dictionary.keys():
                output.append(dictionary[nums[i]])
                output.append(i)
            else:
                dictionary[difference] = i
        
        return output

        # Runtime = 57ms, beats 92.36% of users
        # Memory = 17.92MB, beats 6.60% of users
