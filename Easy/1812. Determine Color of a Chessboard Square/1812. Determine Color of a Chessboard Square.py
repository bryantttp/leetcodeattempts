#201223 Submission
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        # Approach
        # 1) If first iteration is a,c,e and g and 2nd iteration is 1,3,5 or 7, return false. If first iteration is b,d,f,h and 2nd iteration is 2,4,6,8, return false. Else, return true

        if coordinates[0] == "a" or coordinates[0] == "c" or coordinates[0] == "e" or coordinates[0] == "g":
            if coordinates[1] == "1" or coordinates[1] == "3" or coordinates[1] == "5" or coordinates[1] == "7":
                return False
        if coordinates[0] == "b" or coordinates[0] == "d" or coordinates[0] == "f" or coordinates[0] == "h":
            if coordinates[1] == "2" or coordinates[1] == "4" or coordinates[1] == "6" or coordinates[1] == "8":
                return False
        return True

        # Test cases:
        # 1) False test
        #    coordinates = "a1" -> Returns False
        # 2) True test
        #    coordinates = "a2" -> Returns True

        # Runtime = 29ms, beats 95.49% of users
        # Memory = 17.30MB, beats 11.75% of users

        
