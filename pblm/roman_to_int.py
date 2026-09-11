# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 1. map the given values and put the toal to 0 for further adition
# 2. outer loop goes till last one
# 3. considers each item as current vlaue 
# 4. if the current index is less than the len of the whole string means it reaches the last element until that consider the next one of the current vlaue as next value. if its out of index the next value becomes 0
# 5. if the current value is grearter or equal than the next one add that mappes char index value with total
# 6. else deduct it from the total  
def roman_to_int(s):
    roman_int_map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    total = 0
    for char in range(len(s)):
        current_value = roman_int_map[s[char]]
        
        if char + 1 < len(s):
            next_value = roman_int_map[s[char + 1]]
        else:
            next_value = 0


        if current_value >= next_value:
            total += current_value
        else:
            total -= current_value
    return total
    
if __name__ == "__main__":
    s = "III"
    # s = "LVIII"
    # s = "MCMXCIV"
    integer_value = roman_to_int(s)
    print(integer_value)