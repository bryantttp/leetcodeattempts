#121223 Submission
class Solution:
    def countPoints(self, rings: str) -> int:

        # Approach
        # 1) Initialize dictionary to store rod as key and rings as value -> O(n)
        # 2) Initialize output to store answer
        # 3) Loop through dictionary.keys(). If len(set(dictionary[key])) == 3, output += 1
        # 4) Return output
        
        dictionary: Dict[int,List[str]] = {}
        output: int = 0

        for i in range(1,len(rings),2):
            if rings[i] not in dictionary.keys():
                dictionary[rings[i]] = [rings[i-1]]
            else:
                dictionary[rings[i]].append(rings[i-1])
        
        for j in dictionary.keys():
            if len(set(dictionary[j])) == 3:
                output += 1
        return output

        # Test cases
        # 1) No rods with all 3 colors
        #    rings = "B0B1B2" -> Returns 0
        # 2) 1 rod with all 3 colors
        #    rings = "B0B6G0R6R0R6G9" -> Returns 1
        # 3) Multiple rods with all 3 colors
        #    rings = "R1B1G1R2B2G2" -> Returns 2

        # Runtime = 37ms, beats 66.42% of users
        # Memory = 16.35MB, beats 14.63% of users
