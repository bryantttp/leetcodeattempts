class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x > 0 and x % 10 == 0):  # This is to capture the cases that x is negative or has a 0 at the back (there is no number that starts with 0)
            return False
        rev_x = 0  # Initialize the reversed ver. of x
        while x > rev_x:  # If a number is a palindrome, the numbers are a mirror image of each other within the number (In 123321, 123 is a mirror form of 321). While loop breaks when it reaches the middle of the number, which means that x has been split into 2 mirrored numbers. All while this is happening, x now contains one side of the numbers while rev_x contains the REVERSED version of the mirrored number in x
            rev_x = rev_x * 10  # This is to ensure any previous number added to rev_x is shifted to the next tens/hundreds/thousands etc. place
            rev_x += x % 10  # This adds the remainder of x%10 to rev_x, which is essentially just to add the right most digit of x to rev_x
            x = x // 10  # This divides x by 10 and returns the quotient, which is essentially removing the right most digit from x

        if x == rev_x or x == rev_x // 10:  # If the number is a palindrome, x and rev_x are would be the same. If the number is odd-numbered, this would mean that rev_x has 1 more digit than x. The 2nd condition helps by removing the 'middle' number, essentially making x and rev_x the same AGAIN, if the number is a palindrome
            return True
        else:
            return False

        # """
        # :type x: int
        # :rtype: bool
        # """
