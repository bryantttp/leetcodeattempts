class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m: list = []  # Initialize list to record the no. of instructions the robot can execute
        for i in range(len(s)):  # Loop through each instruction in s
            temp_m: int = 0  # Initialize a temp counter to count no. of instructions that can be executed
            temp_pos: List[int] = startPos[:]  # Initialize a temp position to go through the executed instructions. Rmb to use [:] to do a full slice as using temp_pos = startPos will not reset temp_pos in each i loop
            for j in range(i, len(s)):  # This is to count from the beginning of the ith instruction
                if s[j] == 'U' and temp_pos[0] - 1 < 0:  # Up execution moves along row axis, so ensure it does not go out of bounds
                    break  # If out of bounds, breaks out of loop
                elif s[j] == 'D' and temp_pos[0] + 1 >= n:  # Down execution moves along row axis, so ensure it does not go out of bounds
                    break  # If out of bounds, breaks out of loop
                elif s[j] == 'L' and temp_pos[1] - 1 < 0:  # Left execution moves along column axis, so ensure it does not go out of bounds
                    break  # If out of bounds, breaks out of loop
                elif s[j] == 'R' and temp_pos[1] + 1 >= n:  # Right execution moves along column axis, so ensure it does not go out of bounds
                    break  # If out of bounds, breaks out of loop
                elif s[j] == 'U':  # Here, the instruction executed would not cause the robot to go out of bounds, so the 4 elif functions are here to ensure the temp_pos is moving accordingly to the instructions executed
                    temp_pos[0] -= 1
                elif s[j] == 'D':
                    temp_pos[0] += 1
                elif s[j] == 'L':
                    temp_pos[1] -= 1
                elif s[j] == 'R':
                    temp_pos[1] += 1
                temp_m += 1  # Adding 1 to the temp counter to count the executed instruction in this loop
            m.append(temp_m)  # Once loop has been completed for the ith instruction, the total no. of instructions that can be executed (temp_m) will be added to m

        return m

        # """
        # :type n: int
        # :type startPos: List[int]
        # :type s: str
        # :rtype: List[int]
        # """
