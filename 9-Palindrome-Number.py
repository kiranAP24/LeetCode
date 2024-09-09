class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        num = str(x)  # Convert the number to a string
        rev = num[::-1]  # Reverse the string using slicing
        
        # Return True if palindrome, False otherwise
        return rev == num
