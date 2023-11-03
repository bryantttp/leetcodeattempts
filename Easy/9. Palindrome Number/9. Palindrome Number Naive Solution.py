class Solution(object):
    def isPalindrome(self, x):
        temp = x  # Create a variable to store value of x, so we can manipulate it
        rev_x = 0  # this is the variable that will store the reverse of x
        while temp > 0:  # While loop stops eventually since temp is constantly divided by 10 and has its quotient returned
            rev_x = rev_x * 10  # This is to ensure any previous number added to rev_x is shifted to the next tens/hundreds/thousands etc. place
            rev_x += temp % 10  # This adds the remainder of temp%10 to rev_x, which is essentially just to add the right most digit of temp to rev_x
            temp = temp // 10  # This divides temp by 10 and returns the quotient, which is essentially removing the right most digit from temp
        return x == rev_x

        # """
        # :type x: int
        # :rtype: bool
        # """
