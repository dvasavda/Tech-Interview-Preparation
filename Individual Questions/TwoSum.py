class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Iterate through array
        # Take each index (x) and subtract it by target
        # Search for remainder (y) in array
        # Return x and y
        # Example input: [2, 7, 11, 15], target = 9

        # *in* operator = O(n)
        # .index() call = O(n)

        for i, x in enumerate(nums):
            if (target - x) in nums:
                value = target - x
                return (i, nums.index(value))






t = Solution()
print(t.twoSum([3, 2, 4], 6))
