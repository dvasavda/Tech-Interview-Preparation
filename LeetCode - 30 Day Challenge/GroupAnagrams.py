'''
Day 6



Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # We can use a dict
        dict = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in dict:
                dict[key] = [word]
            else:
                dict[key] += [word]

        return dict.values()

# Algorithm analysis
# O(n log n) for the use of Timsort-like sorted())
# O(1) average case for dict insert
# O(n) average case for dict iteration
# The average case of this program is o(n log n) as we are bottlenecked by sorted(word)

test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))