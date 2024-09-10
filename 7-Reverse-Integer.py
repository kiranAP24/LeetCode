class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Determine if the number is negative
        sign = -1 if x < 0 else 1
        
        # Reverse the absolute value of the integer
        reversed_num = int(str(abs(x))[::-1])
        
        # Apply the original sign
        reversed_num *= sign
        
        # Handle overflow: if the number is outside the 32-bit signed integer range
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
