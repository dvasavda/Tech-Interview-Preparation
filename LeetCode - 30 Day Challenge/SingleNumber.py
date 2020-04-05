'''
Day 1

Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1


Example 2:

Input: [4,1,2,1,2]
Output: 4

'''

# This file includes two solutions
# First one uses extra space, the other one uses no extra space

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        # Extra space solution
        # Time and space complexity O(n). Better than that is O(logn), then O(1)
        # Traverse nums:
        #   insert elements and counts in hash table
        # Traverse array again:
        #   return first element with count == 1

        counter_dict = defaultdict(lambda: 0)

        # Insert all elements into hash table
        for num in range(len(nums)):
            counter_dict[nums[num]] += 1

        # Traverse array again
        # Return element with count 1
        for num in range(len(nums)):
            if counter_dict[nums[num]] == 1:
                return nums[num]

        return 0

    def singleNumberXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using XOR Bitwise solution
        # Syntax: x ^ y, where ^ is the XOR operator
        # O(n) runtime, no extra space used O(1)
        #
        # Traverse the nums:
        #   Counter will XOR with index of array
        # return counter

        counter = 0

        for num in range(len(nums)):
            counter ^= nums[num]

        return counter





# Dict solution test cases
test = Solution()
print(test.singleNumber([2, 2, 1])) # output 1
print(test.singleNumber([2, 1, 2])) # output 1
print(test.singleNumber([4, 1, 2, 1, 2])) # output 4

print('\n')

# XOR solution test cases
print(test.singleNumberXOR([2, 2, 1])) # output 1
print(test.singleNumberXOR([2, 1, 2])) # output 1
print(test.singleNumberXOR([4, 1, 2, 1, 2])) # output 4