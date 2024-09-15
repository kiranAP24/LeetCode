class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        # Convert the string to lowercase and filter out non-alphanumeric characters
        filtered_string = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string is the same as its reverse
        return filtered_string == filtered_string[::-1]

# Example usage
solution = Solution()
print(solution.isPalindrome(\A man, a plan, a canal: Panama\))  # Output: True
print(solution.isPalindrome(\race a car\))                      # Output: False
print(solution.isPalindrome(\ \))                               # Output: True
