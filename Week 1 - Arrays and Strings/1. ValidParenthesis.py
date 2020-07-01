class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
            Plan:
            Split string in half. We now half string_1 and string_2
            reverse string_2
            Check if string_1 == string_2, then True
            Else false
        '''
        # Open brackets must be closed by same type of bracket
        # Open bracket must be closed in the correct order

        # STACK problem!
        # Create dict where the opposite bracket matches, i.e. ') : ('
        # Use stack to check - if item is in stack:
        #   stack.append()
        # Else if stack is empty or value does not == pop
        # Return false

        bracket_map = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif stack:
                expected_bracket = stack.pop()
                if expected_bracket != char:
                    # Incorrect bracket
                    return False
            else:
                # Empty stack
                return False

        if len(stack) != 0:
            return False

        return True







test = Solution()
print(test.isValid('()'))
print(test.isValid('([])'))
print(test.isValid('([[]])'))
print(test.isValid('([[])')) # False
print(test.isValid('([[{}]')) # False
print(test.isValid('([{}}')) # False