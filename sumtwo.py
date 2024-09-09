class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # Create a hashmap to store the number and its index
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            if complement in hashmap:  # If complement exists in hashmap
                return [hashmap[complement], i]  # Return the indices
            hashmap[num] = i  # Store the current number and its index
