# -*- coding: utf-8 -*-

"""
Using GeeksForGeeks to Prepare
https://www.geeksforgeeks.org/python-programming-examples/


Class Template:

#
class Number(object):
    def run(self):
        '''

        '''

        return




Divider Template:


############################################
# Lists
############################################

"""


# Add two numbers
class NumberOne(object):
    def run(self, num1, num2):
        sum = num1 + num2
        return sum


# Factorial of a number
class NumberTwo(object):
    def run(self, number):
        # Factorial of 1 or 0  =  1
        if (number == 1 or number == 0):
            return 1
        else:
            return number * self.run(number - 1)


# Simple interest
class NumberThree(object):
    def run(self, p, t, r):
        # Where p = princple
        #       t = time
        #       r = rate

        return (p * t * r)/100

# Compound Interest
class NumberFour(object):
    def run(self, principle, rate, time):
        compound_interest = principle * (1 + rate/100)
        return compound_interest


# Check area of circle
class NumberSix(object):
    import math

    def run(self, r):
        return math.pi * (r * r)


# Print all Prime numbers in interval
class NumberSeven(object):
    def run(self, start, end):

        for value in range(start, end + 1):
            # If number is divisible between 2 and value, it is not prime
            if value > 1:
                for n in range(2, value):
                    if (value % n) == 0:
                        break
                    else:
                        return value
        return


# Check if number is prime
class NumberEight(object):
    def run(self, n):

        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            else:
                return True
        else:
            return False

        return


# Check for n-th Fibonacci number
# we can use recursion
class NumberNine(object):
    def run(self, number):
        if number < 0:
            print('Bad input.')
        # First Fibonacci number is 0
        elif number  == 1:
            return 0
        # Second Fibonacci number is 1
        elif number == 2:
            return 1
        else:
            return self.run(number - 1)+self.run(number - 2)




############################################
# Arrays
############################################

