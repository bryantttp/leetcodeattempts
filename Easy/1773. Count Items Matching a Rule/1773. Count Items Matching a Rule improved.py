class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):

        temp_dict = {'type': 0, 'color': 1, 'name': 2}  # Create dictionary with the index matched to items[i]

        index = temp_dict[ruleKey]  # Match index with the ruleKey

        output = 0  # Initialize the output

        for i in items:
            if i[index] == ruleValue:  # Check if string in ruleKey's index matches the ruleValue
                output += 1

        return output
        # """
        # :type items: List[List[str]]
        # :type ruleKey: str
        # :type ruleValue: str
        # :rtype: int
        # """
