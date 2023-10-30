class Solution(object):
    def finalValueAfterOperations(self, operations):
        X = 0 #Start with initial value of X
        operations_dictionary = { '--X':-1,'X--':-1,'X++':1,'++X':1} #Store all possible operations so that it can be easily accessed

        for operation in operations: #Loop through all elements in the operations list, calling each element (Not index)
            X += operations_dictionary.get(operation) #Since we know that operations will contain one of the key in the operations dictionary, we just need to add the correct value based on the operation done

        return X #Return the value after all operations have been done


        
        """
        :type operations: List[str]
        :rtype: int
        """
