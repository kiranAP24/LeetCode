class Solution(object):
    def romanToInt(self, s):
      self.s=s  
      values = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }

      total_values = 0
      prev_values = 0

      for char in s:
        current_values = values[char]

        if current_values > prev_values:
            total_values += current_values - 2 * prev_values
        else:   
            total_values += values[char]

        prev_values = current_values
        
      return total_values

        