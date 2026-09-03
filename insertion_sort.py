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
# 1. 
# 2. 
# 3. 
# 4. 

def insertion_sort_descending_basic(values, n):
    pass

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