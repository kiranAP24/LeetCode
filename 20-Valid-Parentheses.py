class Solution(object):
    def isValid(self, s):
      
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to hold mappings of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to hold opening brackets
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top of the stack if it's not empty
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched properly
        return not stack
