# there is given an array find the lowest value amoung the values in the array
# eg, [5, 1, 4, 0, -7, 30], ans is -7
# 1. assing the minvalue variable with the 1st indext value of this array
# 2. Go through the whole array till the last element
# 3. compare the min value with each index value of the array till the last one
# 4. if any lower value than the min value is found update the minvalue with it
# 5. at the end print the min value

array = [5, 1, -4, 0, 7, -9]
minValue = array[0] # assumes that the first item is the lowest
for i in array:
    if i < minValue:
        minValue = i # when gets a new less value than the current one udpates the min value with it
print(minValue)
