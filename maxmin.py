def maxmin(array):
    array.sort()
    smallest = array[0]
    largest = array[len(array)-1]

    return [smallest,largest]

print(maxmin([9,-1,2,3,100,101,-55,-60]))

#remember that array doesn't return a value, it just sorts the existing list

