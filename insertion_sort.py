# perform the insertion sort here with the array, assending and descending both

# Basic Pop replace method
#ASSENDING:
# 1. Go through the whole array from 1 to n, skip the 1st value in outer loop
# 2. inner traverse goes backwards and compares the current one with the with current value gets popped out and that value is compared with the all values and find its index to put it 
# 3. when the position is found and current vlue is less than the other values put it in the outer index thats its actual position
# 4. DO it for all


def insertion_sort_assending_basic(values, n):
    print(values)
    # outer loop starts from the 2nd element skips the 1st one, as a position to put the sorted ones, in each circle the front place becomes a place to put the sorted entry
    for idx in range(1, n):
        # starts from the 0 the 1st element of the array in reverse counter order, till 0. It moves backward so that the elements can be inserted easily in front of the current value. Putting the sorted entries are easier that putting them in the fornt.

        insert_index = idx # gets the insert index where to put it

        current_value = values.pop(idx) # gets the current value out and stores for placing in a new place

        # inner loop starts from one steps behind than the ith, moves backward, 1 deducts each time 
        for jdx in range(idx - 1, -1 , -1):

            # compare the current ith index value with all the values in the array
            if values[jdx] > current_value: # if value is greater than the flagged current value
                insert_index = jdx # there is a greater value that the targeted one and this becomes the new index to move forward
        values.insert(insert_index, current_value) # inserts the sorted value in the 
    return values



#Descending:
# 1. Outer loop goest from the 1th element and skips the 0th one and goes till the last one, flag the current index and current value gets popped out for leaveigng a place to set the sorted value
# 2. innser loop moves backward, till 0 each time, starts form the previous value of ith value, backward because it makers easier to insert the sorted value in actual position
# 3. if the current ith value is height that the other one in the inner loop then make this one the insertion index and put the ith value there 
# 4. DO it for all the values in the array

def insertion_sort_descending_basic(values, n):
    # outer loop from 1th element till the last one, keeping the previous value of ith one always empty to get the sorted one to be inserted
    for idx in range(1,n):
        insert_index = idx # current index to be get inserted with sorted value

        current_value = values.pop(idx) # pops the current value to make an empty palce to insert it in its appropiate position

        #inner loop backward , from the previous element of the outher loop
        for jdx in range(idx - 1, -1, -1):
            if values[jdx] < current_value: # if the current value is heigher that means this becomes the updated one to be inserted on
                insert_index = jdx # that means there are more heigher value and that insertion point
        values.insert(insert_index, current_value)
    return values




# Optimised way: Copy past mehthod.
#ASSENDING:
# 1. 
# 2. 
# 3. 
# 4.
def insertion_sort_assending_optimized(values, n):
    pass


#Descending:
# 1. 
# 2. 
# 3. 
# 4. 

def insertion_sort_descending_optimized(values, n):
    pass

if __name__ == "__main__":
    values = [5, 2, 0, 19, 100, 55, 30, 10, 20]
    n = len(values)
    print("Insertion Sort Ascending: (BASIC)", insertion_sort_assending_basic(values, n))
    print("Insertion Sort Descending (BASIC): ", insertion_sort_descending_basic(values, n))
    # print("Insertion Sort Ascending: ", insertion_sort_assending_optimized(values, n))
    # print("Insertion Sort Descending: ", insertion_sort_descending_optimized(values, n))