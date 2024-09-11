class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        char = 0 
        
        for i in range(1,len(nums)):
           
            if nums[i]!= nums[char]:
                char += 1
                nums[char] = nums[i]

        return char+1
            
                
            
                
            
        return len(dummy)

                
        