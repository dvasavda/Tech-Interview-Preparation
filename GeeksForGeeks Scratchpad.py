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


# Find words which are greater than length k
class StringNumberThirteen(object):
    def run(self, str1, k):
        '''
        A string is given and you have to find all the words (substrings separated by a space) which are greater than given length k.

        Examples:

        Input : str = "hello geeks for geeks
                is computer science portal"
                k = 4
        Output : hello geeks geeks computer
                science portal
        Explanation : The output is list of all
        words that are of length more than k.

        Input : str = "string is fun in python"
                k = 3
        Output : string python
        '''
        # Plan:
        # split string on ''
        # count length of each index
        # if count == k:
        #   print (split_string[i])

        split_string = str1.split(' ')
        n = len(split_string)

        for i in range(n):
            char_count = len(split_string[i]) # iterate over each word and get length
            if char_count > k: # if word length is greater than specified, then print
                print(split_string[i])


        return

# Remove i-th character from a string
class StringNumberFourteen(object):
    def run(self, str1, ithcharacter):
        '''
        Given the string, we have to remove the ith indexed character from the string.

        In any string, indexing always start from 0. Suppose we have a string geeks then its indexing will be as –

        g e e k s
        0 1 2 3 4
        Examples :



        Input : Geek
                i = 1
        Output : Gek

        Input : Peter
                i = 4
        Output : Pete
        '''
        # Plan:
        # Typecast string into list() to separate character
        # remove index of ithcharacter from list
        # rejoin list using ''.join, and print

        str_list = list(str1)

        str_list.pop(ithcharacter)

        joined_list = ''.join(str_list)

        return joined_list


# Permutation of a given string using inbuilt function
class StringNumberTwenty(object):
    def run(self, str1):
        from itertools import permutations
        '''
        A permutation, also called an “arrangement number” or “order”, is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.

        Examples:

        Input :  str = 'ABC'
        Output : ABC
                ACB
                BAC
                BCA
                CAB
                CBA

            '''
        perm_list = permutations(str1)

        for i in perm_list:
            ''.join(i)
            print(i)


        return








############################################
# Dictionaries
############################################

# Sort Python dictionaries by Key or Value
class DictNumberOne(object):
    '''
    Problem Statement – Here are the major tasks that are needed to be performed.

    Create a dictionary and display its keys alphabetically.
    Display both the keys and values sorted in alphabetical order by the key.
    Same as part (ii), but sorted in alphabetical order by the value.
    '''
    # Syntax:
    #   mydict[key] = "value"
    #   Key : Value
    #   2 : 56

    # Step 1: Display the Keys alphabetically
    def part_one(self):
        # Declare hash function
        key_value = { }

        # Intialize value
        key_value[2] = 56
        key_value[1] = 2
        key_value[5] = 4
        key_value[4] = 18
        key_value[6] = 91
        key_value[3] = 7

        print('Task 1 - ')
        print('Keys in order are: ')

        # Iterate through each key and print
        for key in (key_value.keys()):
            print(key)

        print('Printing keys as an array form: ')
        print(key_value.keys())


        return


    # Print the values alphabetically
    def part_two(self):
        # Declare hash function
        key_value = { }

        # Intialize value
        key_value[2] = 56
        key_value[1] = 2
        key_value[5] = 4
        key_value[4] = 18
        key_value[6] = 91
        key_value[3] = 7

        print('Values of the dictionary are: ')
        for value in key_value.values():
            print(value)


        print('Values of the dictionary, in sorted form, are: ')
        for sorted_value in sorted(key_value.values()):
            print(sorted_value)

    # Add values to the dict
    def part_three(self):
        word_dict = {
            'Hello'     : 1,
            'Hi'        : 2,
            'Greetings' : 3,
        }

        # Update( {key: value} ) - adds a new key
        word_dict.update( {'What Up' : 4} )

        # Calling Update({}) on an existing key updates the value
        word_dict.update(Hello = 99)

        # Update( [ (key, value), (key, value) ] ) - can add multiple key:value pairs as tuples
        word_dict.update([ ('Ok', 5), ('Where', 6) ])

        print(word_dict)

# Dict access time is O(1)

# Handle missing keys in Python dictionary
class DictNumberTwo(object):
    '''
    In python, dictionaries are containers which map one key to its value with access time complexity to be O(1). But in many applications, the user doesn’t know all the keys present in the dictionaries. In such instances, if user tries to access a missing key, an error is popped indicating missing keys.

    # Python code to demonstrate Dictionary and
    # missing value error

    # initializing Dictionary
    d = { 'a' : 1 , 'b' : 2 }

    # trying to output value of absent key
    print ("The value associated with 'c' is : ")
    print (d['c'])
    Error :

    Traceback (most recent call last):
    File "46a9aac96614587f5b794e451a8f4f5f.py", line 9, in
        print (d['c'])
    KeyError: 'c'

    '''
    def run(self):
        # Use .get()
        dictionary = {'a': 'b'}

        dictionary.get('a', 'b')

        return



# Find sum of all items in the dictionary
class DictNumberFour(object):
    def run(self, dict):

        sum = 0

        for i in dict:
            sum = sum + dict[i]


        return sum


# Delete an item in the dictionary
class DictNumberFive(object):
    def run(self, dict):

        del dict['x']

        return dict


# Dictionary and counter in Python to find winner of election
class DictNumberSix(object):

    def run(self, votes_dict):
        from collections import Counter

        '''
        Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.

        Examples:

        Input :  votes[] = {"john", "johnny", "jackie",
                            "johnny", "john", "jackie",
                            "jamie", "jamie", "john",
                            "johnny", "jamie", "johnny",
                            "john"};
        Output : John
        We have four Candidates with name as 'John',
        'Johnny', 'jamie', 'jackie'. The candidates
        John and Johny get maximum votes.› Since John
        is alphabetically smaller, we print it.
        '''

        # Plan:
        # Convert votes into dictionary using Counter(i)
        # Create another dictionary and count the votes and put it as key
        # Find maximum vote. Get list of candidates
        # Sort list of candidates having same number of max votes

        votes = Counter(votes_dict)

        dict = {}

        for value in votes.value():
            dict[value] = []

        for (key,value) in votes.iteritems():
            dict[value].append(key)

        max_vote = sorted(dict.keys(), reverse = True) [0]

        if len(dict[max_vote]) > 1:
            print(sorted(dict[max_vote]))



        return





############################################
#  Run code
############################################

# test = StringNumberTwenty()
# print(test.run
#             ('ABC'))

test = DictNumberFive()
print(test.run({
    'x' : 10,
    'y' : 20,
    'z' : 30
 }))