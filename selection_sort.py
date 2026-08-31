# perform the selection sort both ascending and descending
#BASIC SOLUTION:
#Ascending: [Replacement method]
# 1. Go throguh the whole array till the last item
# 2. compare the current value with all the next values if its less than it or not
# 3. if found a less value put the less value in the current position 
# 4. Do this operation till the last element of the array
def ascending_sort_selection_basic(values, n):
    # outer loop for traversing through the whole array , n - 1 for not going out of index
    for idx in range(n - 1):
        min_index = idx # make the current index as the minimum index assume it.
        # inner loop for comparison traverse, from the next value of current index till the last element of the array. loop will start from next value of i
        for jdx in range(idx+1, n):
            if values[jdx] < values[min_index]: # if the current value of inner loop is less than the assumed min index of array
                min_index = jdx # as min value found the previous assumed min index updated with the current one of jdx. here it finds the most minimum value present in the whole array over inner loop traverse and minindex update
        min_value = values.pop(min_index) # kick the most minimum value out of the current array
        
        values.insert(idx,min_value) # current outer loop actual current position of the array gets the inner found miminum value
    return values






#Descending[Replaceing Method]:
# 1. go throguh the array from till the last element of the array
# 2. compare the current value with the next values, till the last one
# 3. if the current one is greater than the next ones, replace the greater one to the ith index position
# 4. do this till the last element
def descending_sort_selection_basic(values, n):
    # outer loop till the last element, n-1 for not going out of index
    for idx in range(n-1): 
        max_index = idx # assume the ith location index as the mix index for further uupdate
        # innner loop from the next element of current index of i and till the last element of the array
        for jdx in range(idx+1, n):
            if values[jdx] > values[max_index]: # if the valued of j indexes are somehow greater than the current assumed max index
                max_index = jdx # update the max index with the current greater value index
        max_value = values.pop(max_index) # removes the max element from the array 
        values.insert(idx, max_value)
    return values




# Optimized Solution:
#Ascending:
# 1. go through the whole array till the last element  outer loop, also make an assumption of min indexed value as the current ith index
# 2. compare the current index value with all the values in the array on each run inner loop
# 3. compare current value index with min_index value if its less in comparing upcoming values update the min_index
# 4. swap the current ith value with the updated min index value 
def ascending_sort_selection(values, n):
    for idx in range(n-1): # outer loop till the before the last element solves out of index
        min_index = idx # assume the ith index is the min index value
        for jdx in range(idx, n):
            if values[jdx] < values[min_index]: # if the values are less than the min index flag update the minindex
                min_index = jdx # updates the min index
        values[idx], values[min_index] = values[min_index], values[idx] # swaps the value of current ith index with the minindexed value, thus we gets the less selection the lowes one gets in the intial position faster
    return values



    
#Descending:
# 1. 
# 2. 
# 3. 
# 4.
def descending_sort_selection(values, n):
    pass


if __name__ == "__main__":
    values = [12, 5, 4, 9, 0, 2, 100]
    print("Main Array: ", values)
    n = len(values) # for the breaking logic of the loops 
    print("Ascending Sort with Selection Sort(BASIC)", ascending_sort_selection_basic(values, n))
    print("Descending Sort with Selection Sort(BASIC)", descending_sort_selection_basic(values, n))
    print("Ascending Sort with Selection Sort(OPTIMIZED)", ascending_sort_selection(values, n))
    # print("Descending Sort with Selection Sort(OPTIMIZED)", descending_sort_selection(values, n))
