class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Traverse the digits from the end to the start
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits are 9, the result will be [1, 0, 0, ..., 0]
        return [1] + digits




    





        
        
        


      
