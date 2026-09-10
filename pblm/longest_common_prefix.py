# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
# -------------------------------------------------------------------------------------





# Horizontal solution:O(n2)
# 1.  if there is value in the list define the 1st one as the common prefix , that we will compare with others
# 2. define the braking case if the list item is not there or has only one element
# 3. in the outer loop avoid the 1st element and go till the last one
# 4. define a counter for index to count till the matched one, and the ith values as current word
# 5. inner loop goes till the sequence between the current word or common prefix word min value, if one ends no need to compare further thats why
# 6. compare both common and current at jth index, 
# 7. if found update the counter by one, else brek the loop and go for next ith one
# 8. after each inner loop run update the common prefix till the last counter of each inner loop run, thats the longest point
# 9. return the final common prefix with final counter point

def longest_common_prefix(strs):
    common_prefix = strs[0] # assumes the 1st one as common prefix as flag
    if not strs: # if the list is empty
        return ""
    if len(strs) == 1: # if the list has only single string
        return common_prefix
    
    for idx in range(1, len(strs)):
        current_word = strs[idx] # consider all other values without the common prefix
        match = 0
        for jdx in range(min(len(common_prefix), len(current_word))): # which ever is lower it runs till that between common and current

            if common_prefix[jdx] == current_word[jdx]: # if both current and common(assumed) match index  by index then that the point
                match += 1 # increase the counter till that point if matches this point is the point till it matched
            else:
                break
        common_prefix = common_prefix[:match] # overwrites till the matching value

    return common_prefix
   
def longest_common_prefixV(strs):
    pass
if __name__ == "__main__":
    # strs = ["dog","racecar","car"]
    # strs = ["a"]

    strs = ["flower","flow","flight"]
    # strs = ["reflower","flow","flight"]
    # strs = ["aaa","aa","aaa"]

    longest_horizontal = longest_common_prefix(strs)
    print(longest_horizontal)

    longes_vertical = longest_common_prefixV(strs)
