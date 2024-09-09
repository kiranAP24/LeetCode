class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]#assume the first string of the array be prefix

        for string in strs[1:]:#iternate through the array starting from 1st string
            while string[:len(prefix)] != prefix:#compare the length of the strings 
                 prefix = prefix[:-1]
                 
                 if not prefix:
                    return ""
        return prefix

    

        