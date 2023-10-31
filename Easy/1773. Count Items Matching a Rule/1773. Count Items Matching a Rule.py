class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):

        output = 0  # Initialize the output

        if ruleKey == 'type':
            for i in items:
                if ruleValue == i[0]:  # Checks first element in list, which is the type
                    output += 1
        elif ruleKey == 'color':
            for i in items:
                if ruleValue == i[1]:  # Checks second element in list, which is the color
                    output += 1
        else:  # ruleKey can only be 3 strings according to question, so else can be used here
            for i in items:
                if ruleValue == i[2]:  # Checks third element in list, which is the name
                    output += 1

        return output

        # """
        # :type items: List[List[str]]
        # :type ruleKey: str
        # :type ruleValue: str
        # :rtype: int
        # """