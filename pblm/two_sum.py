# two sum basic solution,
# 1. starts forom the begining element of the array goes till the last one n - 1 for not going out of index
# 2. innner loop srarts form the next of outer loop index idx + 1 and goes till the last one
#     it starts form the idx+1 because so that it compares from the next value when i use the idx during adding with other values
#     add the outer loop idx with the inner loop jdx, this reduces the channce of going out of index for the jdx
# 3. when the values of addition matches the target value return the array of both idx and jdx as additional points 
def twoSum(nums, target):
    for idx in range(len(nums) - 1):
        for jdx in range(idx + 1, len(nums)):
            # here the idx holds the value that is stand anole adding and comparing with all its next values till the end            
            if nums[idx] + nums[jdx] == target:
                return [idx, jdx]


# solve this two sum pro solution same way just in O(n) time complexity
def twoSumPro(nums, target):
    pass


if __name__ == "__main__":
    values = [3, 2, 3]
    target = 6
    # perform two sum in this array when any value of two number is equal of the target one return both index
    
    twoSum = twoSum(nums=values, target=target)
    print("Two sum basic",twoSum)

    two_sum_pro = twoSumPro(nums = values, target = target)