class Solution(object):
    def removeElement(self, nums, val):
        # Pointer for placing elements that are not equal to val
        k = 0
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Assign the current element to the k-th position
                nums[k] = nums[i]
                # Move the pointer k forward
                k += 1
        
        # Return the number of elements not equal to val
        return k
