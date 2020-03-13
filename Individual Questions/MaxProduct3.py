class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Find the maximum product of 3 integers
        # The first thought in my head is - sort the array
        # Sort the list in ascending order and combine the last 3 digits to fnd the product
        # return

        # Possible Problem: sorting could be too taxing. The faster sorting algorithm to
        #   use here is quicksort, at O(n log n)

        # Python's sort() method runs at O(n log n), which is fine too
        # This could also be a problem in case an interviewer is not OK with it
        
        # Sort the nums
        nums.sort()
        
        # Save the size of the array
        n = len(nums)

        # Take the last n, n-1, n-2 items and multiply them
        product1 = nums[n-1]
        product2 = nums[n-2]
        product3 = nums[n-3]

        

        return product1 * product2 * product3

        # Analysis
        # Sorting takes nlog(n) from Python Sort() method
        # Space takes log(n) from Python sort() method