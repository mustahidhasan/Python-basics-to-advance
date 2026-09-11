# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

# stack method
# 1. define an empty list for using as stack
# 2. outer loop go thorugh each elemtn of the sting one at a time and check if there is any opening element (, {. [ if its append it in the stack
# 3. else check is the inttial stack is empty or not return false is empty
# 4. now check the left over closing values and compare it with each pop value of the stack 
# 5. if they do not math with the left over parenthesis with consiqutive opening and closing then return false for each case
# if out of the loop the stack is empty then return true else false 

def valid_parenthesis(s):
    list_of_parenthesis = []
    for chr in range(len(s)):
        if s[chr] == "(" or s[chr] == "{" or s[chr] == "[":
            list_of_parenthesis.append(s[chr])
        else:
            if list_of_parenthesis == []:
                return False
            
            top_parenthesis_match = list_of_parenthesis.pop()
            if s[chr] == ")" and top_parenthesis_match != "(":
                return False
            if s[chr] == "}" and top_parenthesis_match  != "{":
                return False
            if s[chr] == "]" and top_parenthesis_match  != "[":
                return False
    if list_of_parenthesis == []:
        return True
    else:
        return False

    
if __name__ == "__main__":
    s = "()" #true
    # s = "()[]{}" #true
    # s = "(]" #false
    # s = "([])" #true
    # s = "([)]" #false
    is_valid = valid_parenthesis(s)
    print(is_valid)