# Rotate array
class LeetcodeRotateArray(object):
    def rotate(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        '''

        temp_arr = nums[0]
        arr_size = len(nums)

        for i in range(arr_size):
            nums[i] = nums[i + 1]
        nums[n+1] = temp_arr



# Find the sum of array
class ArrayNumberOne(object):
    def run(self, arr):
        return sum(arr)


# Find the largest element of array
class ArrayNumberTwo(object):
    def run(self, arr):
        return max(arr)


# Rotate an array (not in-place)
class ArrayNumberThree(object):
    def run(self, arr, d):
        '''
        leftRotate(arr[], d, n)
        start
        For i = 0 to i < d
            Left rotate all elements of arr[] by one
        end
        '''

        # for i in range(d):
        #     temp.append(arr[i])
        #     arr.pop(i)
        #     arr.append(temp[i])

        #     print('i = ', i)
        #     print('Temp = ', temp)

        # print('Temp = ', temp)
        # return arr

        n = len(arr)

        for i in range(d):
            for j in range(1):
                a = arr[0]
                print('a = ', a)
                arr.pop(0)
                print('arr pop = ', arr)
                arr.append(a)
                print('arr append = ', arr)

        return arr


# Split the array and add first part to the end (out of place)
class ArrayNumberFive(object):
    import math

    def run(self, arr, k):
        '''
        Input : arr[] = {12, 10, 5, 6, 52, 36}
            k = 2
        Output : arr[] = {5, 6, 52, 36, 12, 10}
        Explanation : Split from index 2 and first
        part {12, 10} add to the end .

        Input : arr[] = {3, 1, 2}
                k = 1
        Output : arr[] = {1, 2, 3}
        Explanation : Split from index 1 and first
        part add to the end.

        '''
        n = len(arr)
        split_arr = []

        for i in range(0, k):
            split_arr.append(arr[0])
            arr.pop(0)

        arr += split_arr

        return arr

# Find remainder of array multiplication divided by n
class ArrayNumberSix(object):
    def run(self, arr, n):
        '''
        Given multiple numbers and a number n, the task is to print the
        remainder after multiply all the number divide by n.

        Examples:

        Input : arr[] = {100, 10, 5, 25, 35, 14},
                    n = 11
        Output : 9
        100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9
        '''

        # Multiply each number in array
        # then take number % n
        # return result

        result = 1

        for i in range(len(arr)):
            result *= arr[i] # multiply each element by the next

        # Take remainder
        result = result % n

        return result




############################################
# Lists
############################################

# Swap first and last element of a list
class ListNumberOne(object):
    def run(self, list):
        """
        Given a list, write a Python program to swap
        first and last element of the list.

        Examples:

        Input : [12, 35, 9, 56, 24]
        Output : [24, 35, 9, 56, 12]

        Input : [1, 2, 3]
        Output : [3, 2, 1]
        """
        # Store the first item in a variable
        first_item = list[0]

        # Set first item = last
        # list[-1] means to count backwards - so get the last index
        list[0] = list[-1]

        # Set last item = first_item variable
        list[-1] = first_item

        return list


# Swap two elements in a list
class ListNumberTwo(object):
    def run(self, list, pos1, pos2):
        '''
        Given a list in Python and provided the positions
        of the elements, write a program to swap the two elements in the list.

        Examples:

        Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
        Output : [19, 65, 23, 90]

        Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
        Output : [1, 5, 3, 4, 2]
        '''
        first_list_pos = pos1 - 1
        second_list_pos = pos2 - 1

        list[first_list_pos], list[second_list_pos] = list[second_list_pos], list[first_list_pos]

        return list

# Remove nth occurance of given word
# Incomplete
class ListNumberThree(object):
    def run(self, list, word, n):
        '''
        Given a list of words in Python, the task is to remove
        the Nth occurrence of the given word in that list.

        Examples:

        Input: list - ["geeks", "for", "geeks"]
            word = geeks, N = 2
        Output: list - ["geeks", "for"]

        Input: list - ["can", "you",  "can", "a", "can" "?"]
            word = can, N = 1
        Output: list - ["you",  "can", "a", "can" "?"]
        '''
        count = 0
        flag = 1

        for i in range(len(list) - 1):
            while(flag):
                if list[i] == word:
                    print(count)
                    print(list[i])
                    count += 1
                    print(count)
                    if count == n:
                        list.pop(i)
                        print(i)
                        flag = 0


        return list

# Practicing Python Utility functions
class ListNumber4thru9(object):
    def run(self):
        test_list = [ 1, 6, 3, 5, 3, 4 ]


        # Get the length of a list
        a = len(test_list)
        print('Length of list', a)


        # Check if element exists in list
        if 4 in test_list:
            print('element 4 is in test list')
        if 9 not in test_list:
            print('element 9 is not in test list')
        if 'a' in [1, 2, 3, 'a']:
            print('a is in list')


        # Clear list
        list_to_clear = [1, 2, 3]
        del list_to_clear[:]
        print('test list is now deleted: ', list_to_clear)


        # Clone or copy a list
        # We can use the extend() function
        list_original = [1, 2, 3]
        list_clone = []
        list_clone.extend(list_original)
        print('List cloned: ', list_clone)


        # Count occurances of a list for a given number
        occurance = 4
        print('Count of test_list: ', test_list.count(occurance))


        return

# Find sum of elements in list
class ListNumberTen(object):
    def run(self, list):

        return sum(list)

# Multiply all numbers in the list
class ListNumberEleven(object):
    def run(self, list):
        result = 1

        for i in list:
            result *= i

        return result

# Find secont largest element in list
class ListNumberFourteen(object):
    def run(self, list):
        # Sort all elements in ascending order
        # Return second to last elemnent
        arr_size = len(list)

        list.sort()
        return list[arr_size - 2]



# Print even numbers in a list
class ListNumberSixteen(object):
    def run(self, list):

        last_element = len(list) - 1

        for i in range(last_element):
            if i % 2 == 0:
                print(list[i])

        return


# Print odd numbers in a list
class ListNumberSeventeen(object):
    def run(self, list):
        last_element = len(list) - 1

        for i in range(last_element):
            if i % 2 != 0:
                print(list[i])

        return





############################################
# Strings
############################################
class StringNumberOne(object):
    def run(self, string):
        '''
        Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if reverse of the string is same as string.

        Examples:

        Input : malayalam
        Output : Yes

        Input : geeks
        Output : No
        '''
        print(string[::-1])

        if string[::-1] == string:
            return True

        return False

# Check if substring present in string
class StringNumberTwo(object):
    def run(self, string, substring):
        '''
        Given two strings, check if s1 is there in s2.

        Examples:

        Input : s1 = geeks s2=geeks for geeks
        Output : yes

        Input : s1 = geek s2=geeks for geeks
        Output : yes
        '''

        if string.find(substring) == 1:
            return True

        return False

# Print even length of words in a string
class StringNumberThree(object):
    def run(self, string):
        '''
        Given a string. The task is to print all words with even length in the given string.

        Examples:

        Input: s = "This is a python language"
        Output: This
                is
                python
                language

        Input: s = "i am muskan"
        Output: am
                muskan
        '''

        string = string.split(' ') # split each word up

        for word in string:
            if len(word) % 2 == 0:
                print(word)


        return

# Accept the string which contain all vowels
class StringNumberSeven(object):
    def run(self, string):
        '''
        Given a string, the task is to check and accept the given string if contains all vowels


        Example:

        Input : geeksforgeeks
        Output : Not Accepted

        Input : ABeeIghiObhkUul
        Output : Accepted
        '''
        # Plan:
        # create vowels set() which contains vowels
        # check if each element in string is contained in the set()
        # if vowel:
        #   add to set s
        # after coming out of loop, check length of set s
        # if len(s) == len(vowels)

        # set() will conver
        vowels = set('aeiou')
        s = set({})

        # make all characters lowercase
        string = string.lower()

        # Check if character is present inside
        # Vowels set or not
        for char in string:
            if char in vowels:
                s.add(char)
            else:
                pass

        # Check the length of set s equal to length
        # of vowels set or not. if equal, string is
        # accepted, otherwise now
        if len(s) == len(vowels):
            print('Accepted')
        else:
            print('Not accepted')

        return


# Count the number of matching characters in a pair of strings
class StringNumberEight(object):
    def run(self, str1, str2):
        '''
        Given a pair of non empty strings. Count the number of matching characters in those strings (consider the single count for the character which have duplicates in the strings).

        Examples:

        Input : str1 = 'abcdef'
                str2 = 'defghia'
        Output : 4
        (i.e. matching characters :- a, d, e, f)

        Input : str1 = 'aabcddekll12@'
                str2 = 'bb22ll@55k'
        Output : 5
        (i.e. matching characters :- b, 1, 2, @, k)
        '''
        # Use set() to remove all duplicate characters
        # Use a set(intersection) on both strings
        # Return the len(set)

        set_str1 = set(str1)
        set_str2 = set(str2)

        matched_characters = set_str1 & set_str2

        return len(matched_characters)



# Count the number of vowels in the pair of strings
class StringNumberNine(object):
    def run(self, str1):
        '''
        Given a string, count the number of vowels present in given string using Sets.

        Prerequisite: Sets in Python

        Examples:



        Input : GeeksforGeeks
        Output : No. of vowels : 5

        Input : Hello World
        Output : No. of vowels :  3
        '''
        # Create a set() of vowels
        # Match to see if characters in string == vowels
        # If so, add to counter
        # return counter

        counter = 0
        str1 = str1.lower()

        vowels = set(
            'aeiou'
        )

        for char in str1:
            if char in vowels:
                counter+=1


        return counter



# Remove all duplicates from a given string
class StringNumberTen(object):
    def run(self, str1):
        '''
        We are given a string and we need to remove all duplicates from it ? What will be the output if order of character matters ?
        Examples:

        Input : geeksforgeeks
        Output : efgkos
        '''
        # Plan:
        # place string into set() to remove all duplicates
        # now we need to change the output. we will join the set on ''

        string_set = set(str1)

        joined_set = ''.join(string_set)

        return joined_set


# Check if string contains a special character
class StringNumberEleven(object):
    def run(self, str1):
        '''
        Given a string, the task is to check if that string contains any special character (defined special character set). If any special character found, don’t accept that string.


        Examples :

        Input : Geeks$For$Geeks
        Output : String is not accepted.

        Input : Geeks For Geeks
        Output : String is accepted
        '''
        counter = 0
        special_characters = set(
            r'[]\|!@#$%^&*()_+:;,`~./<>?'
        )


        for character in str1:
            if character in special_characters:
                counter+=1


        if counter > 0:
            print('String is not accepted')
        else:
            print('String is accepted')

        return



# Check if string contains a special character
class StringNumberTwelve(object):
    def run(self, str1):





############################################
#  Run code
############################################

test = StringNumberEleven()
print(test.run
            ( 'GeeksForGeeks' )        )

