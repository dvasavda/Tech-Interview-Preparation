'''
Day 4


Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""

		# Iterate through nums[] and check for zeros in the array
		i = 0
		end = len(nums)

		# Iterate through array
		while i < end:
			if nums[i] == 0:
				# Delete 0 from that position
				del nums[i]
				# Add 0 to the end
				nums.append(0)
				# Reduce iteration as we have 1 less element when we use del
				end -= 1
			else:
				i += 1


		return nums



test = Solution()
print(test.moveZeroes([0, 1, 0, 3, 12]))