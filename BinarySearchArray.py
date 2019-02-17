def binarySearchSortedArray(nums, s):
    """
    Args:
    {List<int>} nums
    {int} s
    Returns:
    {boolean} Whether s is in nums.
    """
    # Write your code here.
    beginning = 0
    end = len(nums) - 1
    found = False

    while beginning <= end and not found:
        mid = (beginning + end) // 2
        if nums[mid] == s:
            found = True 
        else:
            if s <= nums[mid]:
                end = mid - 1
            if s >= nums[mid]:
                beginning = mid + 1
								
    return found