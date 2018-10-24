# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.

 
# Follow up:
# Could you solve it using only O(1) extra space?

 
# Example 1:

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 0
        results = []
        old = ""
        for char in chars:
            if char == old:
                count += 1
            else:
                if count != 0:
                    if count == 1:
                        results += [old]
                    else:
                        new_count = [digit for digit in str(count)]
                        results += [old] + new_count
                old = char
                count = 1
        if count != 0:
            if count == 1:
                results += [old]
            else:
                new_count = [digit for digit in str(count)]
                results += [old] + new_count
        del chars[:]
        for result in results:
            chars.append(result)
            