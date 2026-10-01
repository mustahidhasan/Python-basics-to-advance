# perform quick sort in the array both descending and ascending.
# divide and conqure

# Ascending:
# 1. 
# 2. 
# 3. 
def partition_ascending(values, low, high):
    piviot = values[high]
    idx = low - 1
    for jdx in range(low, high):
        if values[jdx] <= piviot: # decides whether it should be ascending or descending 
            idx += 1
            values[idx], values[jdx] = values[jdx], values[idx]
    values[idx + 1], values[high] = values[high], values[idx + 1]
    return idx + 1


def quick_sort_ascending(values, low = 0, high = None):
    if high is None: # when it reaches to the last item to ignore the out of index
        high = len(values) - 1 # lenght -1
    if low < high: # as long as the high index is grater than the low that means ther are room for sorting
        piviot = partition_ascending(values, low, high) # return the piviot point where all lower is left and highr is in right of piviot
        quick_sort_ascending(values, low, piviot - 1) # handles the piviot left end breaking logic, sorts entire left sub array
        quick_sort_ascending(values, piviot + 1, high) # handles the piviot right end breaking logic, sorts entire right sub array 
    return values

def partition_descending(values, low, high):
    piviot = values[high] # assumes the hight position value as piviot 
    idx = low - 1 # goes one step behind to traverse the whole array
    for jdx in range(low, high):
        if values[jdx] >= piviot: # puts the hight values in the left , descending order
            idx += 1 # increae the the idex to one index
            values[idx], values[jdx] = values[jdx], values[idx]
    values[idx + 1], values[high] = values[high], values[idx + 1] # swaps woth high value, idx + 1 cox we started one step behind
    return idx + 1


def quick_sort_descending(values, low = 0, high = None):
    if high is None:
        high = len(values) -1 # to avoid index out

    if low < high:
        piviot = partition_descending(values, low, high)
        quick_sort_descending(values, low, piviot - 1) # left side of the array to be sorted 
        quick_sort_descending(values, piviot + 1, high) # right side of the array to be sorted
    return values

if __name__ == "__main__":
    values = [4, 3, 60, 9, 100, 40, 30, 10, 20, 5]
    low = 0
    high = None

    print("Ascending Order:", quick_sort_ascending(values,low, high))
    print("descending Order:", quick_sort_descending(values, low, high))
