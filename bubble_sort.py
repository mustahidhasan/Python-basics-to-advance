# perform a bubble sort assending & decending, make two seperate funcitons

def assending_bubble_sort(values, n):
    # 1. go through each value of the array one by one
    # 2. compare it with the next value. of the array
    # 3. if theif the current value is heigher than the next one one swap the position
    # 4. do it till the last value of the array

    # looping through the whole array except the last index so that during comparing the index do not gets out of index
    for idx in range(n - 1): 
        # the innder comparing loop is also before the last index, just another one is before the 'idx" index too because in each loop run the ith times index of this array is already sorted no need for extra traverse
        for jdx in range(n - idx - 1):
            if values[jdx] > values[jdx + 1]: # when the values of current index is greater than the next one swap 
                values[jdx], values[jdx + 1] = values[jdx + 1], values[jdx] # sorts in assending by swaping positons

    return  values # returns the final sorted array

    

def decending_bubble_sort(values, n):
    # 1. go thorugh the values of the array one at a Time 
    # 2. compare each item with the next item of the array
    # 3. if current value is lower than the next one swap
    # 4. do it till the end item of the array

    # continue the loop before the las element of the array for solving the out of index issue
    for idx in range(n- 1):
        # run this innser loop also before the last elemnt also before the ith element, as the current ith element is already sorted
        for jdx in range(n - idx -1):
            # if the value of the current index of the inner loop is less than the next one swap
            if values[jdx] < values[jdx + 1]:
                values[jdx], values[jdx + 1] = values[jdx + 1], values[jdx] # swap
    return values

    


if __name__ == "__main__":
    values = [12, 4, 5, 9, 0, 2, 100]
    n = len(values) # gets the length of the complete array for the loop breaking logic
    print("Ascending Sort With Bubble Sort: ",assending_bubble_sort(values, n)) # sorts the array from lower to heigher values and prints the array
    print("Decending Sort with Bubble Sort",decending_bubble_sort(values, n)) # sorts the array from height to lower values and prints the array



