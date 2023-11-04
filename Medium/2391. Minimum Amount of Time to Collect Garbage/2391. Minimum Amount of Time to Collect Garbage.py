class Solution(object):
    def garbageCollection(self, garbage, travel):
        minutes = 0  # Initialize time taken to travel
        travel_minutes_g = 0  # Initialize time taken for glass collecting truck to travel
        travel_minutes_p = 0  # Initialize time taken for paper collecting truck to travel
        travel_minutes_m = 0  # Initialize time taken for metal collecting truck to travel
        travel.insert(0, 0)  # Add the time taken to travel to the first house into the travel duration list
        for i in range(len(garbage) - 1, -1, -1):  # Loop list in reverse
            if 'G' in garbage[i]:  # Since list loops in reverse, the first instance 'G' appears means that the glass collecting truck would have its final stop at the current house
                travel_minutes_g = sum(travel[0:i + 1])  # Stores the time taken to travel from the first house to the current house
                break  # Loop is broken to keep the time taken for glass collecting truck to travel
        for i in range(len(garbage) - 1, -1, -1):  # Loop list in reverse
            if 'P' in garbage[i]:  # Since list loops in reverse, the first instance 'P' appears means that the paper collecting truck would have its final stop at the current house
                travel_minutes_p = sum(travel[0:i + 1])
                break
        for i in range(len(garbage) - 1, -1, -1):  # Loop list in reverse
            if 'M' in garbage[i]:  # Since list loops in reverse, the first instance 'M' appears means that the metal collecting truck would have its final stop at the current house
                travel_minutes_m = sum(travel[0:i + 1])
                break
        minutes += ''.join(garbage).count('G')  # This essentially adds all occurrences where 'G' appears in the list, which would calculate the time taken to collect glass for all houses
        minutes += ''.join(garbage).count('P')  # Same as above but for 'P'
        minutes += ''.join(garbage).count('M')  # Same as above but for 'M'
        output = minutes + travel_minutes_g + travel_minutes_p + travel_minutes_m

        return output

        # """
        # :type garbage: List[str]
        # :type travel: List[int]
        # :rtype: int
        # """
