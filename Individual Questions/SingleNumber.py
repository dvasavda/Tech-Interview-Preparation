"""
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution(object):
    def singleNumber(self, nums):
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