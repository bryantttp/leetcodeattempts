#211123 Submission
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        # Approach
        # 1) Use replace function to replace . with [.] -> O(n)

        return address.replace(".","[.]")

        # Runtime = 37ms, beats 59.20% of users
        # Memory = 16.43MB, beats 24.43% of users
