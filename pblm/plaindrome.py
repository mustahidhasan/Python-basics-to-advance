# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def find_plaindrome(x):
    if x < 0:
        return False # if its negative return false
    # flat both 
    original = x 
    reverse = 0
    while x > 0: # as soon as the main number is greter than 0 that means there are digits to look into
        last_digit = x % 10 # get the last digit out of the number
        reverse = (reverse * 10) + last_digit # make a place in the current reverse numner on right side and add the last digit one by one. that makes it reverse of the main one
        x = x//10 # loose the last digit and repeat the process
        
    if original == reverse:
        return True
    else:
        return False
        


if __name__ == "__main__":
    # x = 121
    x = -121
    is_plaindrome = find_plaindrome(x)
    print(is_plaindrome)
