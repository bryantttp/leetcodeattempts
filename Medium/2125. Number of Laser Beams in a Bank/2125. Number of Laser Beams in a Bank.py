#151123 Submission
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        # Approach
        # 1) Initialize output to count no. of beams and list to store no. of cameras in each row
        # 2) Loop through bank. If "1" in bank[i], count no. of "1" and append to list -> O(n^2)
        # 3) Loop through list from 0 to len(list) - 1. For each iteration, output += i*(i+1) -> O(n)
        # 4) Return output

        # output: int = 0
        # no_of_cameras: List[int] = []
        # for i in bank:
        #     if "1" in i:
        #         no_of_cameras.append(i.count("1"))
        
        # if len(no_of_cameras) == 1:
        #     return output

        # for j in range(len(no_of_cameras)-1):
        #     output += no_of_cameras[j]*no_of_cameras[j+1]

        # return output

        # Test cases
        # 1) No beams
        #    bank = ["0000","1000"] -> Returns 0
        #    bank = ["000","000","111"] -> Returns 0
        #    bank = ["111111"] -> Returns 0
        # 2) Some beams
        #    bank = ["011001","000000","010100","001000"] -> Returns 8
        #    bank = ["11111","00001","11000"] -> Returns 7

        # Runtime = 99ms, beats 63.61% of users
        # Memory = 18.84MB, beats 9.49% of users

        # Improved Approach
        # 1) Initalize output to count no. of laser beams and previous to store count of cameras in previous row that isnt blocked by other cameras
        # 2) Loop through bank from 0 to len(bank) - 1. Initialize temp_count to store the current iteration's no. of cameras. If previous != 0 and temp_count != 0, output += previous*temp_count. If temp_count != 0, previous = temp_count -> O(n^2)
        # 43) Return output

        output: int = 0
        previous: int = 0
        for i in bank:
            temp_count = i.count("1")
            if previous != 0 and temp_count != 0:
                output += temp_count*previous
            if temp_count != 0:
                previous = temp_count
        return output

        # Runtime = 86ms, beats 95.10% of users
        # Memory = 18.46MB, beats 36.87% of users

