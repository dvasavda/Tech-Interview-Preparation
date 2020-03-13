# Enter your code here. Read input from STDIN. Print output to STDOUT
# Can you call me instead of using the Google Hangout? (440) 715-0430
# yeah!give me a second
# "V" = 5
# "I" = 1
# "VI" = 5 + 1 = 6
# "VI" -> 6

def romanToInt(roman_number):
    # Roman number mapping with dict
    roman_map = {
                    "I" : 1,
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000
                }

    output = 0
    for i in range(len(roman_number)):
        if i > 0 and roman_map[roman_number[i]] > roman_map[roman_number[i - 1]]:
            output += roman_map[roman_number[i]] - 2 * roman_map[roman_number[i - 1]]
        else:
            output += roman_map[roman_number[i]]
    return output
    # if roman_map[x] > roman_map[x - 1]:
    #     output += roman_map[x] - 2 * roman_map[x - 1]
    
  0    1
["X", "X"]
"I"     output = 1
"XX"    output = 10 + 10 = 20
"VI"
"IV"
"LVIII"
"LIV"       prev = 10 curr = 100
"MCMXCIV"   i = 5 output = 1994
 0123456
10 > 10 -> False



# "I"
# "XX"
# # If the proceeding number is > current number, convert the 
# "VI" = 5 + 1
# "IV" = 5 - 1 = 4
# "LIV" = 50 +(- 1 - 5 = 
# "IV"

# 50 + (1
 
# 50 + (5 - 1 * 2)

# MCMXCIV = 1994 
#         1000 + 900 + 90 + 4
#         1000 + (1000 - 100) + (100 - 10 * 2)
# output = 0


# if roman_map[x] > roman_map[x - 1]:
#     output += roman_map[x] - 2 * roman_map[x - 1]

# IV = 5 - 1 * 2 = 4
# # if the number doesn't have a preceeding numeral, then just add the value
# output = 5 

# ["V", "